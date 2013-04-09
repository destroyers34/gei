from django.contrib import admin
from employe.models import *
from django.contrib.auth.models import User

class EmployeAdmin(admin.ModelAdmin):
    list_display = ('__unicode__','user','compagnie','hire_date','banque_heure')

class CompagnieAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    
admin.site.register(Compagnie, CompagnieAdmin)    
admin.site.register(Employe, EmployeAdmin)


