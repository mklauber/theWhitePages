import logging

import dht
from individual import User
from server import Server


logger = logging.getLogger(__name__)

pubA, privA = (55, 7), (55, 23)
pubB, privB = (91, 5), (91, 29)
pubC, privC = (3120, 17), (3120, 2753)


if __name__ == '__main__':
    logging.basicConfig(level='INFO')

    alice = User(Server('ServerA'))
    bob = User(Server('ServerB'))
    eve = User(Server('ServerC'))

    server = alice.post(bob.pubkey, {'name':'name'})
    print server.data
    b = bob.get(server)

    print "Alice's name == %s" % 'name'
    print "Bob determines Alice's Address == %s" % b
