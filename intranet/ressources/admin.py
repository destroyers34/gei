from django.contrib import admin
from ressources.models import *
from django.contrib.auth.models import User

class EmployeAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','user','compagnie','hire_date','banque_heure')
    ordering = ('user',)
    list_filter = ('compagnie',)
    search_fields = ['user','hire_date']
    
class CompagnieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    ordering = ('nom',)

class DeviseAdmin(admin.ModelAdmin):
   list_display   = ('nom', 'code_iso', 'symbole', 'taux_toCAD', 'taux_inverse', 'date_taux')
   ordering       = ('nom', 'code_iso', )
   search_fields = ['nom', 'code_iso']  
   
class TacheAdmin(admin.ModelAdmin):
    list_display = ('numero', 'description')
    search_fields = ['numero', 'description']  
    
admin.site.register(Compagnie, CompagnieAdmin)    
admin.site.register(Employe, EmployeAdmin)
admin.site.register(Devise, DeviseAdmin)
admin.site.register(Tache, TacheAdmin)

