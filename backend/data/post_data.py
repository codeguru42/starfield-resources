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
def post_resources(filename: str, username: str, password: str):
    token = AuthClient().token(username, password)
    resource_data = pd.read_csv(filename)
    resource_data.columns = map(str.lower, resource_data.columns)
    client = ApiClient(token)
    for resource in resource_data.to_dict("records"):
        try:
            client.post_resource(models.Resource(**resource))
        except ValidationError:
            print(f"Unable to insert: {resource}")


if __name__ == "__main__":
    app()
