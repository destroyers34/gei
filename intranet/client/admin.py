from django.contrib import admin
from client.models import *

class ClientAdmin(admin.ModelAdmin):
    list_display = ('compagnie','adresse','ville','province_etat','postal_code','pays','telephonne','fax')
    list_filter = ('ville','province_etat','pays')

admin.site.register(Client, ClientAdmin)
