
import unittest
from unittest.mock import MagicMock
from kayttajat import Kayttajat



class TestKayttajat(unittest.TestCase):

    def setUp(self):
        dbc = MagicMock(name="dbconn")
        cursor = MagicMock(name="cursor")
        dbc.cursor.return_value = cursor
        self.test_class = Kayttajat(dbc)

    def test_voi_lisata_uuden_kayttajan(self):
        result = self.test_class.lisaa_uusi_kayttaja("maija", "kala")
        self.assertTrue(result)

    def test_olemassa_oleva_tunnus_loytyy_tietokannasta(self):
        self.test_class.lisaa_uusi_kayttaja("maija", "kala")
        onko_olemassa = self.test_class.tarkasta_kayttajatunnus("maija")
        self.assertTrue(onko_olemassa)
