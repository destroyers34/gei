from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from gpao.models import Nm, Pe


def main_gpao(request):
    return render(request, "gpao/main_gpao.html")


def liste_nm(request):
    liste_nm = Nm.objects.all()
    return render(request, "gpao/liste_nm.html", {'liste_nm': liste_nm})


def details_nm(request, no_nm):
    nm = Nm.objects.get(reference=no_nm)
    return render(request, "gpao/details_nm.html", {'nm': nm})


def liste_pe(request):
    liste_pe = Pe.objects.all()
    return render(request, "gpao/liste_pe.html", {'liste_pe': liste_pe})