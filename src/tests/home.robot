*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page


*** Test Cases ***
Main Page Open
    Main Page Should Be Open

Click Register Link
    Click Button  Rekisteröidy
    Register Page Should Be Open