import unittest
from vinkki import Vinkki


class TestMain(unittest.TestCase):
    def setUp(self):
        self.vinkki = Vinkki()

    def testaa_vastaus(self):
        self.assertEqual(self.vinkki.vastaus(), "Hello Hello!")

    def testaa_huomenta(self):
        self.assertEqual(self.vinkki.huomenta(), "Good Morning, Rise'n Shine Today!")

