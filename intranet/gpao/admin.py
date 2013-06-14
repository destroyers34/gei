# admin.py
from django.contrib import admin
from gpao.models import Nm, LienNM

class LienNMInline(admin.TabularInline):
    model = LienNM
    fk_name = 'from_nm'
    extra = 0

class NmAdmin(admin.ModelAdmin):
    inlines = [LienNMInline]
    list_display = ('reference','designation','categorie',)
    list_filter    = ('categorie',)
    
admin.site.register(Nm, NmAdmin)