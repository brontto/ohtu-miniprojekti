from db import db
from app import app

app.app_context().push()

def luo_taulut():
    db.session.execute("""
        CREATE TABLE kayttajat (
            id SERIAL PRIMARY KEY,
            tunnus TEXT UNIQUE,
            salasana TEXT
        );

        CREATE TABLE lukuvinkit (
            id SERIAL PRIMARY KEY,
            otsikko TEXT,
            linkki TEXT,
            kayttaja_id INTEGER REFERENCES kayttajat
        );
    """)
    db.session.commit()

def poista_taulut():
    db.session.execute("""
        DROP TABLE IF EXISTS kayttajat CASCADE;
        DROP TABLE IF EXISTS lukuvinkit CASCADE;
        """)
    db.session.commit()

def alusta_tietokanta():
    poista_taulut()
    luo_taulut()

def lisaa_kayttaja():
    db.session.execute("""
        INSERT INTO kayttajat (tunnus, salasana) VALUES ('testikeiju', 'testi123')
        """)
    db.session.commit()

if __name__ == "__main__":
    alusta_tietokanta()
