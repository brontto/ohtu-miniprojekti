from db import db

class KayttajaRepository:
    def __init__(self):
        pass

    def lisaa_uusi_kayttaja(self, tunnus, salasana):
        sql = "INSERT INTO kayttajat(tunnus, salasana) \
            VALUES (:tunnus, :salasana)"
        try:
            db.session.execute(sql, {"tunnus": tunnus, "salasana": salasana})
            db.session.commit()
            print("Rekisteröityminen onnistui")
        except Exception as virhe:
            print(virhe)
    # def tarkasta_sisaankirjautuminen(self, tunnus):
    #     sql = "SELECT id, salasana FROM kayttajat WHERE tunnus=:tunnus"
    #     result = db.session.execute(sql, {"tunnus":tunnus})
    #     return result.fetchone()

    # def hae_kayttajan_id(self, tunnus):
    #     sql = "SELECT id FROM kayttajat WHERE tunnus=:tunnus"
    #     result = db.session.execute(sql, {"tunnus":tunnus})
    #     kayttajan_id = result.fetchone().id
    #     return kayttajan_id
kayttajarepositorio = KayttajaRepository()
