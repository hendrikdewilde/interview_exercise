from unittest import TestCase

from gen_lib.utils import *


class UtilsTestCase(TestCase):
    """Will use unittest"""

    # string_to_base64
    def test_string_to_base64_valid_1(self):
        assert string_to_base64('abc') == b'YWJj'

    # base64_to_string
    def test_base64_to_string_valid_1(self):
        assert base64_to_string(b'YWJj') == 'abc'

    # string_to_byte
    def test_string_to_byte_valid_1(self):
        assert string_to_byte('abc') == b'abc'

    # byte_to_string
    def test_byte_to_string_valid_1(self):
        assert byte_to_string(b'abc') == 'abc'

    # strip_non_ascii
    def test_strip_non_ascii_valid_1(self):
        assert strip_non_ascii('abcê') == 'abc'

    # strip_non_ascii
    def test_strip_non_numeric_valid_1(self):
        assert strip_non_numeric('abc123') == '123'

    # day_of_month_suff
    def test_day_of_month_suff_valid_1(self):
        assert day_of_month_suff(1) == 'st'

    def test_day_of_month_suff_valid_2(self):
        assert day_of_month_suff(22) == 'nd'

    def test_day_of_month_suff_valid_3(self):
        assert day_of_month_suff(3) == 'rd'

    def test_day_of_month_suff_valid_4(self):
        assert day_of_month_suff(27) == 'th'

    # last_day_of_month
    def test_last_day_of_month_valid_1(self):
        enter_date = date(2020, 5, 11)
        assert last_day_of_month(enter_date) == date(2020, 5, 31)

    def test_last_day_of_month_valid_2(self):
        enter_date = date(2020, 6, 11)
        assert last_day_of_month(enter_date) == date(2020, 6, 30)
