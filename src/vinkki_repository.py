from db import db

class VinkkiRepository:
    def __init__(self):
        pass

    def lisaa_uusi_vinkki(self, vinkki):
        sql = "INSERT INTO lukuvinkit (otsikko, linkki, kayttaja_id) \
            VALUES (:otsikko, :linkki, 1)"

        db.session.execute(sql, {"otsikko": vinkki.get_otsikko(),
            "linkki": vinkki.get_linkki()})
        db.session.commit()

vinkki_repositorio = VinkkiRepository()
