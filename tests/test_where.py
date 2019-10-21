from firestore_mockdb.client import create_mock_client
import unittest


class TestWhere(unittest.TestCase):
    
    def setUp(self) -> None:
        self.client = create_mock_client()
        self.client.collection("good").add({
            "number": 1,
            "pearson": 4,
            "name": "Mario"
        })

        self.client.collection("good").add({
            "number": 2,
            "pearson": 3,
            "name": "Paolo"
        })

        self.client.collection("good").add({
            "number": 4,
            "pearson": 7,
            "name": "Leo"
        })

        self.client.collection("good").add({
            "number": 1,
            "pearson": 9,
            "name": "Mary"
        })
        
    def tearDown(self) -> None:
        del self.client
    
    def test_op_string_less_equal(self):
        result = []
        for i in self.client.collection("good").where("pearson", "<=", 3).stream():
            result.append(i.to_dict())
            
        self.assertEqual(len(result), 1, "")
        self.assertDictEqual(result[0], {"number": 2, "pearson": 3, "name": "Paolo"})

    def test_op_string_equal(self):
        result = []
        for i in self.client.collection("good").where("number", "==", 1).stream():
            result.append(i.to_dict())

        self.assertEqual(len(result), 2, "")