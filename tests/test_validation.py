from scurri_zipcode.functions import is_valid


class TestValidation:
    def test_zip_code_AA9A_9AA_format_is_valid(self):
        assert is_valid('EC1A 1BB')

    def test_zip_code_A9A_9AA_format_is_valid(self):
        assert is_valid('W1A 0AX')

    def test_zip_code_A9_9AA_format_is_valid(self):
        assert is_valid('M1 1AE')

    def test_zip_code_A99_9AA_format_is_valid(self):
        assert is_valid('B33 8TH')

    def test_zip_code_AA9_9AA_format_is_valid(self):
        assert is_valid('CR2 6XH')

    def test_zip_code_AA99_9AA_format_is_valid(self):
        assert is_valid('DN55 1PT')

    def test_zip_code_special_case_is_valid(self):
        assert is_valid('ASCN 1ZZ')

    def test_zip_code_in_lowercase_is_valid(self):
        assert is_valid('ec1a 1bb')

    def test_zip_code_with_extra_whitespaces_is_invalid(self):
        assert not is_valid('E C 1 A1 B B')
