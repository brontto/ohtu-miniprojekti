*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Main Page


*** Test Cases ***
Main Page Open
    Main Page Should Be Open

Click Register Link
    Click Link  Rekisteröidy täällä
    Register Page Should Be Open