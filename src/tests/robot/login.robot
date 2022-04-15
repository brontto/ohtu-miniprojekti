*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Main Page

*** Test Cases ***
Login With Correct Credentials
    Set Username  keiju
    Set Password  keijusana
    Submit Credentials
    Login Should Succeed

Login With Incorrect Username
    Set Username  keijo
    Set Password  keijon_salasana
    Submit Credentials
    Login Should Fail With Message  Käyttäjätunnus tai salasana väärin

Login With Incorrect Password
    Set Username  keiju
    Set Password  keijun_salasana
    Submit Credentials
    Login Should Fail With Message  Käyttäjätunnus tai salasana väärin

Logged Out User Cannot Add A Lukuvinkki
    Go To Lukuvinkit Page
    Add New Should Not Be Available

Logged In User Can Add A Lukuvinkki
    Set Username  keiju
    Set Password  keijusana
    Submit Credentials
    Add New Should Be Available


*** Keywords ***
Create User And Go To Main Page
    Reset Application
    Logout
    Create User  keiju  keijusana
    Go To Main Page
    Main Page Should Be Open

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
    Page Should Contain  Luo uusi lukuvinkki

Add New Should Not Be Available
    Page Should Not Contain  Luo uusi lukuvinkki

    