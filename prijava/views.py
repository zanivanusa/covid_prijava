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
            form.save()
            return redirect('/podatki')
    else:
        form = PrijavaForm()
    
    return render(request, "prijava.html", {'PrijavaForm':form})


def prijava_podatki(request):
    podatki = Prijava.objects.latest('id')#nekak drugace ker lehko vpises samo #podatki pa ti vrze zadnjega ustvarjenega
    context = {
        'ime':podatki.ime,
        'priimek':podatki.priimek,
        'emso': podatki.emso,
        'mail':podatki.mail,
        'datum_vpisa':podatki.datum_vpisa
        }
    return render(request, "podatki.html", context)
