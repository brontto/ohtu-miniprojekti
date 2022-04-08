from db import db

class KayttajaRepository:
    def __init__(self):
        pass

    def lisaa_uusi_kayttaja(self, kayttaja):
        pass

    # def tarkasta_sisaankirjautuminen(self, tunnus):
    #     sql = "SELECT id, salasana FROM kayttajat WHERE tunnus=:tunnus"
    #     result = db.session.execute(sql, {"tunnus":tunnus})
    #     return result.fetchone()

    # def hae_kayttajan_id(self, tunnus):
    #     sql = "SELECT id FROM kayttajat WHERE tunnus=:tunnus"
    #     result = db.session.execute(sql, {"tunnus":tunnus})
    #     kayttajan_id = result.fetchone().id
    #     return kayttajan_id 