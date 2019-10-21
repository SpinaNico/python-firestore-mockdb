import unittest
from firestore_mockdb.mock._db import Doc


class TestDoc(unittest.TestCase):
    
    def test_square_bracket(self):
        d = Doc()
        d.data = {"hello": "hello"}
        self.assertEqual(d["hello"], "hello")