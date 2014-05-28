from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from unittest import TestCase

from individual import make_payload


class MakePayloadTests(TestCase):
    def setUp(self):
        TestCase.setUp(self)
        n = 125901055307842980415913392605238281157588717994184931769756254728022255206666612297633321243585174817389685911286457203649571385978289818145687398602711727256472196414661863208391088365507187635474354157033288702668364847480161810462431111611186393510163416349638084806419758244686369426767073819580997473839
        e = 65537L
        d = 59676066681154681228007593083130475393736910993352773555330703219117190834793958289419434687439612288133317105577040550744927072249715350273549801641738810109249280903322912212761576808790805681023212954997857478202683898911968626615328112858226815497039645092542207851077987913075530419461990429057793357505L
        p = 10921735883887675853232351186527903319002450669215143140618024602262892880543036563121422567831251215548039469308400235795107232555381951876814275131726597L
        q = 11527568204023217219810969226479706526632083100746947623440394171589126500689184535305009967686414578591319763848646201407965575400540428110128240432986787L
        u = 9998090784357828579141729403446713021466573403228511568791615422601543040009583646767719904315243094732840620944299325208637513675705796750926655871134707L
        self.key = RSA.construct((n, e, d, p, q, u))
        self.cipher = PKCS1_OAEP.new(self.key)

    def test_data_is_single_pair_of_strings(self):
        data = {'name': 'name'}

        _, actual = make_payload(self.key.publickey(), data)
        self.assertEqual(self.cipher.decrypt(actual['name']), data['name'])

    def test_data_is_multiple_pair_of_strings(self):
        data = {'name': 'name',
                'phone': '123-456-7890'}

        _, actual = make_payload(self.key.publickey(), data)
        self.assertEqual(self.cipher.decrypt(actual['name']), data['name'])
        self.assertEqual(self.cipher.decrypt(actual['phone']), data['phone'])

    def test_data_is_a_list_of_strings(self):
        data = {'phone': ['123-456-7890', '098-765-4321']}

        _, actual = make_payload(self.key.publickey(), data)
        for i, number in enumerate(data['phone']):
            result = self.cipher.decrypt(actual['phone'][i])
            self.assertEqual(result, number)

    def test_data_is_a_dictionary(self):
        data = {'phone': {'mobile': '123-456-7890', 'home': '098-765-4321'}}

        _, actual = make_payload(self.key.publickey(), data)
        for name, number in data['phone'].items():
            result = self.cipher.decrypt(actual['phone'][name])
            self.assertEqual(result, number)

