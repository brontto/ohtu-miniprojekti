*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
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

Logout From App
    Set Username  keiju
    Set Password  keijusana
    Submit Credentials
    Click Link  Kirjaudu ulos
    Page Should Contain  Rekisteröidy täällä





    