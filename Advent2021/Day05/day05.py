from typing import List

from Day05 import PUZZLE_INPUT
from Day05.hydrothermal_vents import (
    Coordinate,
    VentLine,
    HydrothermalVents
)

if __name__ == '__main__':
    vents = HydrothermalVents(vent_lines=[])
    vents.parse_vent_lines(PUZZLE_INPUT)
    vents.process_lines()
    print(vents.get_number_of_dangerous_coordinates(2))
