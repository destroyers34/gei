from django.contrib import admin
from ressources.models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


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


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeInline(admin.TabularInline):
    model = Employe
    max_num = 1
    can_delete = False


# Define a new User admin
class UserAdmin(AuthUserAdmin):
    def compagnie(self, instance):
        return instance.get_profile().compagnie
    compagnie.short_description = 'Compagnie'

    def hire_date(self, instance):
        return instance.get_profile().hire_date
    hire_date.short_description = 'Date d\'embauche'

    def banque_heure(self, instance):
        return instance.get_profile().banque_heure
    banque_heure.short_description = 'Banque d\'heure'
    ordering = ['-is_active', 'first_name', ]
    inlines = [EmployeInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'compagnie', 'banque_heure', 'hire_date',
                    'is_staff', 'is_active')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email')}),
    )

# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, UserAdmin)

admin.site.register(Compagnie, CompagnieAdmin)
admin.site.register(Devise, DeviseAdmin)
admin.site.register(Tache, TacheAdmin)

