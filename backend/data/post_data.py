import numpy as np
import pandas as pd
import typer

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


if __name__ == "__main__":
    app()
