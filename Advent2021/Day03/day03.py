from Day03 import PUZZLE_INPUT
from Day03.diagnostics import DiagnosticReport, convert_binary_string_to_int


def run_part1(r: DiagnosticReport) -> int:
    gamma_rate = convert_binary_string_to_int(r.get_gamma_rate())
    epsilon_rate = convert_binary_string_to_int(r.get_epsilon_rate())
    return gamma_rate * epsilon_rate


def run_part2(r: DiagnosticReport) -> int:
    o2_gen_rate = convert_binary_string_to_int(r.get_oxygen_generator_rating())
    co2_scrub_rate = convert_binary_string_to_int(r.get_co2_scrubber_rating())
    return o2_gen_rate * co2_scrub_rate


if __name__ == '__main__':
    report = DiagnosticReport()
    report.load(PUZZLE_INPUT)

    print(f"Part 1: {run_part1(report)}")
    print(f"Part 2: {run_part2(report)}")
