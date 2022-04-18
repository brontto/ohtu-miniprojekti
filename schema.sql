DROP TABLE IF EXISTS kayttajat CASCADE;
DROP TABLE IF EXISTS lukuvinkit CASCADE;

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
    ON DELETE CASCADE
);