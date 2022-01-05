from typing import List

from Day04.bingo import (
    BingoBoardGenerator,
    BingoBoard,
    BingoBoardNumber
)


def test_parse_string_into_board():
    board_str = '''67 97
47 15'''

    expected = BingoBoard(
        board=[
            [
                BingoBoardNumber(value=67),
                BingoBoardNumber(value=97)
            ],
            [
                BingoBoardNumber(value=47),
                BingoBoardNumber(value=15)
            ]
        ]
    )

    result: BingoBoard = BingoBoardGenerator.parse_string_into_board(board_str)

    assert result == expected


def test_parse_string_into_boards():
    boards_str = '''67 97
47 15

44 11
66  7'''

    expected = [
        BingoBoard(
            board=[
                [
                    BingoBoardNumber(value=67),
                    BingoBoardNumber(value=97)
                ],
                [
                    BingoBoardNumber(value=47),
                    BingoBoardNumber(value=15)
                ]
            ]
        ),
        BingoBoard(
            board=[
                [
                    BingoBoardNumber(value=44),
                    BingoBoardNumber(value=11)
                ],
                [
                    BingoBoardNumber(value=66),
                    BingoBoardNumber(value=7)
                ]
            ]
        )
    ]

    result: List[BingoBoard] = BingoBoardGenerator.parse_string_into_boards(boards_str)

    assert result == expected


def test_get_sum_of_all_unmarked_numbers():
    bingo_board = BingoBoard(
        board=[
            [
                BingoBoardNumber(value=67),
                BingoBoardNumber(value=97)
            ],
            [
                BingoBoardNumber(value=47),
                BingoBoardNumber(value=15, marked=True)
            ]
        ]
    )

    expected = 67 + 97 + 47

    result = bingo_board.get_sum_of_all_unmarked_numbers()

    assert result == expected


def test_mark_number():
    bingo_board = BingoBoard(
        board=[
            [
                BingoBoardNumber(value=67),
                BingoBoardNumber(value=97)
            ],
            [
                BingoBoardNumber(value=47),
                BingoBoardNumber(value=15)
            ]
        ]
    )

    expected_board = BingoBoard(
        board=[
            [
                BingoBoardNumber(value=67),
                BingoBoardNumber(value=97)
            ],
            [
                BingoBoardNumber(value=47),
                BingoBoardNumber(value=15, marked=True)
            ]
        ]
    )

    bingo_board.mark_number(15)

    assert bingo_board == expected_board


def test_calculate_horizontal_win_returns_true():
    bingo_board = BingoBoard(
        board=[
            [
                BingoBoardNumber(value=67, marked=True),
                BingoBoardNumber(value=97, marked=True)
            ],
            [
                BingoBoardNumber(value=47),
                BingoBoardNumber(value=15)
            ]
        ]
    )

    result = bingo_board._calculate_horizontal_win()

    assert result is True


def test_calculate_horizontal_win_returns_false():
    bingo_board = BingoBoard(
        board=[
            [
                BingoBoardNumber(value=67, marked=True),
                BingoBoardNumber(value=97)
            ],
            [
                BingoBoardNumber(value=47, marked=True),
                BingoBoardNumber(value=15)
            ]
        ]
    )

    result = bingo_board._calculate_horizontal_win()

    assert result is False


def test_calculate_vertical_win_returns_true():
    bingo_board = BingoBoard(
        board=[
            [
                BingoBoardNumber(value=67, marked=True),
                BingoBoardNumber(value=97)
            ],
            [
                BingoBoardNumber(value=47, marked=True),
                BingoBoardNumber(value=15)
            ]
        ]
    )

    result = bingo_board._calculate_vertical_win()

    assert result is True


def test_calculate_vertical_win_returns_false():
    bingo_board = BingoBoard(
        board=[
            [
                BingoBoardNumber(value=67, marked=True),
                BingoBoardNumber(value=97, marked=True)
            ],
            [
                BingoBoardNumber(value=47),
                BingoBoardNumber(value=15)
            ]
        ]
    )

    result = bingo_board._calculate_vertical_win()

    assert result is False
