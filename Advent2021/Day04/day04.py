from typing import List

from Day04 import (
    BOARDS_INPUT,
    CALL_NUMBERS_INPUT
)
from Day04.bingo import (
    BingoBoardGenerator,
    BingoBoard
)


def part1(
    calls: List[int],
    boards: List[BingoBoard]
) -> None:
    for call in calls:
        print(f'\nCalling {call:2} on all boards... ', end='')
        for board in boards:
            board.mark_number(call)
            is_bingo = board.calculate_win()

            if is_bingo:
                print('Bingo!')
                unmarked_numbers_sum = board.get_sum_of_all_unmarked_numbers()
                print(f'Part 1 Answer: {unmarked_numbers_sum} * {call} = {unmarked_numbers_sum * call}')
                return


def part2(
    calls: List[int],
    boards: List[BingoBoard]
):
    winning_boards: List[BingoBoard] = []
    last_bingo_call: int = 0

    for call in calls:
        print(f'\nCalling {call:2} on all boards... ', end='')
        boards_to_remove: List[BingoBoard] = []

        for board in boards:
            board.mark_number(call)
            is_bingo = board.calculate_win()

            if is_bingo:
                print('Bingo! ', end='')
                winning_boards.append(board)
                last_bingo_call = call
                boards_to_remove.append(board)

        if boards_to_remove:
            for board in boards_to_remove:
                boards.remove(board)

    last_winning_board = winning_boards[len(winning_boards) - 1]
    unmarked_numbers_sum = last_winning_board.get_sum_of_all_unmarked_numbers()
    print(f'\nPart 2 Answer: {unmarked_numbers_sum} * {last_bingo_call} = {unmarked_numbers_sum * last_bingo_call}')


if __name__ == '__main__':
    calls_str: List[str] = CALL_NUMBERS_INPUT.split(',')
    _calls: List[int] = [int(call_str) for call_str in calls_str]

    print('Running part 1')
    boards1 = BingoBoardGenerator.parse_string_into_boards(BOARDS_INPUT)
    part1(_calls, boards1)

    print('\nRunning part 2')
    boards2 = BingoBoardGenerator.parse_string_into_boards(BOARDS_INPUT)
    part2(_calls, boards2)
