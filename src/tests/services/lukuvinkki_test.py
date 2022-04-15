import unittest
from lukuvinkki import Lukuvinkki

class TestLukuvinkki(unittest.TestCase):
    def setUp(self):
        self.lukuvinkki = Lukuvinkki("Fairy Platinum", "https://fi.wikipedia.org/wiki/Fairy")

    def test_otsikko_oikein(self):
        otsikko = self.lukuvinkki.get_otsikko()
        self.assertEqual(otsikko, "Fairy Platinum")

    def test_merkkijonoesitys_oikein(self):
        mjono = str(self.lukuvinkki)
        self.assertEqual(mjono, "Otsikko: Fairy Platinum \n Url: https://fi.wikipedia.org/wiki/Fairy ")
