import unittest
from mockstore.client import create_mock_client


class TestSelect(unittest.TestCase):
    
    def setUp(self) -> None:
        self.client = create_mock_client()
        self.client.collection("hello").add({"field1": "1", "field2": "2", "field3": "3", })
        
    def test_select_one_field(self):
        result = [i.to_dict() for i in self.client.collection("hello").select(["field1"]).stream()]
        self.assertListEqual(result, [{"field1": "1"}])
    
    def test_select_two_field(self):
        result = [i.to_dict() for i in self.client.collection("hello").select(["field1", "field2"]).stream()]
        self.assertListEqual(result, [{"field1": "1", "field2": "2"}])