from mockstore.client import create_mock_client
import unittest


class TestCursor(unittest.TestCase):
    
    def setUp(self) -> None:
        self.client = create_mock_client()
        
        self.result = [
            {"name": "mario"}, {"name": "andrea"}, {"name": "paolo"},
            {"name": "giovanni"}, {"name": "matteo"}, {"name": "mary"},
            {"name": "???"}
        ]
        
        for i in range(0, len(self.result)):
            self.client.collection("lol").document(str(i)).set(self.result[i])
        
    def tearDown(self) -> None:
        del self.client
        
    def test_start_at(self):
        result = [i.to_dict() for i in self.client.collection("lol").start_at("4").stream()]
        self.assertEqual(len(result), 3)
        self.assertListEqual(result, self.result[4:])

    def test_start_after(self):
        result = [i.to_dict() for i in self.client.collection("lol").start_after("4").stream()]
        self.assertEqual(len(result), 2)
        self.assertListEqual(result, self.result[5:])
    
    def test_end_at(self):
        result = [i.to_dict() for i in self.client.collection("lol").end_at("4").stream()]
        self.assertEqual(len(result), 5)
        self.assertListEqual(result, self.result[:5])

    def test_end_before(self):
        result = [i.to_dict() for i in self.client.collection("lol").end_before("4").stream()]
        self.assertEqual(len(result), 4)
        self.assertListEqual(result, self.result[:4])
