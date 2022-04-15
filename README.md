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


## Heroku 
[Heroku App](https://damp-dawn-78777.herokuapp.com/)

## Sovelluksen konfigurointi

Luo juurihakemistoon tiedosto *.env* ja kopioi sinne tiedoston [*.env.template*](https://github.com/brontto/ohtu-miniprojekti/blob/main/.env.template) sisältö. Aseta .env-tiedostossa käyttämäsi tietokannan osoite ja salainen avain.

Salaisen avaimen luominen onnistuu esim. Python-tulkissa komennoilla
``` python
import secrets
secrets.token_hex(16)
```

## Tietokannan käyttöönotto

Asenna PostgreSQL

Asenna uudet riippuvuudet 
```
poetry install
```
Luo juurihakemistoon tiedosto *.env* ja lisää sinne rivi
```
DATABASE_URL=postgresql:///database_name
```
missä `database_name` on käyttämäsi tietokannan nimi.

Alusta tietokantataulut komennolla
```
psql < schema.sql
```
## Testaaminen

Testit alustavat tietokannan jokaisella suorituskerralla joten niitä varten on hyvä luoda oma tietokanta. Siirry Postgresql:n komentoriville komennolla `psql` ja suorita siellä komento
```
CREATE DATABASE testitietokanta;
```
Luo projektin juurihakemistoon tiedosto *.env.test* ja lisää sinne rivi
```
DATABASE_URL=postgresql:///database_name
```
missä tietokannan nimi on äsken luomasi testitietokannan nimi.

### Yksikkötestit

Suorita yksikkötestit komennolla
```
poetry run invoke test
```
