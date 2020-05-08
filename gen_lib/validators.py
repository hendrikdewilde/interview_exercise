import logging
from datetime import date, datetime

from django.core.exceptions import ValidationError

log = logging.getLogger(__name__)


def char_field_only_digits(value):
    if value != '' and not value.isdigit():
        raise ValidationError('Only digits allowed.')


def no_space_in_field(value):
    for char in value:
        if char in [' ']:
            raise ValidationError('No white spaces allowed.')


def date_not_in_future(value):
    if value > date.today():
        raise ValidationError('The date may not be in the future.')


def date_not_in_past(value):
    if value < date.today():
        raise ValidationError('The date may not be in the past.')


def datetime_not_in_future(value):
    if value > datetime.today():
        raise ValidationError('The datetime may not be in the future.')


def datetime_not_in_past(value):
    if value < datetime.today():
        raise ValidationError('The datetime may not be in the past.')
