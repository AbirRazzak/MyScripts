from pydantic import BaseModel


class DigitCount(BaseModel):
    num_0s: int
    num_1s: int


class BinaryNumber(str):
    pass


class DiagnosticReport(BaseModel):
    binary_numbers: list[BinaryNumber] = []

    def load(self, report: str):
        for line in report:
            self.binary_numbers.append(BinaryNumber(line))

    def get_gamma_rate(self):
        gamma_rate = 0

        for number in self.binary_numbers:
            pass

        return gamma_rate
