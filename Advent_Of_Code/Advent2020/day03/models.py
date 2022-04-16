from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class ForestElement(str, Enum):
    EMPTY = '.',
    TREE = '#'


class Forest(BaseModel):
    grid: List[List[ForestElement]] = []

    def convert_text_to_object(self, string_representation: str) -> None:
        lines = string_representation.split('\n')
        for line in lines:
            self.grid.append(list(line))


class Velocity(BaseModel):
    x_velocity: int
    y_velocity: int


class Toboggan(BaseModel):
    velocity: Velocity
