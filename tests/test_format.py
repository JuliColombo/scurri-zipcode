import pytest

from scurri_zipcode.exceptions import ZipCodeException
from scurri_zipcode.functions import format


class TestFormat:
    def test_zip_code_in_lowercase_returns_uppercase(self):
        assert format('ec1a 1bb') == 'EC1A 1BB'

    def test_valid_zip_code_returns_valid_zip_code(self):
        assert format('EC1A 1BB') == 'EC1A 1BB'

    def test_valid_zip_code_without_whitespace_returns_valid_zip_code(self):
        assert format('EC1A1BB') == 'EC1A 1BB'

    def test_invalid_zip_code_returns_exception(self):
        with pytest.raises(ZipCodeException):
            format('EC1A 111')
