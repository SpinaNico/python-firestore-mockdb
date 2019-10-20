from __future__ import annotations
from typing import List, Optional
from abc import ABC, abstractmethod


class Getter(ABC):
    def __init__(self):
        self.name: str = "_"
        
    @abstractmethod
    def get(self, name: str, make: bool = False) -> Optional[Getter]:
        pass
    

class Col(Getter):
    
    def __init__(self):
        super().__init__()
        self.docs: List[Doc] = []

    def get(self, name: str, make: bool = False) -> Optional[Getter]:
        for i in self.docs:
            if i.name == name:
                return i
        if make is False:
            return None
        else:
            d = Doc()
            d.name = name
            self.docs.append(d)
            return d


class Doc(Getter):
    
    def __init__(self):
        super().__init__()
        self.data: Optional[dict] = None
        self.cols: List[Col] = []
        
    def get(self, name: str, make: bool = False) -> Optional[Getter]:
        for i in self.cols:
            if i == name:
                return i
        if make is False:
            return None
        else:
            c = Col()
            c.name = name
            self.cols.append(c)
            return c