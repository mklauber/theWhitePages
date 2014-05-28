import logging
logger = logging.getLogger(__name__)


class Server(object):
    def __init__(self, name):
        self.name = name
        self.data = {}

    def set(self, name, data):
        logger.info('%s knows the encrypted address for %s is %s', self.name, name, data)
        logger.debug('ID: %s, data: %s', name, data)
        self.data[name] = data


    def get(self, name):
        logger.debug('ID: %s, data: %s', name, self.data[name])
        return self.data[name]
