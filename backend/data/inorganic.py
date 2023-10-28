import pandas as pd
from pydantic import ValidationError

from client import models
from client.auth import AuthClient
from client.starfield_resources import ApiClient


def extract(filename):
    return pd.read_csv(filename)


def transform(data):
    data.columns = data.columns.str.lower()
    data = data[["resource", "description", "rarity"]]
    data = data.rename(columns={"description": "name", "resource": "abbreviation"})
    return data


def load(resource_data, username, password):
    try:
        token = AuthClient().token(username, password)
        client = ApiClient(token)
        for resource in resource_data.to_dict("records")[1:]:
            try:
                resource["rarity"] = models.Rarity[resource["rarity"].upper()]
                model = models.Resource(**resource)
                response = client.post_resource(model)
                # TODO should post_resource() do this check and throw an
                #  exception instead?
                if response.status_code != 201:
                    print(model)
                    print(response.json())
            except ValidationError as err:
                print(f"Unable to insert: {resource}")
                print(err.json())
    except ValidationError as err:
        print(err.json())
