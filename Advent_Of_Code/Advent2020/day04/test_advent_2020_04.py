import pytest
from advent_2020_04 import BatchFileParser, NorthPoleCredential, PassportScanner


def test_passport_scanner_convert_to_dict_without_newlines():
    input = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm'

    ps = PassportScanner()

    result = ps.convert_to_dict(input=input)
    assert result == {
        'ecl': 'gry',
        'pid': '860033327',
        'eyr': '2020',
        'hcl': '#fffffd',
        'byr': '1937',
        'iyr': '2017',
        'cid': '147',
        'hgt': '183cm'
    }


def test_passport_scanner_convert_to_dict_with_newlines():
    input = 'hcl:#ae17e1 iyr:2013\neyr:2024\necl:brn pid:760753108 byr:1931\nhgt:179cm'

    ps = PassportScanner()

    result = ps.convert_to_dict(input=input)
    assert result == {
        'hcl': '#ae17e1',
        'iyr': '2013',
        'eyr': '2024',
        'ecl': 'brn',
        'pid': '760753108',
        'byr': '1931',
        'hgt': '179cm'
    }


def test_passport_scanner_validate_passport_without_newlines():
    input = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm'
    expected_object = NorthPoleCredential(
        ecl='gry',
        pid='860033327',
        eyr='2020',
        hcl='#fffffd',
        byr='1937',
        iyr='2017',
        cid='147',
        hgt='183cm'
    )

    ps = PassportScanner()

    result = ps.validate_passport(passport=input)
    assert result == expected_object


def test_passport_scanner_validate_passport_with_invalid_passport_returns_none():
    input = 'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929'
    ps = PassportScanner()

    result = ps.validate_passport(passport=input)
    assert result == None


def test_passport_scanner_validate_passport_without_cid():
    input = 'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm'
    expected_object = NorthPoleCredential(
        hcl='#ae17e1',
        iyr='2013',
        eyr='2024',
        ecl='brn',
        pid='760753108',
        byr='1931',
        hgt='179cm'
    )
    
    
    ps = PassportScanner()

    result = ps.validate_passport(passport=input)
    assert result == expected_object

def test_passport_scanner_validate_passport_with_invalid_passport_without_cid_returns_none():
    input = 'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in'
    ps = PassportScanner()

    result = ps.validate_passport(passport=input)
    assert result == None


@pytest.mark.parametrize(
    'input',
    [
        'eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926',
        'iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946',
        'hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277',
        'hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007',
        'hgt:190cm ecl:brn eyr:2021 hcl:#123abc iyr:2011 pid:0123456789 byr:2001'
    ]
)
def test_passport_scanner_validate_passport_with_additional_validation_returns_none(input):
    ps = PassportScanner()

    result = ps.validate_passport(passport=input)
    assert result == None

def test_batch_file_parser():
    input = '''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in'''

    bfp = BatchFileParser()

    result = bfp.parse_batch_file(batch_file=input)
    assert len(result) == 2