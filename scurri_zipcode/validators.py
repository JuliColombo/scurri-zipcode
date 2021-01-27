import re
from abc import ABC

from scurri_zipcode.exceptions import ZipCodeException
from scurri_zipcode.utils import *


class Validator(ABC):
    def __init__(self, zip_code):
        self.zip_code = zip_code
        self.area = self.__get_area(zip_code)
        self.district = self.__get_district(zip_code)

    def __get_outward_code(self, zip_code):
        return zip_code[:-INWARD_CODE_LENGTH]

    def __is_special_case(self, zip_code):
        return not bool(re.search(r'\d', self.__get_outward_code(zip_code)))

    def __get_area(self, zip_code):
        return re.findall('([A-Z ]*)\d*.*', zip_code)[0]

    def __get_district(self, zip_code):
        if self.__is_special_case(zip_code):
            return ''
        return self.__get_outward_code(zip_code).split(self.__get_area(zip_code))[1].replace(' ', '')

    def validate(self):
        if not self.is_valid():
            raise ZipCodeException("Zip code is invalid")

    def matches(self) -> bool:
        pass

    def is_valid(self) -> bool:
        pass


class GeneralValidator(Validator):
    def matches(self) -> bool:
        return True

    def is_valid(self) -> bool:
        return bool(re.search(UK_ZIP_CODE_REGEX, self.zip_code)) and \
               not re.search(FORBIDDEN_FIRST_LETTERS_OUTWARD_REGEX, self.zip_code) and \
               not re.search(FORBIDDEN_SECOND_LETTERS_OUTWARD_REGEX, self.zip_code) and \
               not re.search(LAST_INWARD_LETTERS_REGEX, self.zip_code)


class ZeroDistrictValidator(Validator):
    def matches(self) -> bool:
        return self.district == '0'

    def is_valid(self) -> bool:
        return self.area in ZERO_DISTRICT_AREAS


class DoubleDigitDistrictValidator(Validator):
    def matches(self) -> bool:
        return self.area in DOUBLE_DIGIT_DISTRICT_AREAS

    def is_valid(self) -> bool:
        return bool(re.search(AA99_FORMAT_REGEX, self.zip_code))


class SingleDigitDistrictValidator(Validator):
    def matches(self) -> bool:
        return self.area in SINGLE_DIGIT_DISTRICT_AREAS

    def is_valid(self) -> bool:
        return bool(re.search(AA9_FORMAT_REGEX, self.zip_code))


class A9AFormatMixin:
    def matches_format(self, zip_code) -> bool:
        return bool(re.search(A9A_FORMAT_REGEX, zip_code))


class AA9AFormatMixin:
    def matches_format(self, zip_code) -> bool:
        return bool(re.search(AA9A_FORMAT_REGEX, zip_code))


class A9AFormatLastLetterValidator(Validator, A9AFormatMixin):
    def matches(self) -> bool:
        return self.matches_format(self.zip_code)

    def is_valid(self) -> bool:
        return bool(re.search(LAST_OUTWARD_LETTERS_FOR_A9A_REGEX, self.zip_code))


class A9AFormatSpecialCasesValidator(Validator, A9AFormatMixin):
    def matches(self) -> bool:
        return self.matches_format(self.zip_code)

    def is_valid(self) -> bool:
        district_number = int(self.district[0])
        district_letter = self.district[1]
        return (self.area == 'W' and district_number == 1) or \
               (self.area == 'E' and district_number == 1 and district_letter == 'W') or \
               (self.area == 'N' and district_number == 1 and district_letter in ['C', 'P'])


class AA9AFormatLastLetterValidator(Validator, AA9AFormatMixin):
    def matches(self) -> bool:
        return self.matches_format(self.zip_code)

    def is_valid(self) -> bool:
        return bool(re.search(LAST_OUTWARD_LETTERS_FOR_AA9A_REGEX, self.zip_code))


class AA9AFormatSpecialCasesValidator(Validator, AA9AFormatMixin):
    def matches(self) -> bool:
        return self.matches_format(self.zip_code)

    def is_valid(self) -> bool:
        district_number = int(self.district[0])
        district_letter = self.district[1]
        return (self.area == 'EC' and district_number in [1, 2, 3, 4]) or \
               (self.area == 'SW' and district_number == 1) or \
               (self.area == 'WC' and district_number in [1, 2]) or \
               (self.area == 'NW' and district_number == 1 and district_letter == 'W') or \
               (self.area == 'SE' and district_number == 1 and district_letter == 'P')
