from scurri_zipcode.exceptions import ZipCodeException
from scurri_zipcode.utils import INWARD_CODE_LENGTH
from scurri_zipcode.validators import Validator


def __create_validators(zip_code):
    validator_classes = Validator.__subclasses__()
    return [validator(zip_code) for validator in validator_classes if validator(zip_code).matches()]


def __validate(zip_code):
    validators = __create_validators(zip_code)
    for validator in validators:
        validator.validate()


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
