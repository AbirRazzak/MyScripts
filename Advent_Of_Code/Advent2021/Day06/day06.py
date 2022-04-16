from Day06 import PUZZLE_INPUT
from Day06.lanternfish import (
    Lanternfish,
    LanternfishSchoolManager,
    LanternfishSchoolSizeForecaster
)


def part1(verbose=False):
    school_manager = LanternfishSchoolManager()

    for number_as_string in PUZZLE_INPUT.split(','):
        number = int(number_as_string)
        new_fish = Lanternfish(reproduction_timer=number)
        school_manager.school.append(new_fish)

    print(school_manager.current_state_as_string()) if verbose else 0

    for i in range(80):
        school_manager.increment_day()
        print(school_manager.current_state_as_string()) if verbose else 0

    print(f'Number of lanternfish after 80 days: {len(school_manager.school)}')


def part2(
    days_to_simulate=256
):
    # The original solution to part 1 is too inefficient to handle simulating 256 days out.
    # Instead of simulating the days, we instead use math to forecast how many fish there will be instead.

    numbers_as_string = PUZZLE_INPUT.split(',')
    numbers_as_int = [int(n) for n in numbers_as_string]
    f = LanternfishSchoolSizeForecaster(starting_fish=numbers_as_int)

    number_of_fish_at_256_days = f.forecast_school_size(days=days_to_simulate)

    print(f'Number of lanternfish after {days_to_simulate} days: {number_of_fish_at_256_days}')


if __name__ == '__main__':
    part1()
    part2(80)  # This should have the same output as part 1.
    part2()
