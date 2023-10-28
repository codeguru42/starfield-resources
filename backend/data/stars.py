import pandas as pd
from pydantic import ValidationError

from client import models
from client.auth import AuthClient
from client.starfield_resources import ApiClient


def extract(filename):
    return pd.read_csv(filename, skiprows=1)


def transform(data):
    data.columns = data.columns.str.lower()
    stars = data[data.type == "Planet"][["system", "level"]]
    stars = stars.rename(columns={"system": "name"})
    return stars.drop_duplicates()


def load(data, username, password):
    try:
        token = AuthClient().token(username, password)
        client = ApiClient(token)
        for star in data.to_dict("records"):
            model = models.Star(**star)
            response = client.post_star(model)
            if response.status_code != 201:
                print(model)
                print(response.json())
    except ValidationError as err:
        print(err.json())
