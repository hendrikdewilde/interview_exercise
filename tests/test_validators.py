from unittest import TestCase

from gen_lib.validators import *


class ValidatorsTestCase(TestCase):
    """Will use unittest"""

    # char_field_only_digits
    def test_char_field_only_digits_valid_1(self):
        self.assertRaises(ValidationError, char_field_only_digits, 'abc')

    def test_char_field_only_digits_valid_2(self):
        with self.assertRaises(ValidationError):
            char_field_only_digits('abc')

    def test_char_field_only_digits_valid_3(self):
        assert char_field_only_digits('123') is None

    # no_space_in_field
    def test_no_space_in_field_valid_1(self):
        self.assertRaises(ValidationError, no_space_in_field, 'ab c')

    def test_no_space_in_field_valid_2(self):
        with self.assertRaises(ValidationError):
            no_space_in_field('ab c')

    def test_no_space_in_field_valid_3(self):
        assert no_space_in_field('123') is None

    # date_not_in_future
    def test_date_not_in_future_valid_1(self):
        self.assertRaises(ValidationError, date_not_in_future,
                          date(2030, 5, 1))

    def test_date_not_in_future_valid_2(self):
        with self.assertRaises(ValidationError):
            date_not_in_future(date(2030, 5, 1))

    def test_date_not_in_future_valid_3(self):
        assert date_not_in_future(date.today()) is None

    # date_not_in_past
    def test_date_not_in_past_valid_1(self):
        self.assertRaises(ValidationError, date_not_in_past, date(2020, 5, 1))

    def test_date_not_in_past_valid_2(self):
        with self.assertRaises(ValidationError):
            date_not_in_past(date(2020, 5, 1))

    def test_date_not_in_past_valid_3(self):
        assert date_not_in_past(date.today()) is None

    # datetime_not_in_future
    def test_datetime_not_in_future_valid_1(self):
        self.assertRaises(ValidationError, datetime_not_in_future,
                          datetime(2030, 5, 1, 14, 45, 58))

    def test_datetime_not_in_future_valid_2(self):
        with self.assertRaises(ValidationError):
            datetime_not_in_future(datetime(2030, 5, 1, 14, 45, 58))

    # datetime_not_in_past
    def test_datetime_not_in_past_valid_1(self):
        self.assertRaises(ValidationError, datetime_not_in_past,
                          datetime(2020, 5, 1, 14, 45, 58))

    def test_datetime_not_in_past_valid_2(self):
        with self.assertRaises(ValidationError):
            datetime_not_in_past(datetime(2020, 5, 1, 14, 45, 58))
