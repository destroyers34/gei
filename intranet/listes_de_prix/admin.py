from django.contrib import admin
from listes_de_prix.models import Option, Machine, Fournisseur, Categorie
from decimal import *


class MachinerieInline(admin.TabularInline):
    model = Option.machines.through
    extra = 1


class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'nom_en')
    search_fields = ['nom', 'nom_en']
    ordering       = ('nom', )


class FournisseurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'telephonne', 'fax', 'siteweb', 'devise', 'ratio', 'ratio_us', 'actif')
    list_filter = ('devise',)
    ordering = ('nom',)


class MachineAdmin(admin.ModelAdmin):
    list_display   = ('numero', 'description', 'categorie', 'fournisseur', 'prix_fournisseur', 'prixCAD_f', 'dateprix',
                      'escompte', 'costCAD_f', 'ratioEffectif', 'pl_f', 'ratioEffectifUs', 'plUS_f', 'profit_f',
                      'profitUS_f', 'profit_pourcent_f', 'profitUS_pourcent_f', 'actif')
    search_fields = ['numero', 'description']
    list_filter    = ('categorie', 'fournisseur')
    ordering       = ('-actif', 'numero', '-categorie',)
    inlines = [
        MachinerieInline,
    ]

    def prixCAD_f(self, obj):
        return "%.2f" % obj.prixCAD()
    prixCAD_f.short_description = 'Prix ($CA)'

    def costCAD_f(self, obj):
        return "%.2f" % obj.cost()
    costCAD_f.short_description = 'Cost ($CA)'

    def pl_f(self, obj):
        return "%.2f" % obj.plMin()
    pl_f.short_description = 'PL ($CA)'

    def plUS_f(self, obj):
        return "%.2f" % obj.plMinUS()
    plUS_f.short_description = 'PL (US$)'

    def profit_f(self, obj):
        return "%.2f" % obj.profit()
    profit_f.short_description = 'Profit ($CA)'

    def profit_pourcent_f(self, obj):
        return "%.2f" % obj.profit_pourcent()
    profit_pourcent_f.short_description = 'Profit (% Brute)'

    def profitUS_f(self, obj):
        return "%.2f" % obj.profitUs()
    profitUS_f.short_description = 'Profit US ($CA)'

    def profitUS_pourcent_f(self, obj):
        return "%.2f" % obj.profit_pourcentUs()
    profitUS_pourcent_f.short_description = 'Profit US (% Brute)'


class OptionAdmin(admin.ModelAdmin):
    actions = None
    list_display   = ('numero', 'description', 'fournisseur', 'prix_fournisseur', 'prixCAD', 'dateprix', 'escompte',
                      'cost', 'ratioEffectif', 'plMin', 'profit', 'profit_pourcent')
    search_fields = ['numero', 'description']
    list_filter    = ('fournisseur',)
    ordering       = ('numero', )
    inlines = [
        MachinerieInline,
    ]
    exclude = ('machines',)
    
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Machine, MachineAdmin)
admin.site.register(Fournisseur, FournisseurAdmin)