import requests

from client import models


class AuthClient:
    # TODO: parametrize host
    TOKEN_ROUTE = "http://localhost:8000/auth/token/"

    def token(self, username, passsword):
        # TODO: Error handling
        body = {
            "username": username,
            "password": passsword,
        }
        response = requests.post(AuthClient.TOKEN_ROUTE, data=body)
        return models.Token(**response.json())
