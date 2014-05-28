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

    alice = User('alice', pubA, privA, Server('ServerA'))
    bob = User('bob', pubB, privB, Server('ServerB'))
    eve = User('eve', pubC, privC, Server('ServerC'))

    server = alice.post(bob.name, pubB)
    server = alice.post(eve.name, pubC)
    b = bob.get(server)
    e = eve.get(server, name='bob')
    print "Alice's Address == %s" % alice.address
    print "Bob determines Alice's Address == %s" % b
    print "Eve determines Alice's Address == %s" % e
