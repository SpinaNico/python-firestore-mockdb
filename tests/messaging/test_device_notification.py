from mock_base.fake_device import FakeDevice
from mock_base import initialize_app, delete_app
from mock_base.messaging import send, Message, Notification
import unittest


class TestDeviceNotify(unittest.TestCase):
    
    def setUp(self) -> None:
        self.app = initialize_app()
        self.device = FakeDevice("example")
    
    def tearDown(self) -> None:
        delete_app(self.app)
    
    def test_recived(self):
        m = Message(
            notification=Notification(
                body="Hello World"
            ),
            token=self.device.device_id_token()
        )
        send(message=m)
        
        self.assertEqual(len(self.device.messages), 1)
        self.assertEqual(self.device.messages[0].token, self.device.device_id_token())
        self.assertEqual(self.device.messages[0].notification.body, "Hello World")