import functools
from typing import List

from pydantic import BaseModel


class Lanternfish(BaseModel):
    reproduction_timer: int = 8

    def increment_day(self) -> None:
        if self.reproduction_timer == 0:
            self.reproduction_timer = 6
        else:
            self.reproduction_timer -= 1


class LanternfishSchoolManager(BaseModel):
    school: List[Lanternfish] = []
    day_number: int = 0

    def increment_day(self):
        new_fish_to_add: List[Lanternfish] = []
        for fish in self.school:
            if fish.reproduction_timer == 0:
                new_fish = Lanternfish()
                new_fish_to_add.append(new_fish)
            fish.increment_day()

        self.school.extend(new_fish_to_add)
        self.day_number += 1

    def current_state_as_string(self, verbose=False) -> str:
        if self.day_number == 0:
            output = f'Initial state: '
        else:
            output = f'After {self.day_number:2} day'
            if self.day_number == 1:
                output += ': '
            else:
                output += 's: '

        if verbose:
            timers = [str(fish.reproduction_timer) for fish in self.school]
            timers_formatted = ','.join(timers)
            output += timers_formatted

        return output


class LanternfishSchoolSizeForecaster:
    initial_fish: List[int]

    def __init__(
        self,
        starting_fish: List[int]
    ):
        self.initial_fish = starting_fish

    @functools.cache
    def _forecast_total_offspring_from_fish(self, fish: int, days: int):
        if fish < days:
            extra_offspring = int(((days - fish - 1) / 7))
            offspring = 1 + extra_offspring
            for i in range(extra_offspring):
                offspring += self._forecast_total_offspring_from_fish(8, ((days - fish - 1) - (7 * i)))
            return offspring
        return 0

    def forecast_school_size(self, days: int):
        count = len(self.initial_fish)
        for fish in self.initial_fish:
            count += self._forecast_total_offspring_from_fish(fish=fish, days=days)
        return count
