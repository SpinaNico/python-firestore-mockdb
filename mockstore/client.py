from .mock.mock import MockClient
from .mock.firestore_impl.client import Client


def create_mock_client() -> Client:
    return MockClient()
