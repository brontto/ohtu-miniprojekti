*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Main Page

*** Test Cases ***
Add New Vinkki
    Login With Correct Credentials
    Go To Lukuvinkit Page
    Set Otsikko  Otsikko
    Set Linkki  www.url.com
    Submit Vinkki
    Page Should Contain  Otsikko
    Page Should Contain  www.url.com

Add New Vinkki Without Linkki
    Login With Correct Credentials
    Go To Lukuvinkit Page
    Set Otsikko  väärä otsikko
    Submit Vinkki
    Page Should Not Contain  väärä otsikko

*** Keywords ***
Set Otsikko
    [Arguments]  ${otsikko}
    Input Text  otsikko  ${otsikko}

Set Linkki
    [Arguments]  ${linkki}
    Input Text  url  ${linkki}

Submit Vinkki
    Click Button  Luo uusi lukuvinkki

*** Keywords ***
Login With Correct Credentials
    Set Username  keiju
    Set Password  keijusana
    Submit Credentials
    

