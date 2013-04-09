from django.contrib import admin
from machines.models import Categorie, Option, Machine, Machine_Option
from django.forms.models import modelformset_factory

class OptionInline(admin.TabularInline):
    model = Machine_Option
    extra = 1

class MachineAdmin(admin.ModelAdmin):
    list_display   = ('code', 'description','categorie', 'fournisseur', 'prixliste', 'prixCAD', 'dateprix', 'escompte', 'cost', 'ratioEffectif', 'plMin', 'profit', 'profit_pourcent')
    search_fields = ['code', 'description','categorie__nom', 'fournisseur__nom']
    list_filter    = ('code', 'description','categorie', 'fournisseur', 'prixliste', 'dateprix','escompte','ratio')
    ordering       = ('code', )
    inlines = [
        OptionInline,
    ]

class OptionAdmin(admin.ModelAdmin):
    actions = None
    list_display   = ('code', 'description', 'prixliste','escompte','ratio')
    list_filter    = ('code', 'description', 'prixliste','escompte','ratio')
    ordering       = ('code', )
    
admin.site.register(Categorie)
admin.site.register(Option,OptionAdmin)
admin.site.register(Machine, MachineAdmin)