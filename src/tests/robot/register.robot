*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Reset Application

*** Test Cases ***
Register With Correct Credentials
    Go To Register Page
    Set Username  keiju
    Set Password And Confrimation  keijusana
    Submit Credentials
    Register Should Succeed
    Page Should Contain  keiju

Register With Incorrect Credentials
    Go To Register Page 
    Set Username  keiju
    Submit Credentials
    Page Should Contain  Error: Tarvitset myös salasanan

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  kayttajatunnus  ${username}

Set Password And Confrimation
    [Arguments]  ${password}
    Input Text  salasana  ${password}
    Input Text  salasana_varmistus  ${password}

Submit Credentials
    Click Button  Rekisteröidy

Register Should Succeed
    Lukuvinkit Page Should Be Open