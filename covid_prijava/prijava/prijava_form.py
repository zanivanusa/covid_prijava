from django.forms import ModelForm
from django import forms
from .models import Prijava



class PrijavaForm(ModelForm):
    class Meta:
        model = Prijava
        fields =['ime','priimek','emso','mail']

    def clean_emso(self):
        emso = self.cleaned_data.get('emso')
        if Prijava.objects.filter(emso=emso).exists():
            datum = Prijava.objects.get(emso = emso).datum_vpisa.strftime('%Y.%d.%m ob %H:%M:%S')
            raise forms.ValidationError('Ta emšo ze obstaja, datum vpisa z njim je: '+ datum)
        else:
            return emso
      