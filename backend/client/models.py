from enum import Enum, auto

from pydantic import BaseModel


class Rarity(Enum):
    COMMON = 0
    UNCOMMON = 1
    RARE = 2
    EXOTIC = 3
    UNIQUE = 4


class Resource(BaseModel):
    name: str
    abbreviation: str
    rarity: Rarity


class Star(BaseModel):
    name: str
    level: int


class Planet(BaseModel):
    name: str
    star: Star
    extreme_environment: bool
    resources: list[Resource]


class Moon(BaseModel):
    name: str
    planet: Planet
    extreme_environment: bool
    resources: list[Resource]
