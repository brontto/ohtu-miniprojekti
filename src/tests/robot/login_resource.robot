*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  kayttajatunnus  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  salasana  ${password}

Submit Credentials
    Click Button  Kirjaudu

Login Should Succeed
    Lukuvinkit Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Main Page Should Be Open
    Page Should Contain  ${message}

Add New Should Be Available
    Page Should Contain Button  Luo uusi lukuvinkki

Add New Should Not Be Available
    Page Should Not Contain  Luo uusi lukuvinkki