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


class Prijava(models.Model):

    ime = models.CharField(max_length = 1, validators=[is_letter])
    priimek = models.CharField(max_length = 1, validators=[is_letter])#ce se emso zacne s 0, zacetek zbrise ker je int
    emso = models.BigIntegerField(unique=True, validators=[emso_regex])
    mail = models.EmailField(max_length = 60)
    datum_vpisa = models.DateTimeField(auto_now_add =True)
    
