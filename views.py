from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import uporabnik
import datetime
import re



def home(request):
    return render(request, 'home.html', {'name':'teo'} )


emso_oblika ="^([1,2][0-9])([0,1][0-9])([0-9]{3})([5][0][5,0])([0-9]{3})"
mail_oblika = "([a-zA-Z0-9.\.-]+)@(gmail|outlook|hotmal)\.(com)"

def vnos(request):

    user = uporabnik()
    user.ime = request.POST["ime"]
    user.priimek = request.POST["priimek"]
    user.emso = request.POST["emso"]
    user.mail = request.POST["mail"]
    user.datum_vpisa = datetime.datetime.now()


        #error checking
        #verjetno ni pravi nacin saj je bolj smiselno da bi to v model bilo
    if not user.emso.isdigit():
        messages.info(request, 'emso mora biti samo številke')
        return redirect('/')

    if user.emso == "":
        messages.info(request, 'niste vnesli emsoja')
        return redirect('/')
    if user.emso == type(str):
        messages.info(request, 'emso mora vsebovati samo stevilke')
        return redirect('/')

    if user.ime == "" or len(user.ime)>1 or user.ime.isdigit():
        messages.info(request, 'vnesite začetnico imena')
        return redirect('/')
    if user.priimek == "" or len(user.priimek) > 1 or user.priimek.isdigit():
        messages.info(request, 'vnesite začetnico priimka')
        return redirect('/')
    if user.mail == "":
        messages.info(request, 'prosim vnesite mail')
        return redirect('/')
    if len(user.mail)>60:
        messages.info(request, 'email je predolgi')
        return redirect('/')


    emso = request.POST["emso"]

    if uporabnik.objects.filter(emso = emso).exists(): #preverimo če emšo že obstaja v DB
        datum = uporabnik.objects.get(emso = emso).datum_vpisa.strftime('%Y.%d.%m ob %H:%M:%S')
        messages.info(request, 'Ta emšo že obstaja,\ndatum vpisa s tem emšojem je: '+str(datum))
        return redirect('/')

    ujemanje_mail = re.fullmatch(mail_oblika, user.mail)#match / fullmatch?
    ujemanje_emso = re.fullmatch(emso_oblika, user.emso)


    if not ujemanje_emso:
        messages.info(request,"invaliden emso")
        return redirect('/')

    if not ujemanje_mail:
        messages.info(request,"invaliden email naslov")
        return redirect('/')

    else:
        user.save()
        return render(request, "informacije.html",{'uporabnik':user})
