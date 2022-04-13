from sqlite3 import InternalError
import unittest
from kayttaja_repository import kayttajarepositorio
from kayttajat import kayttajat
import tests.conftest as conf

class TestKayttajaRepository(unittest.TestCase):

    def setUp(self):
        conf.alusta_tietokanta()    

    def test_voi_lisata_uuden_kayttajan(self):
        kayttajat.lisaa_uusi_kayttaja("kala", "kissa")
        kaikki_kayttajat = kayttajat.hae_kaikki_kayttajat()
        self.assertEqual(len(kaikki_kayttajat), 1)

    def test_olemassa_oleva_tunnus_loytyy_tietokannasta(self):
        kayttajarepositorio.lisaa_uusi_kayttaja("maija", "kala")
        onko_olemassa = kayttajat.tarkasta_kayttajatunnus("maija")
        self.assertTrue(onko_olemassa.tunnus, "maija")

    def test_kayttajan_id_loytyy(self):
        kayttajarepositorio.lisaa_uusi_kayttaja("kala", "kissa")
        id = kayttajarepositorio.hae_kayttajan_id("kala")
        self.assertEqual(id, 1)
    
    def test_kaikki_kayttajat_poistuu(self):
        kayttajarepositorio.lisaa_uusi_kayttaja("keiju", "koira")
        kayttajarepositorio.lisaa_uusi_kayttaja("kala", "kissa")

        kayttajarepositorio.poista_kaikki()
        kayttajat = kayttajarepositorio.hae_kaikki_kayttajat()
        self.assertEqual(len(kayttajat), 0)

