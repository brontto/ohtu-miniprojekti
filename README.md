# Lukuvinkkikirjasto

Ohtu-miniprojekti

[![GitHub Actions](https://github.com/brontto/ohtu-miniprojekti/workflows/CI/badge.svg)](https://github.com/brontto/ohtu-miniprojekti/actions)
[![codecov](https://codecov.io/gh/brontto/ohtu-miniprojekti/branch/main/graph/badge.svg?token=DYFHMFXATT)](https://codecov.io/gh/brontto/ohtu-miniprojekti)

## Definition of Done
- Toiminnallisuus on looginen osa ohjelmaa
- Toiminnallisuuden toteutukselle on kattavat yksikkötestit
- Toteutusta on hyväksymistestattu
- Testikattavuus on 80%
- Tuotteen muutokset on viety tuotantoon

[Burndown-käyrä](https://docs.google.com/spreadsheets/d/1m27JJOADbrihQkSxDsu489VpF2iS6y8GJkZCpKXE13c/edit#gid=453705215)

[Product backlog](https://github.com/brontto/ohtu-miniprojekti/projects/1)

[Loppuraportti](https://docs.google.com/document/d/1VwHhSXfaDF7HMjNcPluxqwuz0yLMjX78Z1BK_nNxKtE/edit?usp=sharing)

## Heroku 
[Heroku App](https://damp-dawn-78777.herokuapp.com/)

## Sovelluksen asentaminen

- Asenna PostgreSQL
- Asenna riippuvuudet komennolla `poetry install`
- Luo juurihakemistoon tiedosto *.env* ja kopioi sinne tiedoston [*.env.template*](https://github.com/brontto/ohtu-miniprojekti/blob/main/.env.template) sisältö. Aseta .env-tiedostossa muuttujaan DATABASE_URL käyttämäsi tietokannan osoite ja muuttujaan SECRET_KEY oma salainen avaimesi.

Salaisen avaimen luominen onnistuu esim. Python-tulkissa komennoilla
``` python
import secrets
secrets.token_hex(16)
```
- Alusta tietokanta komennolla `poetry run invoke initialize`
- Käynnistä sovellus komennolla `poetry run invoke start`


## Testaaminen

Testit alustavat tietokannan jokaisella suorituskerralla joten niitä varten on hyvä luoda oma tietokanta. Siirry Postgresql:n komentoriville komennolla `psql` ja suorita siellä komento
```
CREATE DATABASE testitietokanta;
```
Luo projektin juurihakemistoon tiedosto *.env.test* ja kopioi sinne tiedoston [*.env.template*](https://github.com/brontto/ohtu-miniprojekti/blob/main/.env.template) sisältö. Aseta tietokannan osoitteeksi äsken luomasi testitietokannan osoite ja luo myös uusi salainen avain.

### Yksikkötestit

Suorita yksikkötestit komennolla
```
poetry run invoke test
```

### Hyväksymistestit

Hyväksymistesteissä [(src/tests/robot)](https://github.com/brontto/ohtu-miniprojekti/tree/main/src/tests/robot) käytetään Robot Frameworkia.

Käynnistä testien suorittamista varten Flask-palvelin komennolla `poetry run invoke robot-start`. Suorita testit toisessa terminaali-ikkunassa komennolla `poetry run invoke robot-test`.  
