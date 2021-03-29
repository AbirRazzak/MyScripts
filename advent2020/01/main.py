from typing import List, Tuple


def convert_file_to_list(
        filename: str
) -> List[int]:
    file = open(filename, 'r')
    values = []
    for line in file:
        values.append(int(line))
    return values


def find_two_numbers_that_add_up_to_2020(
        numbers_list: List[int]
) -> Tuple[int, int]:
    for first_number in numbers_list:
        for second_number in numbers_list:
            if first_number + second_number == 2020:
                return first_number, second_number


def find_three_numbers_that_add_up_to_2020(
        numbers_list: List[int]
) -> Tuple[int, int, int]:
    for first_number in numbers_list:
        for second_number in numbers_list:
            for third_number in numbers_list:
                if first_number + second_number + third_number == 2020:
                    return first_number, second_number, third_number


if __name__ == '__main__':
    # read in the input
    numbers = convert_file_to_list('input.txt')

    # find two numbers that add up to 2020
    # num1, num2 = find_two_numbers_that_add_up_to_2020(numbers)
    num1, num2, num3 = find_three_numbers_that_add_up_to_2020(numbers)
    print(f'{num1} {num2} {num3}')

    # multiply those two numbers -> output
    # print(f'{num1 * num2}')
    print(f'{num1 * num2 * num3}')
