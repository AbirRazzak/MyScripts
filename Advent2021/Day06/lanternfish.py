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
