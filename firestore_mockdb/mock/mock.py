from .firestore_impl.client import Client, Query, DocumentReference, DocumentSnapshot, CollectionReference
from ._fx import error_path_not_is_document, error_path_not_is_collection
from ._db import Col, Doc, _DatabaseRaw
from typing import List, Optional, Iterable


class MockDocument(DocumentReference):
    
    def __init__(self, path: List[str], database: _DatabaseRaw):
        self._database = database
        self.__path: List[str] = path
    
    @property
    def path(self) -> str:
        return ".".join(self.__path)
    
    @property
    def id(self) -> str:
        return self.__path[-1]
    
    @property
    def parent(self) -> CollectionReference:
        return MockCollection(self.__path[:-2], self._database)
    
    def collection(self, collection_id) -> CollectionReference:
        return MockCollection(self.__path + [collection_id], self._database)
    
    def create(self, document_data):
        self.set(document_data, merge=False)
    
    def set(self, document_data, merge=False):
        
        e = self._database.search_path(self.__path, make=True)
        
        if isinstance(e, Doc):
            
            if merge is False:
                e.data = document_data
            else:
                
                if e.data is not None:
                    e.data = {**e.data, **document_data}
                else:
                    e.data = document_data
        
        else:
            raise Exception(error_path_not_is_document(self.__path))
    
    def update(self, field_updates, option=None):
        pass
    
    def delete(self, option=None):
        pass
    
    def get(self, field_paths=None, transaction=None) -> DocumentSnapshot:
        return MockSnapshot(self.__path, self._database)
    
    def collections(self, page_size=None) -> List[CollectionReference]:
        e = self._database.search_path(self.__path, make=False)
        if e is None:
            return []
        if isinstance(e, Doc):
            return [MockCollection(self.__path + [i.name], self._database) for i in e.cols]
        else:
            raise Exception(error_path_not_is_document(self.__path))
    
    def on_snapshot(self, callback):
        raise Exception("Not implemented")


class MockClient(Client):
    
    def __init__(self):
        self._database = _DatabaseRaw()
    
    def collection(self, *collection_path) -> CollectionReference:
        path: List[str] = []
        
        for i in collection_path:
            path += str(i).split("/")
        return MockCollection(path, self._database)
    
    def document(self, *document_path) -> DocumentReference:
        path: List[str] = []
        for i in document_path:
            path += str(i).split("/")
        return MockDocument(path, self._database)
    
    @staticmethod
    def field_path(*field_names):
        raise Exception("Not implemented")
    
    def get_all(self, references, field_paths=None, transaction=None):
        raise Exception("Not implemented")
    
    def collections(self) -> List[CollectionReference]:
        cols: List[CollectionReference] = []
        for k in self._database.database:
            cols.append(MockCollection([k.name], self._database))
        
        return cols
    
    def transaction(self, **kwargs) -> Client:
        return self


class MockSnapshot(DocumentSnapshot):
    
    def __init__(self, path: List[str], database: _DatabaseRaw):
        assert database is not None, "database raw is None"
        self._database: _DatabaseRaw = database
        self.__path: List[str] = path
    
    @property
    def exists(self) -> bool:
        e = self._database.search_path(self.__path, make=False)
        if e is None:
            return False
        return True
    
    @property
    def id(self) -> str:
        return self.__path[-1]
    
    @property
    def reference(self) -> DocumentReference:
        return MockDocument(self.__path, self._database)
    
    def get(self, field_path):
        e = self._database.search_path(self.__path, make=False)
        if e is None:
            return None
        
        if isinstance(e, Doc):
            s = field_path.split(".")
            if e.data is not None:
                result = e.data
                for i in s:
                    result = result.get(i, {})
                return result
            else:
                return None
        else:
            raise Exception(error_path_not_is_document(self.__path))
    
    def to_dict(self) -> Optional[dict]:
        
        e = self._database.search_path(self.__path, make=False)
        
        if e is None:
            return None
        if isinstance(e, Doc):
            if e is None:
                return None
            if e.data is not None:
                return e.data
            else:
                return None
        else:
            raise Exception(error_path_not_is_document(self.__path))


class MockQuery(Query):
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"
    
    def __init__(self, col: Col):
        self.__col = col
    
    def select(self, field_paths) -> Query:
        pass

    def where(self, field_path, op_string, value) -> Query:
        pass

    def order_by(self, field_path, direction=ASCENDING) -> Query:
        pass

    def limit(self, count) -> Query:
        pass

    def offset(self, num_to_skip) -> Query:
        pass

    def start_at(self, document_fields) -> Query:
        pass

    def start_after(self, document_fields) -> Query:
        pass

    def end_before(self, document_fields) -> Query:
        pass

    def end_at(self, document_fields) -> Query:
        pass

    def get(self, transaction=None):
        pass

    def stream(self, transaction=None) -> Iterable[DocumentSnapshot]:
        for i in self.__col.docs:
            yield MockDocument

    def on_snapshot(self, callback):
        pass


class MockCollection(MockQuery, CollectionReference):
    
    def __init__(self, path: List[str], database: _DatabaseRaw):
        assert database is not None, "database Raw is None"
        self._database = database
        e = self._database.search_path(path)
        if isinstance(e, Col):
            super().__init__(e)
        else:
            raise error_path_not_is_collection(path)
        self.__path: List[str] = path
        
        
    @property
    def id(self) -> str:
        return self.__path[-1]
    
    @property
    def parent(self) -> Optional[DocumentReference]:
        if len(self.__path) > 2:
            return MockDocument(self.__path[:-1], self._database)
        else:
            return None
    
    def document(self, document_id: Optional[str] = None) -> DocumentReference:
        if document_id is None:
            raise Exception("document id is None")
        else:
            return MockDocument(self.__path + [document_id], self._database)
    
    def add(self, document_data, document_id=None) -> DocumentReference:
        doc_id = document_id
        if doc_id is None:
            doc_id = self._database.random_id()
        
        m = MockDocument(self.__path + [doc_id], self._database)
        m.set(document_data)
        return m
    
    def list_documents(self, page_size=None) -> List[DocumentReference]:
        e = self._database.search_path(self.__path)
        if isinstance(e, Col):
            result: List[DocumentReference] = [MockDocument(self.__path + [i.name], self._database) for i in e.docs]
            print(len(result))
            if page_size is None:
                return result
            else:
                if len(result) < page_size:
                    return result
                else:
                    return result[:page_size]
        
        else:
            raise Exception(error_path_not_is_collection(self.__path))
