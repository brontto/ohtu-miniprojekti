import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5000"

        self.reset_application()

    def create_user(self, username, password):
        data = {
            "kauttajatunnus": username,
            "salasana": password,
            "salasana_varmistus": password
        }

        requests.post(f"{self._base_url}/rekisterointi", data=data)
