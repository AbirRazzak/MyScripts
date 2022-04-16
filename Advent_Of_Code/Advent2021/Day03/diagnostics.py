from pydantic import BaseModel


class DigitCount(BaseModel):
    num_0s: int
    num_1s: int


def convert_binary_string_to_int(binary_string: str) -> int:
    return int(binary_string, 2)


class DiagnosticReport(BaseModel):
    binary_numbers: list[str] = []
    digit_counts: list[DigitCount] = []

    def load(self, report: str):
        for line in report.split('\n'):
            self.binary_numbers.append(line)

    def get_digit_count(self) -> list[DigitCount]:
        if not self.digit_counts:

            for digits in self.binary_numbers[0]:
                digit_counts = DigitCount(num_0s=0, num_1s=0)
                self.digit_counts.append(digit_counts)

            for number in self.binary_numbers:
                for i in range(len(number)):
                    digit = number[i]
                    counter = self.digit_counts[i]
                    if digit == '1':
                        counter.num_1s += 1

                    if digit == '0':
                        counter.num_0s += 1

        return self.digit_counts

    def get_gamma_rate(self) -> str:
        gamma_rate = ''
        digit_counts = self.get_digit_count()

        for count in digit_counts:
            if count.num_1s >= count.num_0s:
                gamma_rate += '1'

            if count.num_0s > count.num_1s:
                gamma_rate += '0'

        return gamma_rate

    def get_epsilon_rate(self) -> str:
        epsilon_rate = ''
        digit_counts = self.get_digit_count()

        for count in digit_counts:
            if count.num_1s >= count.num_0s:
                epsilon_rate += '0'

            if count.num_0s > count.num_1s:
                epsilon_rate += '1'

        return epsilon_rate

    def get_oxygen_generator_rating(self) -> str:
        _sub_report = DiagnosticReport()

        values_filter = set(self.binary_numbers.copy())
        for i in range(len(self.binary_numbers[0])):
            _sub_report = DiagnosticReport()
            _sub_report.binary_numbers = list(values_filter)
            gamma_rate = _sub_report.get_gamma_rate()

            digit = gamma_rate[i]
            values_to_remove = set()
            for value in values_filter:
                if value[i] != digit:
                    values_to_remove.add(value)
            values_filter -= values_to_remove

            if len(values_filter) == 1:
                return values_filter.pop()

    def get_co2_scrubber_rating(self) -> str:
        _sub_report = DiagnosticReport()

        values_filter = set(self.binary_numbers.copy())
        for i in range(len(self.binary_numbers[0])):
            _sub_report = DiagnosticReport()
            _sub_report.binary_numbers = list(values_filter)
            epsilon_rate = _sub_report.get_epsilon_rate()

            digit = epsilon_rate[i]
            values_to_remove = set()
            for value in values_filter:
                if value[i] != digit:
                    values_to_remove.add(value)
            values_filter -= values_to_remove

            if len(values_filter) == 1:
                return values_filter.pop()
