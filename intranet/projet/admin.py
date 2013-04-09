from django.contrib import admin
from projet.models import *

class ProjetAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nom','modele','serial_number','budget_mat','budget_mo','client','date_soumission','date_debut','date_fin','actif')
    list_filter = ('numero', 'nom','modele','serial_number','date_soumission','date_debut','date_fin')
    ordering = ('-actif','-numero',)

admin.site.register(Projet,ProjetAdmin)
