from Day05.hydrothermal_vents import HydrothermalVents

EXAMPLE_INPUT = '''0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2'''


def test():
    vents = HydrothermalVents(vent_lines=[])
    vents.parse_vent_lines(EXAMPLE_INPUT)
    vents.process_lines()

    result = vents.get_number_of_dangerous_coordinates(2)

    assert result == 5

