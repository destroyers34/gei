#-*- coding: utf-8 -*-

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, get_object_or_404
from fournisseurs.models import Fournisseur

def detail_fournisseur(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    return render(request, 'fournisseurs/detail_fournisseur.html', {'fournisseur': fournisseur})    