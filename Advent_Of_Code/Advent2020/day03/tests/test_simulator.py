from Advent_Of_Code.Advent2020.day03.models import Forest, ForestElement, Toboggan, Velocity
from Advent_Of_Code.Advent2020.day03.simulator import TobogganSimulator


def test_simulator_traverse_down_slope():
    grid = [
        [ForestElement.EMPTY, ForestElement.EMPTY, ForestElement.EMPTY, ForestElement.TREE],
        [ForestElement.EMPTY, ForestElement.TREE, ForestElement.EMPTY, ForestElement.TREE],
        [ForestElement.EMPTY, ForestElement.EMPTY, ForestElement.EMPTY, ForestElement.EMPTY],
        [ForestElement.TREE, ForestElement.EMPTY, ForestElement.EMPTY, ForestElement.TREE]
    ]
    forest = Forest(
        grid=grid
    )
    toboggan = Toboggan(
        velocity=Velocity(
            x_velocity=1,
            y_velocity=1
        )
    )
    simulator = TobogganSimulator(
        forest=forest,
        toboggan=toboggan
    )

    result = simulator.traverse_down_slope()

    assert result == 2


def test_simulator_traverse_down_slope_where_map_needs_to_extend():
    grid = [
        [ForestElement.EMPTY, ForestElement.EMPTY],
        [ForestElement.EMPTY, ForestElement.TREE],
        [ForestElement.TREE, ForestElement.EMPTY],
        [ForestElement.TREE, ForestElement.TREE]
    ]
    forest = Forest(
        grid=grid
    )
    toboggan = Toboggan(
        velocity=Velocity(
            x_velocity=1,
            y_velocity=1
        )
    )
    simulator = TobogganSimulator(
        forest=forest,
        toboggan=toboggan
    )

    result = simulator.traverse_down_slope()

    assert result == 3
