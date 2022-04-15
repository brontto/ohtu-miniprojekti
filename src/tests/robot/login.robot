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
    Logout

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

*** Keywords ***
Create User And Go To Main Page
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

    