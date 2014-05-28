import logging
logger = logging.getLogger(__name__)


def enc(msg, key):
    n, e = key
    return (msg ** e) % n


class User(object):
    def __init__(self, name, pub, priv, server):
        logger.info('%s has access to:', name)
        logger.info('\tPubKey:%s', pub)
        logger.info('\tPrivKey:%s', priv)

        self.name = name
        self.pub = pub
        self.priv = priv
        self.server = server
        self.address = 31

    def post(self, name, pub_key):
        logger.info('%s has access to her address %s', self.name, self.address)
        logger.info('%s has access to bob\'s key %s', self.name, pub_key)
        crypted = enc(self.address, pub_key)
        logger.debug('msg: %s, crypt: %s', self.address, crypted)
        self.server.set(name, crypted)
        return self.server

    def get(self, server, name=None):
        name = self.name if name == None else name
        crypt = server.get(name)
        logger.info('%s can get access to %s encrypted address %s', self.name, name, crypt)
        return enc(crypt, self.priv)
