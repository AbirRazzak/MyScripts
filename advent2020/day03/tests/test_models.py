from advent2020.day03.models import Forest, ForestElement


def test_forest_convert_from_text_to_object():
    string_rep = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""
    forest = Forest()

    forest.convert_text_to_object(string_rep)

    assert forest.grid[0][0] == ForestElement.EMPTY
    assert forest.grid[0][2] == ForestElement.TREE
    assert forest.grid[1][0] == ForestElement.TREE
    assert forest.grid[3][1] == ForestElement.EMPTY
