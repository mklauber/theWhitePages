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
        self.key = key if key else RSA.generate(1024)
        self.server = server

    def post(self, pubkey, data):
        """Post a piece of data to a server for a user."""
        crypted = pubkey
        logger.debug('msg: %s, crypt: %s', self.address, crypted)
        self.server.set(pubkey, crypted)
        return self.server

    def get(self, server):
        """Request a piece of data from a server"""
        crypt = server.get(self.key.publickey())
        return self.key.decrypt(crypt)

    def migrate(self, server):
        pass


def make_payload(key, data):
    """Given a json compatible data structure, create new version where the
    structure is the same, but the values are all encrypted with the public key
    """
    cipher = PKCS1_OAEP.new(key)
    payload = {}
    for k, v in data.items():
        if isinstance(v, collections.Mapping):
            _, payload[k] = make_payload(key, v)
        elif hasattr(v, '__iter__'):
            payload[k] = [cipher.encrypt(item) for item in v]
        else:
            payload[k] = cipher.encrypt(v)
    return key, payload
