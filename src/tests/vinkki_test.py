import unittest
from optparse import make_option
from vinkki import Vinkki


class TestMain(unittest.TestCase):
    def setUp(self):
        self.vinkki = Vinkki()

    def viesti(self):
        self.assertEqual(self.vinkki.vastaus(), "Hello Hello!")

