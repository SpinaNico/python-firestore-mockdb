from mock_base.firestore import create_firestore_mock_client
import unittest


class TestCreateDocument(unittest.TestCase):
    
    def setUp(self) -> None:
        self.client = create_firestore_mock_client()
        
    def tearDown(self) -> None:
        del self.client
    
    def test_set(self):
        self.client.collection("hello").document("hello1").set(document_data={
            "hello": "hello"
        })
        
        doc = self.client.collection("hello").document("hello1").get()
        dic = doc.to_dict()
        self.assertDictEqual(dic, {
            "hello": "hello"
        })
        self.assertEqual(doc.exists, True)
    
    def test_create(self):
        self.client.collection("hello").document("hello").create({"hola": "hello"})
        
        doc = self.client.collection("hello").document("hello").get()
        self.assertEqual(doc.exists, True)
        dic = doc.to_dict()
        self.assertIsInstance(dic, dict)
        self.assertEqual(dic, {"hola": "hello"})
    
    def test_list_document(self):
        self.client.collection("hello").document("hello2").create({"hola": "hello"})
        
        l = self.client.collection("hello").list_documents()
        self.assertIsInstance(l, list)
        self.assertEqual(len(l), 1)
    
    def test_add_document(self):
        self.client.collection("h").add({})
        self.client.collection("h").add({}, document_id="ciao")
        
        l = self.client.collection("h").list_documents()
        self.assertIsInstance(l, list)
        
        self.assertEqual(len(l), 2)
        
        doc = self.client.collection("h").document("ciao").get()
        self.assertEqual(doc.exists, True)
        self.assertEqual(doc.id, "ciao")
