
from mock_base.mockstore.firestore_impl.client import Client as MockClient

from _firebase.firebase_admin.firestore import firestore
from _firebase.firebase_admin import auth
from _firebase.firebase_admin import storage


def get_without_underscore(what):
    
    l = dir(what)
    r = []
    for i in l:
        if not i.startswith("_"):
            r.append(i)
    
    return len(r)


if __name__ == "__main__":
    print(
        "firestore: [{}/{}]".format(
            get_without_underscore(MockClient),
            get_without_underscore(firestore.Client)
        )
    )