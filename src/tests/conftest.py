from initialize_database import alusta_tietokanta, lisaa_kayttaja

def pytest_configure():
    alusta_tietokanta()
    lisaa_kayttaja()