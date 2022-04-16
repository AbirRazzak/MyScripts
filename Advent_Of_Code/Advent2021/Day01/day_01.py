from typing import List

from Day01 import PUZZLE_INPUT


def calculate_num_increases(
    list_of_nums_as_strings: List[str]
) -> int:
    counter = 0

    for i in range(1, len(list_of_nums_as_strings)):
        current_number_as_string = list_of_nums_as_strings[i]
        previous_number_as_string = list_of_nums_as_strings[i-1]

        current_number = int(current_number_as_string)
        previous_number = int(previous_number_as_string)

        if current_number > previous_number:
            counter += 1

    return counter


def generate_sliding_window_sums(
    list_of_nums_as_strings: List[str]
) -> List[str]:
    list_of_sums: List[str] = []

    for i in range(2, len(list_of_nums_as_strings)):
        first_number_as_string = list_of_nums_as_strings[i]
        second_number_as_string = list_of_nums_as_strings[i - 1]
        third_number_as_string = list_of_nums_as_strings[i - 2]

        first_number = int(first_number_as_string)
        second_number = int(second_number_as_string)
        third_number = int(third_number_as_string)

        sliding_window_sum = first_number + second_number + third_number
        list_of_sums.append(f'{sliding_window_sum}')

    return list_of_sums


if __name__ == '__main__':
    puzzle_inputs_as_list = PUZZLE_INPUT.split()
    answer1 = calculate_num_increases(puzzle_inputs_as_list)

    sliding_window_sums = generate_sliding_window_sums(puzzle_inputs_as_list)
    answer2 = calculate_num_increases(sliding_window_sums)

    print(f'Answer 1: {answer1}\nAnswer 2: {answer2}')
