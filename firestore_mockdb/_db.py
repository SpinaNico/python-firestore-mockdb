from __future__ import annotations
from typing import List, Optional
from abc import ABC, abstractmethod


class Getter(ABC):
    name: str = "_"
    @abstractmethod
    def get(self, name: str, make: bool = False) -> Optional[Getter]:
        pass
    

class Col(Getter):
    docs: List[Doc] = []

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
    data: Optional[dict] = None
    cols: List[Col] = []
    
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