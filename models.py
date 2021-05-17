from django.db import models
from django.contrib import messages
from django import forms
from django.core.validators import validate_email
import datetime
import re

emso_oblika ="^([1,2][0-9])([0,1][0-9])([0-9]{3})([5][0][5,0])([0-9]{3})"
#mail_oblika = "([a-zA-Z0-9.\.-]+)@(gmail|outlook|hotmal)\.(com)"
#ime_oblika = "([a-zA-Z])"
#priimek_oblika = "([a-zA-Z])"

#mogoce novi file kje so validatorji in importam
class uporabnik(models.Model):

    ime = models.CharField(max_length = 1)
    priimek = models.CharField(max_length = 1)
    emso = models.BigIntegerField()#validators=[validate_emso]
    mail = models.EmailField(max_length = 60)
    datum_vpisa = models.DateTimeField(auto_now_add =True)

 #   def validate_emso(Self):
 #       emso = self.cleaned_data.get("emso")
 #       reg = re.compile("^([1,2][0-9])([0,1][0-9])([0-9]{3})([5][0][5,0])([0-9]{3})")
 #       if reg.match(emso):
 #           if self.objects.filter(emso = emso).exists(): #preverimo če emšo že obstaja v DB
 #               datum = uporabnik.objects.get(emso = emso).datum_vpisa.strftime('%Y.%d.%m ob %H:%M:%S')
 #               messages.info(request, 'Ta emšo že obstaja,\ndatum vpisa s tem emšojem je: '+str(datum))
 #           else:
 #               return emso
 #       else:
 #           raise ValidationError("emso ni validen")
 #   def clean_ime(self):
 #       ime = self.cleaned_data.get("ime")
 #       if self.isdigit():
 #           raise ValidationError("vnesli ste številko")
 #       else:
 #           return ime
