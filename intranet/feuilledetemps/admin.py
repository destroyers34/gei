from django.contrib import admin
from feuilledetemps.models import *

class BlocAdmin(admin.ModelAdmin):
    list_display = ('employe','get_Name', 'date', 'projet', 'tache', 'temps', 'note')
    list_filter = ('employe','date', 'projet', 'tache')

class TacheAdmin(admin.ModelAdmin):
    list_display = ('numero', 'description')
    list_filter = ('numero', 'description')    
    
class BlocBanqueAdmin(admin.ModelAdmin):
    list_display = ('employe', 'date', 'projet', 'tache', 'temps', 'note')
    list_filter = ('employe','date', 'projet', 'tache')
    
admin.site.register(Tache, TacheAdmin)
admin.site.register(Bloc, BlocAdmin)
admin.site.register(Bloc_Banque, BlocBanqueAdmin)

