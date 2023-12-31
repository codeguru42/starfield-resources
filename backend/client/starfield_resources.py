import requests

from client import models


class ApiClient:
    RESOURCE_ROUTE = "http://localhost:8000/api/resources/"
    STAR_ROUTE = "http://localhost:8000/api/stars/"

    def __init__(self, token: models.Token):
        self.headers = {
            "Authorization": f"Token {token.token}",
            "Content-Type": "application/json",
        }

    def post_resource(self, resource: models.Resource):
        # TODO: Error handling
        body = resource.model_dump_json()
        return requests.post(ApiClient.RESOURCE_ROUTE, headers=self.headers, data=body)

    def post_star(self, star: models.Star):
        body = star.model_dump_json()
        return requests.post(ApiClient.STAR_ROUTE, headers=self.headers, data=body)
