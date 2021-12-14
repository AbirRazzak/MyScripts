from Day03.diagnostics import DiagnosticReport


EXAMPLE_INPUT = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''


def test_get_gamma_rate():
    report = DiagnosticReport()
    report.load(EXAMPLE_INPUT)
    assert report.get_gamma_rate() == '10110'


def test_get_epsilon_rate():
    report = DiagnosticReport()
    report.load(EXAMPLE_INPUT)
    assert report.get_epsilon_rate() == '01001'


def test_get_oxygen_generator_rating():
    report = DiagnosticReport()
    report.load(EXAMPLE_INPUT)
    assert report.get_oxygen_generator_rating() == '10111'


def test_get_co2_scrubber_rating():
    report = DiagnosticReport()
    report.load(EXAMPLE_INPUT)
    assert report.get_co2_scrubber_rating() == '01010'


