import re

from scurri_zipcode.exceptions import ZipCodeException
from scurri_zipcode.utils import *


def __outward_code(zip_code):
    return zip_code[:-INWARD_CODE_LENGTH].replace(' ', '')


def __is_special_case(zip_code):
    return not bool(re.search(r'\d', __outward_code(zip_code)))


def __area(zip_code):
    return re.findall('([A-Z ]*)\d*.*', zip_code)[0]


def __district(zip_code):
    if __is_special_case(zip_code):
        return ''
    return __outward_code(zip_code).split(__area(zip_code))[1]


def __matches_basic_validations(zip_code):
    return not re.search(UK_ZIP_CODE_REGEX, zip_code) or \
           re.search(FORBIDDEN_FIRST_LETTERS_OUTWARD_REGEX, zip_code) or \
           re.search(FORBIDDEN_SECOND_LETTERS_OUTWARD_REGEX, zip_code) or \
           re.search(LAST_INWARD_LETTERS_REGEX, zip_code)


def __matches_last_area_letter(zip_code):
    if re.search(A9A_FORMAT_REGEX, zip_code):
        return not re.search(LAST_OUTWARD_LETTERS_FOR_A9A_REGEX, zip_code)
    if re.search(AA9A_FORMAT_REGEX, zip_code):
        return not re.search(LAST_OUTWARD_LETTERS_FOR_AA9A_REGEX, zip_code)
    return False


def __matches_district_number(zip_code):
    area = __area(zip_code)
    district = __district(zip_code)
    if district == '0':
        return area in ZERO_DISTRICT_AREAS
    return True


def __matches_double_digit_district(zip_code):
    if __area(zip_code) in DOUBLE_DIGIT_DISTRICT_AREAS:
        return re.search(AA99_FORMAT_REGEX, zip_code)
    return True


def __matches_single_digit_district(zip_code):
    if __area(zip_code) in SINGLE_DIGIT_DISTRICT_AREAS:
        return re.search(AA9_FORMAT_REGEX, zip_code)
    return True


def __matches_aa9a_special_cases(area, district):
    district_number = int(district[0])
    district_letter = district[1]
    return (area == 'EC' and district_number in [1, 2, 3, 4]) or \
           (area == 'SW' and district_number == 1) or \
           (area == 'WC' and district_number in [1, 2]) or \
           (area == 'NW' and district_number == 1 and district_letter == 'W') or \
           (area == 'SE' and district_number == 1 and district_letter == 'P')


def __matches_a9a_special_cases(area, district):
    district_number = int(district[0])
    district_letter = district[1]
    return (area == 'W' and district_number == 1) or \
           (area == 'E' and district_number == 1 and district_letter == 'W') or \
           (area == 'N' and district_number == 1 and district_letter in ['C', 'P'])


def __matches_special_area_formats(zip_code):
    area = __area(zip_code)
    district = __district(zip_code)
    if re.search(AA9A_FORMAT_REGEX, zip_code) and \
            not __matches_aa9a_special_cases(area, district):
        return False
    if re.search(A9A_FORMAT_REGEX, zip_code) and not \
            __matches_a9a_special_cases(area, district):
        return False
    return True


def __not_valid(zip_code):
    return __matches_basic_validations(zip_code) or \
           __matches_last_area_letter(zip_code) or \
           not __matches_district_number(zip_code) or \
           not __matches_double_digit_district(zip_code) or \
           not __matches_single_digit_district(zip_code) or \
           not __matches_special_area_formats(zip_code)


def __validate(zip_code):
    if __not_valid(zip_code):
        raise ZipCodeException("Zip code is invalid")


def __add_whitespace(zip_code):
    if ' ' in zip_code:
        return zip_code

    inward_code = zip_code[-INWARD_CODE_LENGTH:]
    outward_code = zip_code[:-INWARD_CODE_LENGTH]
    return f'{outward_code} {inward_code}'


def is_valid(zip_code):
    try:
        return bool(format(zip_code))
    except ZipCodeException:
        return False


def format(zip_code):
    zip_code = zip_code.upper()
    __validate(zip_code)
    return __add_whitespace(zip_code)
