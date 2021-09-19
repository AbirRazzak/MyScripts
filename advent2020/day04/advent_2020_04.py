from typing import Dict, List, Literal, Optional
from pydantic import BaseModel, validator
from pydantic.tools import parse_obj_as
from pydantic.types import conint, constr

class NorthPoleCredential(BaseModel):
    byr: conint(ge=1920, le=2002)
    iyr: conint(ge=2010, le=2020)
    eyr: conint(ge=2020, le=2030)
    hgt: constr(regex=r'[0-9]+(cm|in)')
    hcl: constr(regex=r'#([0-9]|[a-f]){6}')
    ecl: Literal['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    pid: constr(regex=r'^[0-9]{9}$')
    cid: Optional[str]

    @validator('hgt')
    def height_validation(cls, v:str):
        if v.endswith('cm'):
            height = int(v[:-2])
            lower_bound = 150
            upper_bound = 193
            if not lower_bound <= height <= upper_bound:
                raise ValueError(f'Height of {height}cm has to be >= {lower_bound}cm and <= {upper_bound}cm.')
        
        if v.endswith('in'):
            height = int(v[:-2])
            lower_bound = 59
            upper_bound = 76
            if not lower_bound <= height <= upper_bound:
                raise ValueError(f'Height of {height}cm has to be >= {lower_bound}in and <= {upper_bound}in.')

        return v


class PassportScanner:

    def validate_passport(
        self,
        passport: str
    ) -> Optional[NorthPoleCredential]:

        input_as_dict = self.convert_to_dict(input=passport)
        try:
            parsed_cred = parse_obj_as(NorthPoleCredential, input_as_dict)
            return parsed_cred
        except:
            return None

    def convert_to_dict(
        self,
        input: str
    ) -> Dict[str,str]:

        input_as_dict: Dict[str, str] = {}

        key_value_pairs = input.replace('\n', ' ').split(sep=' ')

        for key_value_pair in key_value_pairs:
            key_value = key_value_pair.split(sep=':')
            
            key = key_value[0]
            value = key_value[1]

            input_as_dict[key] = value
        
        return input_as_dict

class BatchFileParser:
    def parse_batch_file(
        self,
        batch_file: str
    ) -> List[NorthPoleCredential]:
        ps = PassportScanner()
        valid_passports: List[NorthPoleCredential] = []
        passports = batch_file.split('\n\n')

        for passport in passports:
            valid_passport = ps.validate_passport(passport=passport)

            if valid_passport:
                valid_passports.append(valid_passport)
        
        return valid_passports

if __name__ == '__main__':
    print('Setting up passport scanner...')

    f = open("input.txt", "r")
    input = f.read()

    bfp = BatchFileParser()
    valid_passports = bfp.parse_batch_file(batch_file=input)

    print(f'RESULT: Valid Passports: {len(valid_passports)}.')