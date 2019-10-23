from __future__ import annotations
from . import MockApp, _apps, _DEFAULT_APP_NAME


def send(message: Message, dry_run=False, app: MockApp = None):
    if app is None:
        _a = _apps.get(_DEFAULT_APP_NAME)
        _a.notify_listeners(message)
    else:
        _a = _apps[app.name]
        _a.notify_listeners(message)
    

class Notification(object):
  
    def __init__(self, title=None, body=None):
        self.title = title
        self.body = body


class Message(object):
 
    def __init__(self,
                 data=None,
                 notification=None,
                 android=None,
                 webpush=None,
                 apns=None,
                 token=None,
                 topic=None,
                 condition=None):
        self.data = data
        self.notification = notification
        self.android = android
        self.webpush = webpush
        self.apns = apns
        self.token = token
        self.topic = topic
        self.condition = condition
