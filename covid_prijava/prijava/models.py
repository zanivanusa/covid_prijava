from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re

def is_letter(string):
    if string.isdigit():
        raise ValidationError("niste vnesli crke")
    else:
        return string

def emso_regex(emso):
    emso_oblika = r'[0,1,2,3]\d[0,1]\d{4}50[0,5]\d{3}'
    if re.fullmatch(emso_oblika, str(emso)):
        return emso
    else:
        raise ValidationError("Emšo ni validen")

def emso_verify(emso):

    emso_factor_map = [7, 6, 5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    control_digit = sum([int(emso[i]) * emso_factor_map[i] for i in range(12)]) % 11
    control_digit = 0 if control_digit == 0 else 11 - control_digit
    if control_digit == int(emso[12]):
        return emso
    else:
        raise ValidationError("Emšo ni validen")


class Prijava(models.Model):

    ime = models.CharField(max_length = 1, validators=[is_letter])
    priimek = models.CharField(max_length = 1, validators=[is_letter])#ce se emso zacne s 0, zacetek zbrise ker je int
    emso = models.CharField(unique=True, validators=[emso_regex, emso_verify], max_length=13)
    mail = models.EmailField(max_length = 60)
    datum_vpisa = models.DateTimeField(auto_now_add =True)


