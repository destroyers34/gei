﻿from django.contrib import admin
from listes_de_prix.models import Option, Machine, Fournisseur, Categorie

class MachinerieInline(admin.TabularInline):
    model = Option.machines.through
    extra = 1

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ['nom',]
    ordering       = ('nom', )

class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom','telephonne','fax','siteweb','devise','ratio')
    list_filter = ('devise',)
    ordering = ('nom',)
    
class MachineAdmin(admin.ModelAdmin):
    list_display   = ('numero', 'description','categorie', 'fournisseur', 'prix_fournisseur', 'prixCAD', 'dateprix', 'escompte', 'cost', 'ratioEffectif', 'plMin', 'profit', 'profit_pourcent')
    search_fields = ['numero', 'description','categorie', 'fournisseur']
    list_filter    = ('categorie', 'fournisseur')
    ordering       = ('numero', )
    inlines = [
        MachinerieInline,
    ]
    
class OptionAdmin(admin.ModelAdmin):
    actions = None
    list_display   = ('numero', 'description', 'fournisseur', 'prix_fournisseur', 'prixCAD', 'dateprix', 'escompte', 'cost', 'ratioEffectif', 'plMin', 'profit', 'profit_pourcent')
    search_fields = ['numero', 'description', 'fournisseur']
    list_filter    = ('fournisseur',)
    ordering       = ('numero', )
    inlines = [
        MachinerieInline,
    ]
    exclude = ('machines',)
    
admin.site.register(Categorie,CategorieAdmin)
admin.site.register(Option,OptionAdmin)
admin.site.register(Machine, MachineAdmin)
admin.site.register(Fournisseur,FournisseurAdmin)