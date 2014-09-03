import re
from datetime import datetime, date
from django.core.exceptions import ValidationError


def alphanumeric_val(value):
    result = re.match("^[0-9a-zA-Z]*$", value)
    if result == None:
	msg = u"alphanumeric only"
	raise ValidationError(msg)


def name_val(value):
    result = re.match("^[a-zA-Z]", value)
    if result == None:
        msg = u"invalid name"
        raise ValidationError(msg)


def today_val(value):
    if value > date.today():
	msg = u"invalid date"
        raise ValidationError(msg)


