import unittest
from unittest.mock import Mock
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError
from kayttajat import Kayttajat

class TestKayttajat(unittest.TestCase):
    def setUp(self):
        self.mock_repo = Mock()
        self.kayttajat = Kayttajat(self.mock_repo)

    def test_kayttajan_lisaaminen(self):
        result = self.kayttajat.lisaa_uusi_kayttaja("keiju", "salasana")
        self.mock_repo.lisaa_uusi_kayttaja.assert_called()
        self.assertTrue(result)

    def test_kayttajatunnus_olemassa(self):
        self.mock_repo.lisaa_uusi_kayttaja.side_effect = IntegrityError(0,0,0)
        result = self.kayttajat.lisaa_uusi_kayttaja("keiju", "salasana123")
        self.assertFalse(result)

    def test_kayttajan_haku(self):
        self.mock_repo.hae_kayttaja_tunnuksella.return_value = (1, "silja", "salasana_hash")
        result = self.kayttajat.hae_kayttaja("silja")
        self.mock_repo.hae_kayttaja_tunnuksella.assert_called_with("silja")
        self.assertEqual(result[0], 1)

    def test_hae_kaikki(self):
        self.mock_repo.hae_kaikki_kayttajat.return_value = [(1, "silja"), (2, "keiju"), (3, "testikeiju")]
        result = self.kayttajat.hae_kaikki_kayttajat()
        self.mock_repo.hae_kaikki_kayttajat.assert_called()
        self.assertEqual(len(result), 3)

    def test_kirjaudu_olemassa_oleva(self):
        self.mock_repo.hae_kayttaja_tunnuksella.return_value = (1, "keiju", generate_password_hash("keijusana"))
        result = self.kayttajat.kirjaudu_sisaan("keiju", "keijusana")
        self.assertTrue(result)

    def test_kirjaudu_vaara_tunnus(self):
        self.mock_repo.hae_kayttaja_tunnuksella.return_value = None
        result = self.kayttajat.kirjaudu_sisaan("keiju15", "salakeiju")
        self.assertFalse(result)

    def test_kirjaudu_vaara_salasana(self):
        self.mock_repo.hae_kayttaja_tunnuksella.return_value = (1, "silja", generate_password_hash("kissakala"))
        result = self.kayttajat.kirjaudu_sisaan("silja", "kattikala")
        self.assertFalse(result)

        