import numpy as np
import pandas as pd
import typer
from pydantic import ValidationError

from client import models
from client.auth import AuthClient
from client.starfield_resources import ApiClient

app = typer.Typer()


def get_resources(planet_data):
    resource_cols = [f"Resource {i+1}" for i in range(8)]
    all_resources = pd.concat(
        planet_data[resource_col] for resource_col in resource_cols
    )
    return all_resources[~all_resources.isna()].unique()


def write_resources(resources):
    np.savetxt("resources.csv", resources, delimiter=",", fmt="%s")


@app.command()
def parse_resources(filename: str):
    planet_data = pd.read_csv(filename)
    resources = get_resources(planet_data)
    write_resources(resources)


@app.command()
def load_inorganic(filename: str, username: str, password: str):
    resource_data = _extract_inorganic(filename)
    resource_data = _transform_inorganic(resource_data)
    _load_inorganic(resource_data, username, password)


def _load_inorganic(resource_data, username, password):
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


def _transform_inorganic(resource_data):
    resource_data.columns = map(str.lower, resource_data.columns)
    resource_data = resource_data[["resource", "description", "rarity"]]
    resource_data = resource_data.rename(
        columns={"description": "name", "resource": "abbreviation"}
    )
    return resource_data


def _extract_inorganic(filename):
    return pd.read_csv(filename)


if __name__ == "__main__":
    app()
