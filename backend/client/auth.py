import requests


class AuthClient:
    TOKEN_ROUTE = "http://localhost:8000/auth/token"

    def token(self, username, passsword):
        # TODO: Error handling
        body = {
            "username": username,
            "password": passsword,
        }
        response = requests.post(AuthClient.TOKEN_ROUTE, data=body)
        return response.json()
