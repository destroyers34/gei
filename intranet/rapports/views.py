from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.db.models import Sum, Avg
from django.contrib.auth.decorators import permission_required, login_required
from decimal import *
import csv
from datetime import time, datetime
from clients.models import Compagnie
from projets.models import Projet_Eugenie

@permission_required('feuilles_de_temps.afficher_rapport_temps_eugenie')    
def liste_clients_eci(request):
    liste_clients = Compagnie.objects.values('id','nom').order_by('nom')
    for client in liste_clients:
        liste_projets = Projet_Eugenie.objects.filter(client=client['id']).order_by('numero')
        client.update({'liste_projets' : liste_projets})
    return render(request, 'rapports/liste_clients.html', {'liste_clients':liste_clients})

@permission_required('feuilles_de_temps.afficher_rapport_temps_eugenie')    
def print_liste_clients_eci(request):
    liste_clients = Compagnie.objects.values('id','nom').order_by('nom')
    for client in liste_clients:
        liste_projets = Projet_Eugenie.objects.filter(client=client['id']).order_by('numero')
        client.update({'liste_projets' : liste_projets})
    return render(request, 'rapports/print_liste_clients.html', {'liste_clients':liste_clients})

@permission_required('feuilles_de_temps.afficher_rapport_temps_eugenie')    
def xls_liste_clients_eci(request):
    liste_clients = Compagnie.objects.values('id','nom').order_by('nom')
    for client in liste_clients:
        liste_projets = Projet_Eugenie.objects.filter(client=client['id']).order_by('numero')
        client.update({'liste_projets' : liste_projets})
    response = render_to_response("rapports/xls_liste_clients.html", {'liste_clients':liste_clients})
    filename = "Liste des projets par client %s.xls" % (datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response    