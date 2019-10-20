from firestore_mockdb.mock_db import create_mock_client
import unittest


class TestCreateDocument(unittest.TestCase):
    
    def setUp(self) -> None:
        self.client = create_mock_client()
    
    def test_set(self):
        self.client.collection("hello").document("hello").set(document_data={
            "hello": "hello"
        })
        
        doc = self.client.collection("hello").document("hello").get().to_dict()
        self.assertDictEqual(doc, {
            "hello": "hello"
        })
