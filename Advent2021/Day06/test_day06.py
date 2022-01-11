from Day06 import PUZZLE_INPUT
from Day06.lanternfish import (
    LanternfishSchoolManager,
    Lanternfish
)


def test_part1():
    school_manager = LanternfishSchoolManager()

    for number_as_string in PUZZLE_INPUT.split(','):
        number = int(number_as_string)
        new_fish = Lanternfish(reproduction_timer=number)
        school_manager.school.append(new_fish)

    print(school_manager.current_state_as_string())

    for i in range(80):
        school_manager.increment_day()
        print(school_manager.current_state_as_string())

    assert len(school_manager.school) == 359344
    assert school_manager.day_number == 80
