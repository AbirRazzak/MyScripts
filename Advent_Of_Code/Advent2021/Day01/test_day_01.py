from Day01.day_01 import (
    calculate_num_increases,
    generate_sliding_window_sums
)


def test_calculate_num_increases():
    nums_increasing = ['0', '1', '2', '3', '4', '5']
    expected_result = 5

    result = calculate_num_increases(list_of_nums_as_strings=nums_increasing)

    assert result == expected_result


def test_calculate_num_increases_with_some_decreases():
    nums_increasing = ['0', '1', '2', '0', '2', '1']
    expected_result = 3

    result = calculate_num_increases(list_of_nums_as_strings=nums_increasing)

    assert result == expected_result


def test_generate_sliding_window_sums():
    nums_increasing = ['0', '1', '2', '3', '4', '5']
    expected_window_sums = ['3', '6', '9', '12']

    result = generate_sliding_window_sums(list_of_nums_as_strings=nums_increasing)

    assert result == expected_window_sums
