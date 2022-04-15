import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"

        self.reset_application()

    def create_user(self, username, password):
        data = {
            "kayttajatunnus": username,
            "salasana": password,
            "salasana_varmistus": password
        }

        requests.post(f"{self._base_url}/luo_uusi_kayttaja", data=data)

    def reset_application(self):
        requests.get(f"{self._base_url}/tyhjenna_tietokannat")
