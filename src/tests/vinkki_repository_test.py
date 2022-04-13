import unittest
from vinkki_repository import vinkkirepositorio
from lukuvinkki import Lukuvinkki

class TestVinkkiRepository(unittest.TestCase):
    def setUp(self):
        vinkkirepositorio.poista_kaikki_vinkit()

    def test_uuden_vinkin_lisaaminen(self):
        vinkkirepositorio.lisaa_uusi_vinkki(Lukuvinkki("Keijo Koo", "http://keijokoo.fi"))
        vinkit = vinkkirepositorio.hae_kaikki_vinkit()

        self.assertEqual(len(vinkit), 1)
        self.assertEqual(vinkit[0].otsikko, "Keijo Koo")

    def test_kaikkien_vinkkien_haku(self):
        vinkkirepositorio.lisaa_uusi_vinkki(Lukuvinkki("Keijo Koo", "http://keijokoo.fi"))
        vinkkirepositorio.lisaa_uusi_vinkki(Lukuvinkki("Keiju", "http://keiju.fi"))
        vinkkirepositorio.lisaa_uusi_vinkki(Lukuvinkki("Fairy", "https://fi.wikipedia.org/wiki/Fairy"))

        vinkit = vinkkirepositorio.hae_kaikki_vinkit()

        self.assertEqual(len(vinkit), 3)
        self.assertEqual(vinkit[2].otsikko, "Fairy")
        
    def test_kaikkien_vinkkien_poisto(self):
        vinkkirepositorio.lisaa_uusi_vinkki(Lukuvinkki("Keijo Koo", "http://keijokoo.fi"))
        vinkkirepositorio.lisaa_uusi_vinkki(Lukuvinkki("Keiju", "http://keiju.fi"))
        vinkkirepositorio.lisaa_uusi_vinkki(Lukuvinkki("Fairy", "https://fi.wikipedia.org/wiki/Fairy"))
        vinkkirepositorio.poista_kaikki_vinkit()

        vinkit = vinkkirepositorio.hae_kaikki_vinkit()

        self.assertEqual(len(vinkit), 0)

    def test_uusimman_vinkin_haku(self):
        vinkkirepositorio.lisaa_uusi_vinkki(Lukuvinkki("Keijo Koo", "http://keijokoo.fi"))
        vinkkirepositorio.lisaa_uusi_vinkki(Lukuvinkki("Keiju", "http://keiju.fi"))
        vinkkirepositorio.lisaa_uusi_vinkki(Lukuvinkki("Fairy", "https://fi.wikipedia.org/wiki/Fairy"))

        vinkki = vinkkirepositorio.hae_uusin_vinkki()

        self.assertEqual(vinkki[0], "Fairy")