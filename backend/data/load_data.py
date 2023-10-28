import numpy as np
import pandas as pd
import typer

from data import inorganic, stars

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
    resource_data = inorganic.extract(filename)
    resource_data = inorganic.transform(resource_data)
    inorganic.load(resource_data, username, password)


@app.command()
def load_stars(filename: str, username: str, password: str):
    data = stars.extract(filename)
    data = stars.transform(data)
    stars.load(data, username, password)


if __name__ == "__main__":
    app()
