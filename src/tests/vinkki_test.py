import unittest
from vinkki import Vinkki


class TestMain(unittest.TestCase):
    def setUp(self):
        self.vinkki = Vinkki()

    def testaa_vastaus(self):
        self.assertEqual(self.vinkki.vastaus(), "Hello Hello!")
