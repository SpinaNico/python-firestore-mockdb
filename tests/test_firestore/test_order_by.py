from mock_base.mock_store import create_firestore_mock_client
import unittest


class TestOrderBy(unittest.TestCase):
    
    def setUp(self) -> None:
        self.client = create_firestore_mock_client()
        self.result = [
            {"id": 0}, {"id": 1}, {"id": 2},
            {"id": 4}, {"id": 5}, {"id": 7},
            {"id": 8}, {"id": 9}, {"id": 10}
        ]
        self.client.collection("good").add({"id": 9})
        self.client.collection("good").add({"id": 2})
        self.client.collection("good").add({"id": 4})
        self.client.collection("good").add({"id": 5})
        self.client.collection("good").add({"id": 7})
        self.client.collection("good").add({"id": 8})
        self.client.collection("good").add({"id": 10})
        self.client.collection("good").add({"id": 0})
        self.client.collection("good").add({"id": 1})

    def tearDown(self) -> None:
        del self.client
        
    def test_order_ascending_and_limit(self):
        result = [i.to_dict() for i in self.client.collection("good").order_by("id").limit(3).stream()]
        self.assertListEqual(result, self.result[:3])

    def test_order_ascending(self):
        result = [i.to_dict() for i in self.client.collection("good").order_by("id").stream()]
        self.assertListEqual(result, self.result)

    def test_order_descending(self):
        result = [i.to_dict() for i in self.client.collection("good").order_by("id", direction="DESCENDING").stream()]
        self.result.reverse()
        self.assertListEqual(result, self.result)