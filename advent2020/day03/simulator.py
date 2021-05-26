from advent2020.day03.models import Forest, Toboggan, ForestElement


class TobogganSimulator:
    forest: Forest
    toboggan: Toboggan

    def __init__(
            self,
            forest: Forest,
            toboggan: Toboggan
    ):
        self.forest = forest
        self.toboggan = toboggan

    def traverse_down_slope(self) -> int:
        number_of_trees_encountered = 0
        current_x_coord = 0
        current_y_coord = 0
        max_y_coord = len(self.forest.grid)

        while current_y_coord < max_y_coord:
            if self.check_coordinates_for_trees(
                    current_x_coord,
                    current_y_coord
            ):
                number_of_trees_encountered += 1

            current_x_coord += self.toboggan.velocity.x_velocity
            current_y_coord += self.toboggan.velocity.y_velocity

        return number_of_trees_encountered

    def check_coordinates_for_trees(
            self,
            x_coord: int,
            y_coord: int
    ):
        condensed_x_coord = x_coord % len(self.forest.grid[0])
        return self.forest.grid[y_coord][condensed_x_coord] == ForestElement.TREE
