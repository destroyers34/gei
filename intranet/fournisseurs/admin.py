from django.contrib import admin
from fournisseurs.models import *


class FournisseurAdmin(admin.ModelAdmin):
   list_display   = ('nom', 'telephonne', 'fax', 'devise', 'ratio')
   list_filter    = ('nom', 'devise', 'ratio',)
   ordering       = ('nom', )
   
class DeviseAdmin(admin.ModelAdmin):
   list_display   = ('nom', 'codeiso', 'symbole', 'taux', 'date')
   list_filter    = ('nom', 'codeiso', 'date',)
   ordering       = ('nom', 'codeiso', )

admin.site.register(Fournisseur, FournisseurAdmin)
admin.site.register(Devise, DeviseAdmin)