from django.http import HttpResponse
from .prijava_form import PrijavaForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Prijava
from django.contrib.auth.models import User, auth

def prijava(request):
    if request.method == "POST":
        form =PrijavaForm(request.POST)
        if form.is_valid():
            priimek = form.cleaned_data['priimek']
            ime = form.cleaned_data['ime']
            emso = form.cleaned_data['emso']
            mail = form.cleaned_data['mail']
            obj = form.save()
            datum_vpisa = Prijava.objects.get(emso=emso).datum_vpisa
            context = {
                'ime':ime,
                'priimek':priimek,
                'emso': emso,
                'mail':mail,
                'datum_vpisa':datum_vpisa
                }
            return render(request, "podatki.html", context)
    else:
        form = PrijavaForm()
    
    return render(request, "prijava.html", {'PrijavaForm':form})
