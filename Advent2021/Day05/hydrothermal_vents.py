from typing import List

from pydantic import BaseModel


class Coordinate(BaseModel):
    x: int
    y: int
    counter: int = 0

    def __eq__(self, other):
        is_x_same = self.x == other.x
        is_y_same = self.y == other.y

        return is_x_same and is_y_same


class VentLine(BaseModel):
    start: Coordinate
    end: Coordinate

    def calculate_line_segment(self) -> List[Coordinate]:
        coordinates = [self.start]

        if self.start.x == self.end.x:
            # horizontal
            y_counter = self.start.y
            incremental = 1 if self.start.y < self.end.y else -1

            while y_counter != self.end.y:
                y_counter += incremental
                coordinate_in_line = Coordinate(x=self.start.x, y=y_counter)
                coordinates.append(coordinate_in_line)

        elif self.start.y == self.end.y:
            # vertical
            x_counter = self.start.x
            incremental = 1 if self.start.x < self.end.x else -1

            while x_counter != self.end.x:
                x_counter += incremental
                coordinate_in_line = Coordinate(x=x_counter, y=self.start.y)
                coordinates.append(coordinate_in_line)

        return coordinates


class HydrothermalVents(BaseModel):
    vent_lines: List[VentLine]
    board: List[Coordinate] = []

    def increment_coordinate_count(
        self,
        coordinate_to_increment: Coordinate
    ):
        for board_coordinate in self.board:
            if board_coordinate == coordinate_to_increment:
                board_coordinate.counter += 1
                return

        new_coordinate = Coordinate(
            x=coordinate_to_increment.x,
            y=coordinate_to_increment.y
        )
        self.board.append(new_coordinate)

    def process_lines(
        self
    ):
        for line in self.vent_lines:
            coordinates_to_record = line.calculate_line_segment()

            for coordinate_to_record in coordinates_to_record:
                self.increment_coordinate_count(coordinate_to_record)

    def get_number_of_dangerous_coordinates(
        self,
        danger_level: int
    ) -> int:
        counter = 0

        for board_coordinate in self.board:
            if board_coordinate.counter >= danger_level:
                counter += 1

        return counter
