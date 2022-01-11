from Day06 import PUZZLE_INPUT
from Day06.lanternfish import (
    Lanternfish,
    LanternfishSchoolManager
)

if __name__ == '__main__':
    school_manager = LanternfishSchoolManager()

    for number_as_string in PUZZLE_INPUT.split(','):
        number = int(number_as_string)
        new_fish = Lanternfish(reproduction_timer=number)
        school_manager.school.append(new_fish)

    print(school_manager.current_state_as_string())

    for i in range(80):
        school_manager.increment_day()
        print(school_manager.current_state_as_string())

    print(f'Number of lanternfish after 80 days: {len(school_manager.school)}')
