from Day05 import PUZZLE_INPUT
from Day05.hydrothermal_vents import (
    HydrothermalVents
)

if __name__ == '__main__':
    # Part 1
    vents = HydrothermalVents(vent_lines=[])
    vents.parse_vent_lines(PUZZLE_INPUT)
    vents.process_lines(part_number=1)
    print(vents.get_number_of_dangerous_coordinates(2))

    # Part 2
    vents = HydrothermalVents(vent_lines=[])
    vents.parse_vent_lines(PUZZLE_INPUT)
    vents.process_lines(part_number=2)
    print(vents.get_number_of_dangerous_coordinates(2))
