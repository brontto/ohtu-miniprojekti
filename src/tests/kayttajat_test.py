
import unittest
from unittest.mock import MagicMock
from datetime import datetime
from kayttajat import Kayttajat

class Row(object):
    def __init__(self, x):
        self.query_id = x


class testKayttajat(unittest.TestCase):

    def setUp(self):
        dbc = MagicMock(name="dbconn")
        cursor = MagicMock(name="cursor")
        cursor.fetchall.return_value = [Row(1), Row(2)]
        dbc.cursor.return_value = cursor
        self.test_class = Kayttajat(dbc)

    def test_voi_lisata_uuden_kayttajan(self):
        result = self.test_class.lisaa_uusi_kayttaja("maija", "kala")

        self.assertTrue(result)

    def test_olemassa_oleva_tunnus_loytyy_tietokannasta(self):
        self.test_class.lisaa_uusi_kayttaja("maija", "kala")
        onko_olemassa = self.test_class.tarkasta_kayttajatunnus("maija")
        self.assertTrue(onko_olemassa)
