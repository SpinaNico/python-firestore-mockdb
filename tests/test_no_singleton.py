from firestore_mockdb.client import create_mock_client
import unittest


class TestNoSingleton(unittest.TestCase):
    
    def test_single_db(self):
        client1 = create_mock_client()
        client2 = create_mock_client()
        
        self.assertNotEqual(id(client1), id(client2))
        