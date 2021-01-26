import re

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

    def test_zip_code_invalid_first_letter(self):
        assert not is_valid('QC1A 1BB')

    def test_zip_code_invalid_second_letter(self):
        assert not is_valid('BJ1A 1BB')

    def test_zip_code_invalid_third_letter(self):
        assert not is_valid('E1Z 1BB')

    def test_zip_code_invalid_fourth_letter(self):
        assert not is_valid('EC1Z 1BB')

    def test_zip_code_invalid_last_inward_letters(self):
        assert not is_valid('EC1A 1CI')

    def test_zip_code_invalid_area_when_district_is_zero(self):
        assert not is_valid('BR0 1BB')

    def test_zip_code_valid_area_when_district_is_zero(self):
        assert is_valid('CR0 1BB')

    def test_zip_code_valid_area_is_BS_district_is_ten(self):
        assert is_valid('BS10 1BB')

    def test_zip_code_valid_double_digit_district(self):
        assert is_valid('AB10 1BB')

    def test_zip_code_valid_single_digit_district(self):
        assert is_valid('BR1 1BB')

    def test_zip_code_invalid_AA9A_format_EC(self):
        assert not is_valid('EC5W 1BB')

    def test_zip_code_invalid_AA9A_format_SW(self):
        assert not is_valid('SW2A 1BB')

    def test_zip_code_invalid_AA9A_format_WC(self):
        assert not is_valid('WC3A 1BB')

    def test_zip_code_valid_AA9A_format_WC(self):
        assert is_valid('WC2A 1BB')

    def test_zip_code_invalid_AA9A_format_NW_bad_digit(self):
        assert not is_valid('NW2W 1BB')

    def test_zip_code_invalid_AA9A_format_NW_bad_letter(self):
        assert not is_valid('NW1B 1BB')

    def test_zip_code_valid_AA9A_format_NW(self):
        assert is_valid('NW1W 1BB')

    def test_zip_code_invalid_AA9A_format_SE(self):
        assert not is_valid('SE1C 1BB')

    def test_zip_code_valid_AA9A_format_SE(self):
        assert is_valid('SE1P 1BB')

    def test_zip_code_invalid_A9A_format_W(self):
        assert not is_valid('W2C 1BB')

    def test_zip_code_valid_A9A_format_W(self):
        assert is_valid('W1C 1BB')

    def test_zip_code_invalid_A9A_format_E(self):
        assert not is_valid('E1C 1BB')

    def test_zip_code_valid_A9A_format_E(self):
        assert is_valid('E1W 1BB')

    def test_zip_code_invalid_A9A_format_N_bad_digit(self):
        assert not is_valid('N2C 1BB')

    def test_zip_code_invalid_A9A_format_N_bad_letter(self):
        assert not is_valid('N1D 1BB')

    def test_zip_code_valid_A9A_format_N(self):
        assert is_valid('N1P 1BB')
