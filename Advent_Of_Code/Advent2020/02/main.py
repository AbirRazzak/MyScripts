from typing import List

from pydantic import BaseModel


class PasswordPolicy(BaseModel):
    target_char: str
    min_occurrences: int
    max_occurrences: int
    password: str

    def is_valid(self) -> bool:
        validator = self.password.split(self.target_char)
        occurrences = len(validator) - 1
        if self.min_occurrences <= occurrences <= self.max_occurrences:
            return True
        else:
            return False


class OTCP(BaseModel):
    target_char: str
    first_index: int
    second_index: int
    password: str

    def is_valid(self) -> bool:
        i = 0

        try:
            if self.password[self.first_index - 1] == self.target_char:
                i += 1
        except IndexError:
            pass

        try:
            if self.password[self.second_index - 1] == self.target_char:
                i += 1
        except IndexError:
            pass

        return i == 1


def convert_file_to_list(
        filename: str,
        target_object: str
) -> List[PasswordPolicy]:
    file = open(filename, 'r')
    if target_object == 'PasswordPolicy':
        policies = []
        for line in file:
            a = line.split(': ')
            b = a[0].split()
            c = b[0].split('-')
            policies.append(PasswordPolicy(
                target_char=b[1],
                min_occurrences=c[0],
                max_occurrences=c[1],
                password=a[1].strip('\n')
                )
            )
        return policies
    elif target_object == 'OTCP':
        policies = []
        for line in file:
            a = line.split(': ')
            b = a[0].split()
            c = b[0].split('-')
            policies.append(OTCP(
                target_char=b[1],
                first_index=c[0],
                second_index=c[1],
                password=a[1].strip('\n')
                )
            )
        return policies


if __name__ == '__main__':
    # read in input file
    # password_policies = convert_file_to_list('input.txt', 'PasswordPolicy')
    password_policies = convert_file_to_list('input.txt', 'OTCP')

    # loop through passwords to check if they're valid
    counter = 0
    for policy in password_policies:
        if policy.is_valid():
            counter += 1

    # return number of valid passwords
    print(counter)
