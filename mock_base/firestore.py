from .mockstore.mock import  MockClient
from .mockstore.firestore_impl.client import Client


def create_firestore_mock_client() -> Client:
    return MockClient()
