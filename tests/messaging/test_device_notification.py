from mock_base.fake_device import FakeDevice
from mock_base import initialize_mock_app, delete_mock_app, Notification, Message
from mock_base import mock_messaging
import unittest


class TestDeviceNotify(unittest.TestCase):
    
    def setUp(self) -> None:
        self.app = initialize_mock_app()
        self.device = FakeDevice("example")
    
    def tearDown(self) -> None:
        delete_mock_app(self.app)
    
    def test_recived(self):
        m = Message(
            notification=Notification(
                body="Hello World"
            ),
            token=self.device.device_id_token()
        )
        mock_messaging.send(message=m)
        
        self.assertEqual(len(self.device.messages), 1)
        self.assertEqual(self.device.messages[0].token, self.device.device_id_token())
        self.assertEqual(self.device.messages[0].notification.body, "Hello World")