from Day06 import PUZZLE_INPUT
from Day06.lanternfish import (
    LanternfishSchoolManager,
    Lanternfish,
    LanternfishSchoolSizeForecaster
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


def test_forecast_example():
    f = LanternfishSchoolSizeForecaster(starting_fish=[3, 4, 3, 1, 2])

    r1 = f._forecast_total_offspring_from_fish(3, 13)
    assert r1 == 3

    r2 = f.forecast_school_size(days=18)
    assert r2 == 26


def test_forecast_part1():
    numbers_as_string = PUZZLE_INPUT.split(',')
    numbers_as_int = [int(n) for n in numbers_as_string]
    f = LanternfishSchoolSizeForecaster(starting_fish=numbers_as_int)

    r = f.forecast_school_size(days=80)

    assert r == 359344
