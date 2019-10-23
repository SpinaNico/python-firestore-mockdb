import unittest
from mock_base.firestore import create_firestore_mock_client


class TestSubCollection(unittest.TestCase):

    def setUp(self) -> None:
        self.client = create_firestore_mock_client()
    
    def tearDown(self) -> None:
        del self.client
    
    def test_sub_collection(self):
        self.client.collection("goog").document("hello").collection("hi").document("by").set({
            "hi": "hi"
        })
        
        doc = self.client.collection("goog").document("hello").collection("hi").document("by").get()
        
        self.assertEqual(doc.exists, True)
        self.assertDictEqual(doc.to_dict(), {"hi": "hi"})
