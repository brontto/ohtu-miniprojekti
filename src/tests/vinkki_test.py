import unittest
from vinkki import Vinkki


class TestMain(unittest.TestCase):
    def setUp(self):
        self.vinkki = Vinkki()
        pass

    def viesti(self):
        self.assertEqual(self.vinkki.viesti(), "Hello Codefairy!")

