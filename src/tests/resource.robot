*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0 seconds
${HOME URL}  http://${SERVER}
${LOGIN URL}  http://${SERVER}/kirjautuminen
${REGISTER URL}  http://${SERVER}/rekisterointi

*** Keywords ***
Open And Configure Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window
    Set Selenium Speed  ${DELAY}

Main Page Should Be Open
    Title Should Be  Lukuvinkit

Go To Main Page
    Go To  ${HOME URL}

Go To Register Page 
    Go To  ${REGISTER URL}

Register Page Should Be Open
    Title Should Be  Rekisteröinti