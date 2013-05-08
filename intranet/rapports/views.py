from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.db.models import Sum, Avg
from django.contrib.auth.decorators import permission_required, login_required
from decimal import *
import csv
from datetime import time, datetime
from clients.models import Compagnie
from projets.models import Projet_Eugenie
from feuilles_de_temps.models import Bloc_Eugenie
from ressources.models import Tache, Employe
from rapports.forms import FilterForm, DateRangeForm

@permission_required('feuilles_de_temps.afficher_rapport_temps_eugenie')    
def base_liste_clients_eci(request):
    liste_clients = Compagnie.objects.values('id','nom').order_by('nom')
    for client in liste_clients:
        liste_projets = Projet_Eugenie.objects.filter(client=client['id']).order_by('numero')
        client.update({'liste_projets' : liste_projets})
    return {'liste_clients': liste_clients}
    
@permission_required('feuilles_de_temps.afficher_rapport_temps_eugenie')    
def base_client_details_eci(request, client_id):
    client = Compagnie.objects.get(id=client_id)
    liste_projets = list()
    for projet in client.projet_eugenie_set.all():
        heures = Bloc_Eugenie.objects.filter(projet=projet).aggregate(total=Sum('temps'))
        liste_projets.append({'projet':projet,'heures':heures})
    return {'client':client,'liste_projets':liste_projets}

@permission_required('feuilledetemps.afficher_rapport_temps')
def base_liste_projets_eci(request):
    projets = Projet_Eugenie.objects.all()
    projets_attente = projets.filter(actif=True,en_attente=True)
    projets_actif = projets.filter(actif=True,en_attente=False).annotate(heure=Sum('bloc_eugenie__temps')).order_by('numero')
    projets_inactif = projets.filter(actif=False,en_attente=False).annotate(heure=Sum('bloc_eugenie__temps')).order_by('numero')
    total_attente = projets.filter(actif=True,en_attente=True).aggregate(total_mat=Sum('budget_mat'),total_mo=Sum('budget_mo'))
    total_actif = projets.filter(actif=True,en_attente=False).aggregate(total_mat=Sum('budget_mat'),total_mo=Sum('budget_mo'))
    total_inactif = projets.filter(actif=False,en_attente=False).aggregate(total_heure=Sum('bloc_eugenie__temps'))
    heures = projets.filter(actif=True,en_attente=False).aggregate(total_heure=Sum('bloc_eugenie__temps'))
    total_actif.update({'total_heure':heures['total_heure']})
    total_actif.update({'jours_travail': format((total_actif['total_mo'] - heures['total_heure'])/8, '.2f')})
    if total_actif['total_heure']:
        if total_actif['total_mo'] > 0:
            total_actif.update({'total_pourcent':format(total_actif['total_heure']/total_actif['total_mo']*100, '.2f')})
        else:
            total_actif.update({'total_pourcent':format(total_actif['total_heure']*100, '.2f')})
    else:
        total_actif.update({'total_pourcent':0 })
    return {'projets_attente':projets_attente,'projets_actif':projets_actif,'projets_inactif':projets_inactif,'total_attente':total_attente,'total_actif':total_actif,'total_inactif':total_inactif}

@permission_required('feuilledetemps.afficher_rapport_temps')
def base_liste_taches_eci(request):
    taches = Tache.objects.all().annotate(heure=Sum('bloc_eugenie__temps')).order_by('numero')
    total = Tache.objects.all().aggregate(heures=Sum('bloc_eugenie__temps'))
    return {'taches':taches,'total':total}
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def base_liste_employes_eci(request):
    employes = Employe.objects.all().annotate(heure=Sum('bloc_eugenie__temps')).order_by('user__first_name')
    employes_actif = employes.filter(user__is_active=True)
    employes_inactif = employes.filter(user__is_active=False)   
    total_actif = Employe.objects.filter(user__is_active=True).aggregate(heures=Sum('bloc_eugenie__temps'), banque=Sum('banque_heure'))
    total_inactif = Employe.objects.filter(user__is_active=False).aggregate(heures=Sum('bloc_eugenie__temps'), banque=Sum('banque_heure'))
    return {'employes_actif':employes_actif,'total_actif':total_actif,'employes_inactif':employes_inactif,'total_inactif':total_inactif}
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def base_projet_details_eci(request, numero_projet):
    taches = Tache.objects.filter(bloc_eugenie__projet__numero=numero_projet).annotate(heure=Sum('bloc_eugenie__temps')).order_by('numero')
    projet_total = Projet_Eugenie.objects.filter(numero=numero_projet).aggregate(heures=Sum('bloc_eugenie__temps'))
    return {'taches':taches,'projet_total':projet_total,'numero_projet':numero_projet}

@permission_required('feuilledetemps.afficher_rapport_temps')
def base_tache_details_eci(request, numero_tache):
    projets = Projet_Eugenie.objects.filter(bloc_eugenie__tache__numero=numero_tache).annotate(heure=Sum('bloc_eugenie__temps')).order_by('-numero')
    tache_total = Tache.objects.filter(numero=numero_tache).aggregate(heures=Sum('bloc_eugenie__temps'))
    return {'projets':projets,'tache_total':tache_total,'numero_tache':numero_tache}

@permission_required('feuilledetemps.afficher_rapport_temps')
def base_liste_projets_noms_eci(request, nom_projet):
    modeles = Projet_Eugenie.objects.filter(nom=nom_projet).values('modele').annotate(heure=Sum('bloc_eugenie__temps')).order_by('modele')
    modeles_total = Projet_Eugenie.objects.filter(nom=nom_projet).aggregate(heures=Sum('bloc_eugenie__temps'))
    for modele in modeles:
        liste_projets = Projet_Eugenie.objects.filter(nom=nom_projet,modele=modele['modele']).annotate(heure=Sum('bloc_eugenie__temps')).order_by('numero')
        liste_heures = list()
        for projet in liste_projets:
            if projet.heure is not None:
                liste_heures.append(projet.heure)
        if len(liste_heures)>0 :
            moyenne = format(reduce(lambda x, y: x + y, liste_heures) / len(liste_heures), '.2f')
            modele.update({'liste_projets':liste_projets,'moyenne':moyenne})
    return {'modeles':modeles,'modeles_total':modeles_total,'nom_projet':nom_projet}

@permission_required('feuilledetemps.afficher_rapport_temps')
def base_liste_projets_modeles_eci(request, nom_projet, modele_projet):
    projets = Projet_Eugenie.objects.filter(nom=nom_projet,modele=modele_projet).values('numero').annotate(heure=Sum('bloc_eugenie__temps')).order_by('numero')
    projets_total = Projet_Eugenie.objects.filter(nom=nom_projet,modele=modele_projet).aggregate(heures=Sum('bloc_eugenie__temps'))
    liste_temps_projet = list()
    for projet in projets:
        liste_temps_projet.append(projet['heure'])
        liste_taches = Tache.objects.filter(bloc_eugenie__projet__nom=nom_projet,bloc_eugenie__projet__modele=modele_projet,bloc_eugenie__projet__numero=projet['numero']).annotate(heure=Sum('bloc_eugenie__temps')).order_by('numero')
        projet.update({'liste_taches' : liste_taches})
    moyenne = format(reduce(lambda x, y: x + y, liste_temps_projet) / len(liste_temps_projet), '.2f')
    return {'projets':projets,'projets_total':projets_total,'nom_projet':nom_projet,'modele_projet':modele_projet,'moyenne':moyenne}

@permission_required('feuilledetemps.afficher_rapport_temps')
def base_rapport_complet_eci(request, numero_projet):
    projet = Projet_Eugenie.objects.get(numero=numero_projet)
    total_projet = Projet_Eugenie.objects.filter(numero=numero_projet).aggregate(heures=Sum('bloc_eugenie__temps'))
    liste_taches = Tache.objects.filter(bloc_eugenie__projet=projet).order_by('numero','bloc_eugenie__date','bloc_eugenie__employe').values('numero','description','bloc_eugenie__employe__user__first_name','bloc_eugenie__employe__user__last_name').annotate(total_employe=Sum('bloc_eugenie__temps'))
    total_tache = liste_taches.values('numero','description').annotate(heures=Sum('bloc_eugenie__temps')).order_by('numero')
    return {'projet':projet,'total_projet':total_projet,'liste_taches':liste_taches,'total_tache':total_tache,'pourcent':format(total_projet['heures']/projet.budget_mo*100, '.2f')}

@permission_required('feuilledetemps.afficher_rapport_temps')
def base_employe_details_eci(request, username):
    employe = Employe.objects.get(user__username=username)
    projets = Projet_Eugenie.objects.filter(bloc_eugenie__employe=employe).values('numero','nom','modele').annotate(heure=Sum('bloc_eugenie__temps')).order_by('numero')
    total_projet = Projet_Eugenie.objects.filter(bloc_eugenie__employe=employe).aggregate(heures=Sum('bloc_eugenie__temps'))
    projets = list(projets)
    for projet in projets:
        taches = Tache.objects.filter(bloc_eugenie__employe=employe,bloc_eugenie__projet__numero=projet['numero']).values('numero', 'description').annotate(heure=Sum('bloc_eugenie__temps')).order_by('numero')
        projet.update({'taches' : taches})
    return {'employe':employe,'projets':projets,'total_projet':total_projet}
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def base_projet_tache_details_eci(request, numero_projet, numero_tache):
    projet = Projet_Eugenie.objects.get(numero=numero_projet)
    tache = Tache.objects.get(numero=numero_tache)
    employes = Employe.objects.filter(bloc_eugenie__projet=projet,bloc_eugenie__tache=tache).annotate(heure=Sum('bloc_eugenie__temps')).order_by('user__first_name')
    total_employe = Employe.objects.filter(bloc_eugenie__projet=projet,bloc_eugenie__tache=tache).aggregate(heures=Sum('bloc_eugenie__temps'))
    return {'projet':projet,'tache':tache,'employes':employes,'total_employe':total_employe}
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def base_employe_blocs_eci(request, username):
    blocs = Bloc_Eugenie.objects.filter(employe__user__username=username).order_by('date')
    total_bloc = Bloc_Eugenie.objects.filter(employe__user__username=username).aggregate(heures=Sum('temps'))
    return {'blocs':blocs,'total_bloc':total_bloc}
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def base_employe_blocs_periode_eci(request, username, date_debut, date_fin):
    blocs = Bloc_Eugenie.objects.filter(employe__user__username=username,date__gte=date_debut,date__lte=date_fin).order_by('date')
    total_bloc = Bloc_Eugenie.objects.filter(employe__user__username=username,date__gte=date_debut,date__lte=date_fin).aggregate(heures=Sum('temps'))
    return {'blocs':blocs,'total_bloc':total_bloc}
    
@permission_required('feuilles_de_temps.afficher_rapport_temps_eugenie')    
def liste_clients_eci(request):
    return render(request, 'rapports/liste_clients_eci.html', base_liste_clients_eci(request))
    
@permission_required('feuilles_de_temps.afficher_rapport_temps_eugenie')    
def client_details_eci(request, client_id):
    return render(request, 'rapports/client_details_eci.html', base_client_details_eci(request, client_id))

@permission_required('feuilledetemps.afficher_rapport_temps')
def liste_projets_eci(request):
    variables = base_liste_projets_eci(request)
    if request.method == 'POST':
        form = FilterForm(request.POST)
        if form.is_valid():
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            projet = form.cleaned_data['projet']
            redirect_str = str(projet.numero) + '/' + str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else: 
        form = FilterForm()
    variables.update({'form':form,'date':datetime.now().strftime("%Y-%m-%d")})
    return render(request, 'rapports/liste_projets_eci.html', variables)
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def liste_taches_eci(request):
    return render(request, 'rapports/liste_taches_eci.html', base_liste_taches_eci(request))
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def liste_employes_eci(request):
    return render(request, 'rapports/liste_employes_eci.html', base_liste_employes_eci(request))
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def projet_details_eci(request, numero_projet):
    variables = base_projet_details_eci(request, numero_projet)
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else: 
        form = DateRangeForm()
    variables.update({'form':form,'date':datetime.now().strftime("%Y-%m-%d")})
    return render(request, 'rapports/projet_details_eci.html', variables)
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def tache_details_eci(request, numero_tache):
    variables = base_tache_details_eci(request, numero_tache)
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else: 
        form = DateRangeForm()
    variables.update({'form':form,'date':datetime.now().strftime("%Y-%m-%d")})
    return render(request, 'rapports/tache_details_eci.html', variables)    

@permission_required('feuilledetemps.afficher_rapport_temps')
def liste_projets_noms_eci(request, nom_projet):
    return render(request, 'rapports/liste_projets_noms_eci.html', base_liste_projets_noms_eci(request, nom_projet))
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def liste_projets_modeles_eci(request, nom_projet, modele_projet):
    return render(request, 'rapports/liste_projets_modeles_eci.html', base_liste_projets_modeles_eci(request, nom_projet, modele_projet))

@permission_required('feuilledetemps.afficher_rapport_temps')
def rapport_complet_eci(request, numero_projet):
    return render(request, 'rapports/rapport_complet_eci.html', base_rapport_complet_eci(request, numero_projet))

@permission_required('feuilledetemps.afficher_rapport_temps')
def employe_details_eci(request, username):
    return render(request, 'rapports/employe_details_eci.html', base_employe_details_eci(request, username))

@permission_required('feuilledetemps.afficher_rapport_temps')
def projet_tache_details_eci(request, numero_projet, numero_tache):
    return render(request, 'rapports/projet_tache_details_eci.html', base_projet_tache_details_eci(request, numero_projet, numero_tache))

@permission_required('feuilledetemps.afficher_rapport_temps')
def employe_blocs_eci(request, username):
    variables = base_employe_blocs_eci(request, username)
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else: 
        form = DateRangeForm()
    variables.update({'form':form,'date':datetime.now().strftime("%Y-%m-%d")})
    return render(request, 'rapports/employe_blocs_eci.html', variables)
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def employe_blocs_periode_eci(request, username, date_debut, date_fin):
    variables = base_employe_blocs_periode_eci(request, username, date_debut, date_fin)
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = '../../' + str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else: 
        form = DateRangeForm()
    variables.update({'form':form,'date':datetime.now().strftime("%Y-%m-%d")})
    return render(request, 'rapports/employe_blocs_eci.html', variables)

    
@permission_required('feuilles_de_temps.afficher_rapport_temps_eugenie')    
def print_liste_clients_eci(request):
    return render(request, 'rapports/print_liste_clients_eci.html', base_liste_clients_eci(request))

@permission_required('feuilles_de_temps.afficher_rapport_temps_eugenie')    
def print_client_details_eci(request, client_id):
    return render(request, 'rapports/print_client_details_eci.html', base_client_details_eci(request, client_id))    

@permission_required('feuilledetemps.afficher_rapport_temps')
def print_liste_projets_eci(request):
    return render(request, 'rapports/print_liste_projets_eci.html', base_liste_projets_eci(request))    

@permission_required('feuilledetemps.afficher_rapport_temps')
def print_liste_taches_eci(request):
    return render(request, 'rapports/print_liste_taches_eci.html', base_liste_taches_eci(request))    
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def print_liste_employes_eci(request):
    return render(request, 'rapports/print_liste_employes_eci.html', base_liste_employes_eci(request))   
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def print_projet_details_eci(request, numero_projet):
    return render(request, 'rapports/print_projet_details_eci.html', base_projet_details_eci(request, numero_projet))

@permission_required('feuilledetemps.afficher_rapport_temps')
def print_tache_details_eci(request, numero_tache):
    return render(request, 'rapports/print_tache_details_eci.html', base_tache_details_eci(request, numero_tache))

@permission_required('feuilledetemps.afficher_rapport_temps')
def print_liste_projets_noms_eci(request, nom_projet):      
    return render(request, 'rapports/print_liste_projets_noms_eci.html', base_liste_projets_noms_eci(request, nom_projet))

@permission_required('feuilledetemps.afficher_rapport_temps')
def print_liste_projets_modeles_eci(request, nom_projet, modele_projet):
    return render(request, 'rapports/print_liste_projets_modeles_eci.html', base_liste_projets_modeles_eci(request, nom_projet, modele_projet))
      
@permission_required('feuilledetemps.afficher_rapport_temps')
def print_rapport_complet_eci(request, numero_projet):
    return render(request, 'rapports/print_rapport_complet_eci.html', base_rapport_complet_eci(request, numero_projet))

@permission_required('feuilledetemps.afficher_rapport_temps')
def print_employe_details_eci(request, username):
    return render(request, 'rapports/print_employe_details_eci.html', base_employe_details_eci(request, username))

@permission_required('feuilledetemps.afficher_rapport_temps')
def print_projet_tache_details_eci(request, numero_projet, numero_tache):
    return render(request, 'rapports/print_projet_tache_details_eci.html', base_projet_tache_details_eci(request, numero_projet, numero_tache))    

@permission_required('feuilledetemps.afficher_rapport_temps')
def print_employe_blocs_eci(request, username):    
    return render(request, 'rapports/print_employe_blocs_eci.html', base_employe_blocs_eci(request, username))

@permission_required('feuilledetemps.afficher_rapport_temps')
def print_employe_blocs_periode_eci(request, username, date_debut, date_fin):    
    return render(request, 'rapports/print_employe_blocs_eci.html', base_employe_blocs_periode_eci(request, username, date_debut, date_fin))    
    
    
@permission_required('feuilles_de_temps.afficher_rapport_temps_eugenie')    
def xls_liste_clients_eci(request):
    response = render_to_response("rapports/xls_liste_clients_eci.html", base_liste_clients_eci(request))
    filename = "Liste des projets par client pour EuGénie Canada Inc %s.xls" % (datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response

@permission_required('feuilles_de_temps.afficher_rapport_temps_eugenie')    
def xls_client_details_eci(request, client_id):
    client = Compagnie.objects.get(id=client_id)
    response = render_to_response("rapports/xls_client_details_eci.html", base_client_details_eci(request, client_id))
    filename = "Rapport des projets %s %s.xls" % (client.nom,datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
def xls_liste_projets_eci(request):    
    response = render_to_response('rapports/xls_liste_projets_eci.html', base_liste_projets_eci(request))
    filename = "Liste des projets EuGénie Canada %s.xls" % datetime.now().strftime("%Y-%m-%d")
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def xls_liste_taches_eci(request):    
    response = render_to_response("rapports/xls_liste_taches_eci.html", base_liste_taches_eci(request))
    filename = "Liste des tâches EuGénie Canada %s.xls" % datetime.now().strftime("%Y-%m-%d")
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def xls_liste_employes_eci(request):     
    response = render_to_response('rapports/xls_liste_employes_eci.html', base_liste_employes_eci(request))
    filename = "Liste des employés EuGénie Canada %s.xls" % (datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def xls_projet_details_eci(request, numero_projet):
    response = render_to_response('rapports/xls_projet_details_eci.html', base_projet_details_eci(request, numero_projet))
    filename = "Details du projet %s - %s.xls" % (numero_projet, datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response

@permission_required('feuilledetemps.afficher_rapport_temps')
def xls_tache_details_eci(request, numero_tache):    
    response = render_to_response("rapports/xls_tache_details_eci.html", base_tache_details_eci(request, numero_tache))
    filename = "Details de la tache %s - %s.xls" % (numero_tache, datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def xls_liste_projets_noms_eci(request, nom_projet):  
    response = render_to_response("rapports/xls_liste_projets_noms_eci.html", base_liste_projets_noms_eci(request, nom_projet))
    filename = "Liste des modeles %s - %s.xls" % (nom_projet,datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def xls_liste_projets_modeles_eci(request, nom_projet, modele_projet):
    response = render_to_response("rapports/xls_liste_projets_modeles_eci.html", base_liste_projets_modeles_eci(request, nom_projet, modele_projet))
    filename = "Liste des projets %s %s - %s.xls" % (nom_projet,modele_projet,datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def xls_rapport_complet_eci(request, numero_projet):
    response = render_to_response('rapports/xls_rapport_complet_eci.html', base_rapport_complet_eci(request, numero_projet))
    filename = "Rapport complet du projet %s - %s.xls" % (numero_projet,datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def xls_employe_details_eci(request, username):
    response = render_to_response('rapports/xls_employe_details_eci.html', base_employe_details_eci(request, username))
    filename = "Rapport de l'employe %s - %s.xls" % (username, datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def xls_projet_tache_details_eci(request, numero_projet, numero_tache):
    response = render_to_response('rapports/xls_projet_tache_details_eci.html', base_projet_tache_details_eci(request, numero_projet, numero_tache))
    filename = "Rapport details %s - %s - %s.xls" % (numero_projet, numero_tache, datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def xls_employe_blocs_eci(request, username):    
    response = render_to_response('rapports/xls_employe_blocs_eci.html', base_employe_blocs_eci(request, username))
    filename = "Liste des blocs de %s - %s.xls" % (username,datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def xls_employe_blocs_periode_eci(request, username, date_debut, date_fin):    
    response = render_to_response('rapports/xls_employe_blocs_eci.html', base_employe_blocs_periode_eci(request, username, date_debut, date_fin))
    filename = "Liste des blocs de %s - %s.xls" % (username,datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response