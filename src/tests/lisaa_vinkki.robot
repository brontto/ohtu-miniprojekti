*** Settings ***
Resource  resource.robot

*** Test Cases ***
Lisaa Vinkki    
    Lisaa Uusi Vinkki  otsikko  linkki
    Uuden Vinkin Otsikko Pitaisi Olla  otsikko
