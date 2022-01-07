from typing import (
    List,
    Dict
)

from pydantic import BaseModel


class Coordinate(BaseModel):
    x: int
    y: int
    counter: int = 0

    def __eq__(self, other):
        is_x_same = self.x == other.x
        is_y_same = self.y == other.y

        return is_x_same and is_y_same

    def __str__(self):
        return f'{self.x},{self.y}'


class VentLine(BaseModel):
    start: Coordinate
    end: Coordinate

    def _get_horizontal_line_segment_coordinates(self) -> List[Coordinate]:
        coordinates = [self.start]

        y_counter = self.start.y
        incremental = 1 if self.start.y < self.end.y else -1

        while y_counter != self.end.y:
            y_counter += incremental
            coordinate_in_line = Coordinate(x=self.start.x, y=y_counter)
            coordinates.append(coordinate_in_line)

        return coordinates

    def _get_vertical_line_segment_coordinates(self) -> List[Coordinate]:
        coordinates = [self.start]

        x_counter = self.start.x
        incremental = 1 if self.start.x < self.end.x else -1

        while x_counter != self.end.x:
            x_counter += incremental
            coordinate_in_line = Coordinate(x=x_counter, y=self.start.y)
            coordinates.append(coordinate_in_line)

        return coordinates

    def _get_diagonal_line_segment_coordinates(self) -> List[Coordinate]:
        coordinates = [self.start]

        x_counter = self.start.x
        y_counter = self.start.y

        x_incremental = 1 if self.start.x < self.end.x else -1
        y_incremental = 1 if self.start.y < self.end.y else -1

        while (
            x_counter != self.end.x and
            y_counter != self.end.y
        ):
            x_counter += x_incremental
            y_counter += y_incremental
            coordinate_in_line = Coordinate(x=x_counter, y=y_counter)
            coordinates.append(coordinate_in_line)

        return coordinates

    def calculate_line_segment(
        self,
        part_number: int
    ) -> List[Coordinate]:
        if self.start.x == self.end.x:
            horizontal_coordinates = self._get_horizontal_line_segment_coordinates()
            return horizontal_coordinates

        if self.start.y == self.end.y:
            vertical_coordinates = self._get_vertical_line_segment_coordinates()
            return vertical_coordinates

        # Comment this out for part 1:
        if part_number == 2:
            if abs(self.start.x - self.end.x) == abs(self.start.y - self.end.y):
                diagonal_coordinates = self._get_diagonal_line_segment_coordinates()
                return diagonal_coordinates

        return []

    def __str__(self):
        return f'{self.start} -> {self.end}'


class HydrothermalVents(BaseModel):
    vent_lines: List[VentLine]
    board: Dict[str, Coordinate] = {}

    def parse_vent_lines(self, vent_lines_as_str: str) -> None:
        coordinate_pairs_as_string = vent_lines_as_str.split('\n')
        for coordinate_pair_as_string in coordinate_pairs_as_string:
            coordinates_as_string = coordinate_pair_as_string.split(' -> ')

            start_coordinate_as_string = coordinates_as_string[0]
            start_x = int(start_coordinate_as_string.split(',')[0])
            start_y = int(start_coordinate_as_string.split(',')[1])
            start_coordinate = Coordinate(x=start_x, y=start_y)

            end_coordinate_as_string = coordinates_as_string[1]
            end_x = int(end_coordinate_as_string.split(',')[0])
            end_y = int(end_coordinate_as_string.split(',')[1])
            end_coordinate = Coordinate(x=end_x, y=end_y)

            vent_line = VentLine(start=start_coordinate, end=end_coordinate)
            self.vent_lines.append(vent_line)

    #
    # *** THIS CODE RUNS TOO SLOWLY. CHANGED BOARD FROM A LIST TO A DICT. ***
    #
    # board: List[Coordinate] = []
    # def increment_coordinate_count(
    #     self,
    #     coordinate_to_increment: Coordinate
    # ):
    #     for board_coordinate in self.board:
    #         if board_coordinate == coordinate_to_increment:
    #             board_coordinate.counter += 1
    #             return
    #
    #     new_coordinate = Coordinate(
    #         x=coordinate_to_increment.x,
    #         y=coordinate_to_increment.y
    #     )
    #     self.board.append(new_coordinate)
    #
    # def get_number_of_dangerous_coordinates(
    #     self,
    #     danger_level: int
    # ) -> int:
    #     counter = 0
    #
    #     for board_coordinate in self.board:
    #         if board_coordinate.counter >= danger_level:
    #             counter += 1
    #
    #     return counter

    def increment_coordinate_count(
        self,
        coordinate_to_increment: Coordinate
    ):
        coordinate_key = str(coordinate_to_increment)

        coordinate_in_board = self.board.get(coordinate_key)
        if coordinate_in_board:
            coordinate_in_board.counter += 1
        else:
            new_coordinate_to_add = Coordinate(
                x=coordinate_to_increment.x,
                y=coordinate_to_increment.y,
                counter=1
            )
            self.board[coordinate_key] = new_coordinate_to_add

    def process_lines(
        self,
        part_number: int,
        verbose: bool = False
    ):
        counter = 0
        for line in self.vent_lines:
            counter += 1
            coordinates_to_record = line.calculate_line_segment(part_number)
            print(f'{counter:3}: Processing {line} -- {[str(c) for c in coordinates_to_record]}') if verbose else 0

            for coordinate_to_record in coordinates_to_record:
                self.increment_coordinate_count(coordinate_to_record)

    def get_number_of_dangerous_coordinates(
        self,
        danger_level: int
    ) -> int:
        counter = 0

        for key in self.board:
            board_coordinate = self.board[key]
            if board_coordinate.counter >= danger_level:
                counter += 1

        return counter
