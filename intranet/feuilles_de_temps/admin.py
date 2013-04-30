from django.contrib import admin
from feuilles_de_temps.models import Bloc_Eugenie, Bloc_TPE, Banque

class BlocEugenieAdmin(admin.ModelAdmin):
    list_display = ('employe','get_Name', 'date', 'projet', 'tache', 'temps', 'note')
    list_filter = ('employe','date', 'projet', 'tache')
    search_fields = ['employe','projet', 'date', 'tache']
    ordering = ('-date',)

class BlocTPEAdmin(admin.ModelAdmin):
    list_display = ('employe','get_Name', 'date', 'projet', 'tache', 'temps', 'note')
    list_filter = ('employe','date', 'projet', 'tache')
    search_fields = ['employe','projet', 'date', 'tache']
    ordering = ('-date',)
    
class BanqueAdmin(admin.ModelAdmin):
    list_display = ('employe', 'date', 'temps')
    list_filter = ('employe','date')
    search_fields = ['employe','date']
    ordering = ('-date',)
    
admin.site.register(Bloc_TPE, BlocTPEAdmin)
admin.site.register(Bloc_Eugenie, BlocEugenieAdmin)
admin.site.register(Banque, BanqueAdmin)

