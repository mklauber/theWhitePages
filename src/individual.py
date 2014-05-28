from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import collections
import logging


logger = logging.getLogger(__name__)
enc = None

def make_key(text):
    return RSA.importKey(text)


class User(object):

    @classmethod
    def load(cls, file):
        """Reads data from the file, and returns a new instance of User."""
        return None

    def __init__(self, server, key=None):
        """Create a new User."""
        self.key = key if key != None else RSA.generate(1024)
        self.pubkey = self.key.publickey()
        self.server = server

    def post(self, pubkey, data):
        """Post a piece of data to a server for a user."""
        _, crypted = encrypt_payload(pubkey, data)
        self.server.set(pubkey.exportKey(), crypted)
        return self.server

    def get(self, server):
        """Request a piece of data from a server"""
        crypt = server.get(self.pubkey.exportKey())
        return decrypt_payload(self.key, crypt)[1]

    def migrate(self, server):
        pass


def encrypt_payload(key, data):
    """Given a json compatible data structure, create new version where the
    structure is the same, but the values are all encrypted with the public key
    """
    cipher = PKCS1_OAEP.new(key)
    payload = {}
    for k, v in data.items():
        print k, v
        if isinstance(v, collections.Mapping):
            _, payload[k] = make_payload(key, v)
        elif hasattr(v, '__iter__'):
            payload[k] = [cipher.encrypt(item) for item in v]
        else:
            payload[k] = cipher.encrypt(v)
    return key, payload


def decrypt_payload(key, data):
    """Given a json compatible data structure, create new version where the
    structure is the same, but the values are all encrypted with the public key
    """
    cipher = PKCS1_OAEP.new(key)
    payload = {}
    for k, v in data.items():
        if isinstance(v, collections.Mapping):
            _, payload[k] = decrypt_payload(key, v)
        elif hasattr(v, '__iter__'):
            payload[k] = [cipher.decrypt(item) for item in v]
        else:
            payload[k] = cipher.decrypt(v)
    return key, payload

