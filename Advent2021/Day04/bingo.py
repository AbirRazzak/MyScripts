from typing import List

from pydantic import BaseModel


class BingoBoardNumber(BaseModel):
    value: int
    marked: bool = False


class BingoBoard(BaseModel):
    board: List[List[BingoBoardNumber]]

    def get_sum_of_all_unmarked_numbers(self) -> int:
        sum_of_unmarked_numbers = 0

        for row in self.board:
            for number in row:
                if not number.marked:
                    sum_of_unmarked_numbers += number.value

        return sum_of_unmarked_numbers

    def mark_number(
        self,
        number_to_mark: int
    ) -> bool:
        is_number_marked = False  # Returns True or False if it marks a number

        for row in self.board:
            for number in row:
                if number.value == number_to_mark:
                    number.marked = True
                    is_number_marked = True

        return is_number_marked

    def calculate_win(self) -> bool:
        return self._calculate_horizontal_win() or self._calculate_vertical_win()

    def _calculate_horizontal_win(self) -> bool:
        for row in self.board:
            row_marks = [number.marked for number in row]
            if False not in row_marks:
                return True

        return False

    def _calculate_vertical_win(self) -> bool:
        for i in range(len(self.board[0])):
            column = [row[i] for row in self.board]
            column_marks = [number.marked for number in column]
            if False not in column_marks:
                return True
        return False


class BingoBoardGenerator:
    @staticmethod
    def parse_string_into_board(
        board_input: str
    ) -> BingoBoard:
        board: List[List[BingoBoardNumber]] = []

        board_rows_str: List[str] = board_input.split('\n')

        for row_str in board_rows_str:
            row: List[BingoBoardNumber] = []

            numbers_str: List[str] = row_str.split()

            for number_str in numbers_str:
                number_int = int(number_str)
                number = BingoBoardNumber(value=number_int)
                row.append(number)

            board.append(row)

        bingo_board = BingoBoard(board=board)
        return bingo_board

    @staticmethod
    def parse_string_into_boards(
        boards_input: str
    ) -> List[BingoBoard]:
        boards: List[BingoBoard] = []

        boards_str: List[str] = boards_input.split('\n\n')

        for board_str in boards_str:
            board = BingoBoardGenerator.parse_string_into_board(board_str)
            boards.append(board)

        return boards
