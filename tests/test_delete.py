import unittest
from mockstore.client import create_mock_client


class TestDelete(unittest.TestCase):
    
    def setUp(self) -> None:
        self.client = create_mock_client()
        self.client.collection("lol").document("pp").set({"Hello": "hello"})
    
    def test_delete(self):
        self.client.collection("lol").document("pp").delete()
        result = self.client.collection("lol").document("pp").get().to_dict()
        self.assertEqual(result, None)