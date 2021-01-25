import re

from scurri_zipcode.exceptions import ZipCodeException

UK_ZIP_CODE_REGEX = '^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?' \
                    '[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?' \
                    '[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$'

INWARD_CODE_LENGTH = 3


def __preprocess(zip_code):
    zip_code = zip_code.upper()
    zip_code = zip_code.replace(' ', '')
    return zip_code


def __validate(zip_code):
    if not re.search(UK_ZIP_CODE_REGEX, zip_code):
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
