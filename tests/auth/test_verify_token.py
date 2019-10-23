import unittest
from mock_base.fake_device import FakeDevice
from mock_base.auth import verify_id_token
from mock_base import initialize_mock_app


class TestDevice(unittest.TestCase):
    
    def setUp(self) -> None:
        initialize_mock_app()
    
    def test_device(self):
        device = FakeDevice("hello")
        token = device.get_id_token()
        resolved_token = verify_id_token(token)
        self.assertEqual(resolved_token.get("uid"), "hello")