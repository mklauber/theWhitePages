import logging
logger = logging.getLogger(__name__)


class Server(object):
    def __init__(self, name):
        self.name = name
        self.data = {}

    def set(self, name, data):
        self.data[name] = data


    def get(self, name):
        return self.data[name]
