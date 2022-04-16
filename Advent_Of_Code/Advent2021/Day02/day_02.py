from Day02 import PUZZLE_INPUT
from Day02.submarine import (
    SubmarineInstruction,
    SubmarinePart1,
    Submarine,
    SubmarinePart2
)


def run_puzzle(
    _submarine: Submarine
):
    for line in PUZZLE_INPUT.split('\n'):
        instruction = SubmarineInstruction(instruction=line)
        command = instruction.to_command()
        _submarine.execute(command=command)


if __name__ == '__main__':
    print('Running part 1 simulation...')
    submarine1 = SubmarinePart1()
    run_puzzle(submarine1)
    answer1 = submarine1.horizontal_position * submarine1.depth

    print('Running part 2 simulation...')
    submarine2 = SubmarinePart2()
    run_puzzle(submarine2)
    answer2 = submarine2.horizontal_position * submarine2.depth

    print(f'Results:\n-----')
    print(f'Part 1 Answer: {submarine1.horizontal_position} * {submarine1.depth} = {answer1}')
    print(f'Part 2 Answer: {submarine2.horizontal_position} * {submarine2.depth} = {answer2}')
