import unittest
from vinkkikirjasto import Vinkkikirjasto

class FakeVinkkiRepo:
    def __init__(self):
        self.vinkit = []

    def lisaa_uusi_vinkki(self, vinkki, id):
        self.vinkit.append((vinkki, id))

    def hae_uusin_vinkki(self):
        return self.vinkit[-1]

    def hae_kaikki_vinkit(self):
        return self.vinkit

    def poista_kaikki_vinkit(self):
        self.vinkit.clear()

class TestVinkkikirjasto(unittest.TestCase):
    def setUp(self):
        self.vinkkikirjasto = Vinkkikirjasto(FakeVinkkiRepo())

    def test_konstruktori_luo_tyhjan_kirjaston(self):
        maara = len(self.vinkkikirjasto.hae_kaikki_vinkit())
        self.assertEqual(maara, 0)

    def test_uuden_vinkin_lisaaminen_onnistuu(self):
        self.vinkkikirjasto.lisaa_uusi_vinkki("uusi vinkki!", "lukuvinkki.fi", 1)
        maara = len(self.vinkkikirjasto.hae_kaikki_vinkit())
        self.assertEqual(maara, 1)

    def test_uuden_vinkin_lisaaminen_ei_onnistu_ilman_otsikkoa(self):
        self.vinkkikirjasto.lisaa_uusi_vinkki("", "osoite.fi", 1)
        maara = len(self.vinkkikirjasto.hae_kaikki_vinkit())
        self.assertEqual(maara, 0)

    def test_uuden_vinkin_lisaaminen_ei_onnistu_ilman_osoitetta(self):
        self.vinkkikirjasto.lisaa_uusi_vinkki("otsikko", "", 1)
        maara = len(self.vinkkikirjasto.hae_kaikki_vinkit())
        self.assertEqual(maara, 0)

    def test_uuden_vinkin_lisaaminen_ei_onnistu_jos_url_ei_kelpaa(self):
        self.vinkkikirjasto.lisaa_uusi_vinkki("otsikko1", "www.ur l.fi", 1)
        self.vinkkikirjasto.lisaa_uusi_vinkki("otsikko4", "wwwurlfi", 1)
        maara = len(self.vinkkikirjasto.hae_kaikki_vinkit())
        self.assertEqual(maara, 0)

    def test_uusimman_vinkin_haku(self):
        self.vinkkikirjasto.lisaa_uusi_vinkki("Helinä-keiju", "https://fi.wikipedia.org/wiki/Helinä-keiju", 1)
        self.vinkkikirjasto.lisaa_uusi_vinkki("Keijukainen", "https://fi.wikipedia.org/wiki/Keijukainen", 1)
        self.vinkkikirjasto.lisaa_uusi_vinkki("Keiju tuotteet", "https://www.keiju.fi/tuotteet/", 1)

        uusin = self.vinkkikirjasto.hae_viimeksi_lisatty_vinkki()[0]

        self.assertEqual(uusin.get_otsikko(), "Keiju tuotteet")

    def test_kaikkien_vinkkien_poisto(self):
        self.vinkkikirjasto.lisaa_uusi_vinkki("Helinä-keiju", "https://fi.wikipedia.org/wiki/Helinä-keiju", 1)
        self.vinkkikirjasto.lisaa_uusi_vinkki("Keijukainen", "https://fi.wikipedia.org/wiki/Keijukainen", 1)
        self.vinkkikirjasto.lisaa_uusi_vinkki("Keiju tuotteet", "https://www.keiju.fi/tuotteet/", 1)

        self.vinkkikirjasto.poista_kaikki_vinkit()
        maara = len(self.vinkkikirjasto.hae_kaikki_vinkit())

        self.assertEqual(maara, 0)
