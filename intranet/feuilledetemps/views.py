from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.db.models import Sum, Avg
from django.contrib.auth.decorators import permission_required, login_required
from django.forms.models import modelformset_factory
from decimal import *  
import csv
from datetime import time, datetime
from feuilledetemps.forms import *
from feuilledetemps.models import *
from client.models import Client
from projet.models import Projet

@login_required
def index(request):
    date = datetime.now().strftime("%Y-%m-%d")
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else: 
        form = DateRangeForm()
    return render(request, 'feuilledetemps/rapports.html', {'form':form,'date':date})

@permission_required('feuilledetemps.add_bloc')    
def add_blocs(request):
    BlocFormSet = modelformset_factory(Bloc, form=BlocForm)
    if request.method == 'POST':
        formset = BlocFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("success")
    else:
        formset = BlocFormSet(queryset=Projet.objects.none())
    return render(request,"feuilledetemps/add_blocs.html", {"formset": formset,})

@login_required    
def add_blocs_success(request):
    return render(request,"feuilledetemps/add_blocs_success.html")    

@permission_required('feuilledetemps.add_bloc_banque')    
def add_blocs_banque(request):
    Bloc_BanqueFormSet = modelformset_factory(Bloc_Banque, form=Bloc_BanqueForm)
    if request.method == 'POST':
        formset = Bloc_BanqueFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("success")
    else:
        formset = Bloc_BanqueFormSet(queryset=Projet.objects.none())
    return render(request,"feuilledetemps/add_blocs_banque.html", {"formset": formset,})

@login_required    
def add_blocs_banque_success(request):
    return render(request,"feuilledetemps/add_blocs_banque_success.html")     
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def listerapports(request):
    rapport = Bloc.objects.values('projet__numero', 'projet__nom','projet__modele','projet__client__compagnie','projet__client__id','projet__budget_mat','projet__budget_mo','projet__date_debut','projet__date_fin').annotate(heure=Sum('temps')).order_by('projet__numero')
    rapport_actif =  rapport.filter(projet__actif=True)
    total_actif = Bloc.objects.filter(projet__actif=True).aggregate(total=Sum('temps'))
    total_budget_actif = Projet.objects.raw("SELECT x.id, sum(x.somme_mat) as 'total_budget_mat', sum(x.somme_mo) as 'total_budget_mo' FROM (SELECT DISTINCT p.id, p.numero, sum(p.budget_mat) as 'somme_mat', sum(p.budget_mo) as 'somme_mo' FROM feuilledetemps_bloc as b INNER JOIN projet_projet as p on p.id = b.projet_id WHERE p.actif = True GROUP BY b.id) as x")
    total_pourcent = format(total_actif['total']/total_budget_actif[0].total_budget_mo*100, '.2f')
    total_actif.update({'jours_travail' : format((total_budget_actif[0].total_budget_mo - total_actif['total'])/8, '.2f')})
    rapport_inactif =  rapport.filter(projet__actif=False)
    total_inactif = Bloc.objects.filter(projet__actif=False).aggregate(total=Sum('temps'))
    date = datetime.now().strftime("%Y-%m-%d")
    projets = Projet.objects.filter(actif=True).order_by('numero')
    projets_attente = {}
    projets_liste = list()
    total_mat = 0
    total_mo = 0
    for projet in projets:
        if projet.bloc_set.count() == 0:
            projets_liste.append(projet)
            total_mat += projet.budget_mat
            total_mo += projet.budget_mo
    projets_attente.update({'projets':projets_liste, 'total_mat':total_mat, 'total_mo':total_mo})
    for b in rapport_actif:
        date_fin = b['projet__date_fin']
        if date_fin is not None:
            jours_restant = (date_fin - datetime.now().date()).days
        else:
            jours_restant = "Indéterminé"
        b.update({'pourcent' : format(b['heure']/b['projet__budget_mo']*100, '.2f'), 'jours_restant':jours_restant})
    for b in rapport_inactif:
        b.update({'pourcent' : format(b['heure']/b['projet__budget_mo']*100, '.2f')})
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
    return render(request, 'feuilledetemps/listerapports.html', {'rapport_actif': rapport_actif, 'total_actif': total_actif,'rapport_inactif': rapport_inactif, 'total_inactif': total_inactif, 'date':date, 'form':form,'total_budget_actif':total_budget_actif, 'total_pourcent':total_pourcent, 'projets_attente':projets_attente})

@permission_required('feuilledetemps.afficher_rapport_temps')
def listerapports_csv(request):
    rapport_actif = Bloc.objects.filter(projet__actif=True).values('projet__numero', 'projet__nom','projet__modele','projet__client__compagnie','projet__client__id','projet__budget_mat','projet__budget_mo','projet__date_debut','projet__date_fin').annotate(heure=Sum('temps')).order_by('projet__numero')
    total_actif = Bloc.objects.filter(projet__actif=True).aggregate(total=Sum('temps'))
    total_budget_actif = Projet.objects.raw("SELECT x.id, sum(x.somme_mat) as 'total_budget_mat', sum(x.somme_mo) as 'total_budget_mo' FROM (SELECT DISTINCT p.id, p.numero, sum(p.budget_mat) as 'somme_mat', sum(p.budget_mo) as 'somme_mo' FROM feuilledetemps_bloc as b INNER JOIN projet_projet as p on p.id = b.projet_id WHERE p.actif = True GROUP BY b.id) as x")
    total_pourcent = format(total_actif['total']/total_budget_actif[0].total_budget_mo*100, '.2f')
    total_actif.update({'jours_travail' : format((total_budget_actif[0].total_budget_mo - total_actif['total'])/8, '.2f')})
    date = datetime.now().strftime("%Y-%m-%d")
    projets = Projet.objects.filter(actif=True).order_by('numero')
    projets_attente = {}
    projets_liste = list()
    total_mat = 0
    total_mo = 0
    for projet in projets:
        if projet.bloc_set.count() == 0:
            projets_liste.append(projet)
            total_mat += projet.budget_mat
            total_mo += projet.budget_mo
    projets_attente.update({'projets':projets_liste, 'total_mat':total_mat, 'total_mo':total_mo})
    for b in rapport_actif:
        date_fin = b['projet__date_fin']
        if date_fin is not None:
            jours_restant = (date_fin - datetime.now().date()).days
        else:
            jours_restant = "Indéterminé"
        b.update({'pourcent' : format(b['heure']/b['projet__budget_mo']*100, '.2f'), 'jours_restant':jours_restant})
    # Create the HttpResponse object with the appropriate CSV header.
    response = render_to_response("feuilledetemps/listerapportscsv.html", {'rapport_actif': rapport_actif, 'total_actif': total_actif, 'date':date,'total_budget_actif':total_budget_actif, 'total_pourcent':total_pourcent, 'projets_attente':projets_attente})
    filename = "temps_par_Projet_%s.xls" % datetime.now().strftime("%Y-%m-%d")
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def listetaches(request):
    blocs = Bloc.objects.values('tache__numero', 'tache__description').annotate(heure=Sum('temps')).order_by('tache__numero')
    total = Bloc.objects.all().aggregate(total=Sum('temps'))
    return render(request, 'feuilledetemps/listetaches.html', {'blocs': blocs, 'total': total})
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def listetaches_csv(request):
    blocs = Bloc.objects.values('tache__numero', 'tache__description').annotate(heure=Sum('temps')).order_by('tache__numero')
    total = Bloc.objects.all().aggregate(total=Sum('temps'))
    # Create the HttpResponse object with the appropriate CSV header.
    response = render_to_response("feuilledetemps/listetachescsv.html", {'blocs': blocs, 'total': total})
    filename = "temps_par_tache_%s.xls" % datetime.now().strftime("%Y-%m-%d")
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def rapportdetail(request, numero_projet):
    rapport = Bloc.objects.filter(projet__numero=numero_projet).values('projet__numero', 'tache__numero', 'tache__description').annotate(heure=Sum('temps')).order_by('tache__numero')
    total = Bloc.objects.filter(projet__numero=numero_projet).aggregate(total=Sum('temps'))
    date = datetime.now().strftime("%Y-%m-%d")
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else: 
        form = DateRangeForm()
    return render(request, 'feuilledetemps/rapportdetail.html', {'rapport': rapport, 'total': total, 'date':date, 'form':form, 'numero_projet':numero_projet})  
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def rapportdetail_csv(request, numero_projet):
    rapport = Bloc.objects.filter(projet__numero=numero_projet).values('projet__numero', 'tache__numero', 'tache__description').annotate(heure=Sum('temps')).order_by('tache__numero')
    total = Bloc.objects.filter(projet__numero=numero_projet).aggregate(total=Sum('temps'))
    # Create the HttpResponse object with the appropriate CSV header.
    response = render_to_response("feuilledetemps/rapportdetailcsv.html", {'rapport': rapport, 'total': total})
    filename = "rapport_projet_%s_%s.xls" % (numero_projet, datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def projettemps(request, numero_projet, date_debut, date_fin):  
    blocs = Bloc.objects.filter(date__gte=date_debut,date__lte=date_fin,projet__numero=numero_projet).values('projet__numero', 'date', 'employe__user__username', 'employe__user__first_name', 'employe__user__last_name', 'tache__numero', 'tache__description', 'temps').order_by('date')
    total = Bloc.objects.filter(date__gte=date_debut,date__lte=date_fin,projet__numero=numero_projet).aggregate(total=Sum('temps'))
    date = datetime.now().strftime("%Y-%m-%d")
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = '../../' + str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else: 
        form = DateRangeForm()
    return render(request, 'feuilledetemps/employedetail.html', {'blocs': blocs, 'total': total, 'date':date, 'form':form})

@permission_required('feuilledetemps.afficher_rapport_temps')
def projettemps_csv(request, numero_projet, date_debut, date_fin):  
    blocs = Bloc.objects.filter(date__gte=date_debut,date__lte=date_fin,projet__numero=numero_projet).values('projet__numero', 'date', 'employe__user__first_name', 'employe__user__last_name', 'tache__numero', 'tache__description', 'temps').order_by('date')
    total = Bloc.objects.filter(date__gte=date_debut,date__lte=date_fin,projet__numero=numero_projet).aggregate(total=Sum('temps'))
    response = render_to_response("feuilledetemps/employedetail_csv.html", {'blocs': blocs, 'total': total, 'date_debut':date_debut, 'date_fin':date_fin})
    filename = "rapport_projet_%s_du_%s_au_%s.xls" % (numero_projet, date_debut, date_fin)
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def tachedetail(request, numero_tache):
    blocs = Bloc.objects.filter(tache__numero=numero_tache).values('tache__numero', 'tache__description', 'projet__numero','projet__nom','projet__modele').annotate(heure=Sum('temps')).order_by('-projet__numero')
    total = Bloc.objects.filter(tache__numero=numero_tache).all().aggregate(total=Sum('temps'))
    date = datetime.now().strftime("%Y-%m-%d")
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else: 
        form = DateRangeForm()
    return render(request, 'feuilledetemps/tachedetail.html', {'blocs': blocs, 'total': total, 'form':form, 'date':date, 'numero_tache':numero_tache})

@permission_required('feuilledetemps.afficher_rapport_temps')
def tachedetail_csv(request, numero_tache):
    blocs = Bloc.objects.filter(tache__numero=numero_tache).values('tache__numero', 'tache__description', 'projet__numero','projet__nom','projet__modele').annotate(heure=Sum('temps')).order_by('-projet__numero')
    total = Bloc.objects.filter(tache__numero=numero_tache).all().aggregate(total=Sum('temps'))
    # Create the HttpResponse object with the appropriate CSV header.
    response = render_to_response("feuilledetemps/tachedetailcsv.html", {'blocs': blocs, 'total': total})
    filename = "rapport_tache_%s_%s.xls" % (numero_tache, datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response

@permission_required('feuilledetemps.afficher_rapport_temps')
def tachetemps(request, numero_tache, date_debut, date_fin):  
    blocs = Bloc.objects.filter(date__gte=date_debut,date__lte=date_fin,tache__numero=numero_tache).values('projet__numero', 'date', 'employe__user__first_name', 'employe__user__last_name', 'tache__numero', 'tache__description', 'temps').order_by('date')
    total = Bloc.objects.filter(date__gte=date_debut,date__lte=date_fin,tache__numero=numero_tache).aggregate(total=Sum('temps'))
    date = datetime.now().strftime("%Y-%m-%d")
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = '../../' + str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else: 
        form = DateRangeForm()
    return render(request, 'feuilledetemps/employedetail.html', {'blocs': blocs, 'total': total, 'date':date, 'form':form, 'username':username})

@permission_required('feuilledetemps.afficher_rapport_temps')
def tachetemps_csv(request, numero_tache, date_debut, date_fin):  
    blocs = Bloc.objects.filter(date__gte=date_debut,date__lte=date_fin,tache__numero=numero_tache).values('projet__numero', 'date', 'employe__user__first_name', 'employe__user__last_name', 'tache__numero', 'tache__description', 'temps').order_by('date')
    total = Bloc.objects.filter(date__gte=date_debut,date__lte=date_fin,tache__numero=numero_tache).aggregate(total=Sum('temps'))
    response = render_to_response("feuilledetemps/employedetail_csv.html", {'blocs': blocs, 'total': total, 'date_debut':date_debut, 'date_fin':date_fin})
    filename = "rapport_tache_%s_du_%s_au_%s.xls" % (numero_tache, date_debut, date_fin)
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def projettachedetail(request, numero_tache, numero_projet):
    rapport = Bloc.objects.filter(tache__numero=numero_tache,projet__numero=numero_projet).values('projet__nom','projet__modele','tache__description','employe__user__username','employe__user__first_name','employe__user__last_name').annotate(heure=Sum('temps'))
    total = Bloc.objects.filter(tache__numero=numero_tache,projet__numero=numero_projet).aggregate(total=Sum('temps'))
    return render(request, 'feuilledetemps/projettachedetail.html', {'rapport': rapport, 'total': total, 'numero_tache': numero_tache, 'numero_projet': numero_projet})

@permission_required('feuilledetemps.afficher_rapport_temps')
def projettachedetailcsv(request, numero_tache, numero_projet):
    rapport = Bloc.objects.filter(tache__numero=numero_tache,projet__numero=numero_projet).values('projet__nom','projet__modele','tache__description','employe__user__first_name','employe__user__last_name').annotate(heure=Sum('temps'))
    total = Bloc.objects.filter(tache__numero=numero_tache,projet__numero=numero_projet).aggregate(total=Sum('temps'))
    # Create the HttpResponse object with the appropriate CSV header.
    response = render_to_response("feuilledetemps/projettachedetail.html", {'rapport': rapport, 'total': total, 'numero_tache': numero_tache, 'numero_projet': numero_projet})
    filename = "rapport_employe_%s_%s_%s.xls" % (numero_projet, numero_tache, datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response

@permission_required('feuilledetemps.afficher_rapport_temps')
def listeemployes(request):
    blocs = Bloc.objects.values('employe__user__username','employe__user__first_name', 'employe__user__last_name', 'employe__hire_date', 'employe__banque_heure').annotate(heure=Sum('temps')).order_by('employe__user__first_name')
    employe_actif =  blocs.filter(employe__user__is_active=True)
    total_actif = Bloc.objects.filter(employe__user__is_active=True).aggregate(total=Sum('temps'), total_banque=Sum('employe__banque_heure'))
    employe_inactif =  blocs.filter(employe__user__is_active=False)
    total_inactif = Bloc.objects.filter(employe__user__is_active=False).aggregate(total=Sum('temps'))
    return render(request, 'feuilledetemps/listeemployes.html', {'employe_actif': employe_actif, 'employe_inactif': employe_inactif, 'total_actif': total_actif, 'total_inactif': total_inactif})
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def liste_employes_csv(request):
    blocs = Bloc.objects.values('employe__user__username','employe__user__first_name', 'employe__user__last_name', 'employe__hire_date', 'employe__banque_heure').annotate(heure=Sum('temps')).order_by('employe__user__first_name')
    total = Bloc.objects.all().aggregate(total=Sum('temps'), total_banque=Sum('employe__banque_heure'))
    response = render_to_response("feuilledetemps/liste_employes_csv.html", {'blocs': blocs, 'total': total})
    filename = "liste_employe_%s.xls" % (datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response

@permission_required('feuilledetemps.afficher_rapport_temps')
def employedetail(request, username):
    blocs = Bloc.objects.values('date','employe__user__first_name','employe__user__last_name','projet__numero','projet__nom','projet__modele','tache__numero','tache__description','temps').filter(employe__user__username=username).order_by('date')
    total = Bloc.objects.filter(employe__user__username=username).aggregate(total=Sum('temps'))
    date = datetime.now().strftime("%Y-%m-%d")
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else: 
        form = DateRangeForm()
    return render(request, 'feuilledetemps/employedetail.html', {'blocs': blocs, 'total':total,'form':form, 'date':date, 'username':username})

@permission_required('feuilledetemps.afficher_rapport_temps')
def employedetail_csv(request, username):
    blocs = Bloc.objects.values('date','employe__user__first_name','employe__user__last_name','projet__numero','projet__nom','projet__modele','tache__numero','tache__description','temps').filter(employe__user__username=username).order_by('date')
    total = Bloc.objects.filter(employe__user__username=username).aggregate(total=Sum('temps'))
    response = render_to_response("feuilledetemps/employedetail_csv.html", {'blocs': blocs, 'total':total})
    filename = "rapport_du_temps_%s_%s.xls" % (username,datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response

@permission_required('feuilledetemps.afficher_rapport_temps')
def employedetailperiode(request, username, date_debut, date_fin):
    blocs = Bloc.objects.values('date','employe__user__first_name','employe__user__last_name','projet__numero','projet__nom','projet__modele','tache__numero','tache__description','temps').filter(employe__user__username=username,date__gte=date_debut,date__lte=date_fin).order_by('date')
    total = Bloc.objects.filter(employe__user__username=username,date__gte=date_debut,date__lte=date_fin).aggregate(total=Sum('temps'))
    date = datetime.now().strftime("%Y-%m-%d")
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = '../../' + str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else: 
        form = DateRangeForm()
    return render(request, 'feuilledetemps/employedetail.html', {'blocs': blocs, 'total':total,'form':form, 'date':date, 'date_debut':date_debut, 'date_fin':date_fin, 'username':username})
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def employe_detail_periode_csv(request, username, date_debut, date_fin):
    blocs = Bloc.objects.values('date','employe__user__first_name','employe__user__last_name','projet__numero','projet__nom','projet__modele','tache__numero','tache__description','temps').filter(employe__user__username=username,date__gte=date_debut,date__lte=date_fin).order_by('date')
    total = Bloc.objects.filter(employe__user__username=username,date__gte=date_debut,date__lte=date_fin).aggregate(total=Sum('temps'))
    response = render_to_response("feuilledetemps/employedetail_csv.html", {'blocs': blocs, 'total':total, 'date_debut':date_debut, 'date_fin':date_fin})
    filename = "rapport_de_temps_%s_du_%s_au_%s.xls" % (username,date_debut,date_fin)
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response  

@permission_required('feuilledetemps.afficher_rapport_temps')
def listeblocs(request, date_debut, date_fin):
    blocs = Bloc.objects.values('date','employe__user__username','employe__user__first_name','employe__user__last_name','projet__numero','projet__nom','projet__modele','tache__numero','tache__description','temps').filter(date__gte=date_debut,date__lte=date_fin).order_by('date','employe__user__first_name')
    total = Bloc.objects.filter(date__gte=date_debut,date__lte=date_fin).aggregate(total=Sum('temps'))
    date = datetime.now().strftime("%Y-%m-%d")
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = '../../' + str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else: 
        form = DateRangeForm()
    return render(request, 'feuilledetemps/liste_blocs.html', {'blocs': blocs, 'total':total,'form':form, 'date':date, 'date_debut':date_debut, 'date_fin':date_fin})
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def listeblocs_csv(request, date_debut, date_fin):
    blocs = Bloc.objects.values('date','employe__user__first_name','employe__user__last_name','projet__numero','projet__nom','projet__modele','tache__numero','tache__description','temps').filter(date__gte=date_debut,date__lte=date_fin).order_by('date','employe__user__first_name')
    total = Bloc.objects.filter(date__gte=date_debut,date__lte=date_fin).aggregate(total=Sum('temps'))
    response = render_to_response("feuilledetemps/employedetail_csv.html", {'blocs': blocs, 'total':total, 'date_debut':date_debut, 'date_fin':date_fin})
    filename = "bloc_de_temps_%s_au_%s.xls" % (date_debut, date_fin)
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response

@permission_required('feuilledetemps.afficher_rapport_temps')
def employe_sommaire(request, username):
    blocs = Bloc.objects.filter(employe__user__username=username).values('projet__numero','projet__nom','projet__modele').annotate(heure=Sum('temps')).order_by('projet__numero')
    total = Bloc.objects.filter(employe__user__username=username).aggregate(total=Sum('temps'))
    employe = User.objects.get(username=username)
    for b in blocs:
        tache_projet = Bloc.objects.filter(projet__numero=b['projet__numero'],employe__user__username=username).values('tache__numero', 'tache__description').annotate(heure_tache=Sum('temps')).order_by('tache__numero')
        b.update({'tache_projet' : tache_projet})
    return render(request, 'feuilledetemps/employe_sommaire.html', {'blocs': blocs, 'total':total, 'employe':employe})
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def employe_sommaire_csv(request, username):
    blocs = Bloc.objects.filter(employe__user__username=username).values('projet__numero','projet__nom','projet__modele','tache__numero', 'tache__description').annotate(heure=Sum('temps')).order_by('projet__numero','tache__numero')
    total = Bloc.objects.filter(employe__user__username=username).aggregate(total=Sum('temps'))
    employe = User.objects.get(username=username)
    response = render_to_response("feuilledetemps/employe_sommaire_csv.html", {'blocs': blocs, 'total':total, 'employe':employe})
    filename = "rapport_employe_%s_%s_%s.xls" % (employe.first_name, employe.last_name, datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')
def liste_nom_projet(request, nom_projet):
    blocs = Bloc.objects.filter(projet__nom=nom_projet).values('projet__modele').annotate(heure=Sum('temps'))
    total = Bloc.objects.filter(projet__nom=nom_projet).aggregate(total=Sum('temps'))
    for b in blocs:
        liste_projet = Bloc.objects.filter(projet__nom=nom_projet,projet__modele=b['projet__modele']).values('projet__numero').annotate(heure_modele=Sum('temps')).order_by('projet__numero')
        liste_temps_projets = list()
        for projet in liste_projet:
            liste_temps_projets.append(projet['heure_modele'])
        moyenne = format(reduce(lambda x, y: x + y, liste_temps_projets) / len(liste_temps_projets), '.2f')
        b.update({'liste_projet' : liste_projet, 'moyenne':moyenne})
    return render(request, 'feuilledetemps/liste_nom_projet.html', {'blocs': blocs, 'total':total, 'nom_projet':nom_projet})

@permission_required('feuilledetemps.afficher_rapport_temps')
def liste_nom_projet_csv(request, nom_projet):    
    blocs = Bloc.objects.filter(projet__nom=nom_projet).values('projet__modele').annotate(heure=Sum('temps'))
    total = Bloc.objects.filter(projet__nom=nom_projet).aggregate(total=Sum('temps'))
    for b in blocs:
        liste_projet = Bloc.objects.filter(projet__nom=nom_projet,projet__modele=b['projet__modele']).values('projet__numero').annotate(heure_modele=Sum('temps')).order_by('projet__numero')
        liste_temps_projets = list()
        for projet in liste_projet:
            liste_temps_projets.append(projet['heure_modele'])
        moyenne = format(reduce(lambda x, y: x + y, liste_temps_projets) / len(liste_temps_projets), '.2f')
        b.update({'liste_projet' : liste_projet, 'moyenne':moyenne})
    response = render_to_response("feuilledetemps/liste_nom_projet_csv.html", {'blocs': blocs, 'total':total, 'nom_projet':nom_projet})
    filename = "Rapport des projets de nom %s %s.xls" % (nom_projet,datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response   
    
@permission_required('feuilledetemps.afficher_rapport_temps')    
def liste_modele_projet(request, nom_projet, modele_projet):
    blocs = Bloc.objects.filter(projet__nom=nom_projet,projet__modele=modele_projet).values('projet__numero').annotate(heure=Sum('temps')).order_by('projet__numero')
    total = Bloc.objects.filter(projet__nom=nom_projet,projet__modele=modele_projet).aggregate(total=Sum('temps'))
    liste_temps_projets = list()
    for b in blocs:
        liste_temps_projets.append(b['heure'])
        liste_tache = Bloc.objects.filter(projet__nom=nom_projet,projet__modele=modele_projet,projet__numero=b['projet__numero']).values('tache__numero','tache__description').annotate(heure_tache=Sum('temps')).order_by('tache__numero')
        b.update({'liste_tache' : liste_tache})
    moyenne = format(reduce(lambda x, y: x + y, liste_temps_projets) / len(liste_temps_projets), '.2f')
    return render(request, 'feuilledetemps/liste_modele_projet.html', {'blocs': blocs, 'total':total, 'nom_projet':nom_projet, 'modele_projet':modele_projet, 'moyenne':moyenne})

@permission_required('feuilledetemps.afficher_rapport_temps')    
def liste_modele_projet_csv(request, nom_projet, modele_projet):
    blocs = Bloc.objects.filter(projet__nom=nom_projet,projet__modele=modele_projet).values('projet__numero').annotate(heure=Sum('temps')).order_by('projet__numero')
    total = Bloc.objects.filter(projet__nom=nom_projet,projet__modele=modele_projet).aggregate(total=Sum('temps'))
    liste_temps_projets = list()
    for b in blocs:
        liste_temps_projets.append(b['heure'])
        liste_tache = Bloc.objects.filter(projet__nom=nom_projet,projet__modele=modele_projet,projet__numero=b['projet__numero']).values('tache__numero','tache__description').annotate(heure_tache=Sum('temps')).order_by('tache__numero')
        b.update({'liste_tache' : liste_tache})
    moyenne = format(reduce(lambda x, y: x + y, liste_temps_projets) / len(liste_temps_projets), '.2f')
    response = render_to_response("feuilledetemps/liste_modele_projet_csv.html", {'blocs': blocs, 'total':total, 'nom_projet':nom_projet, 'modele_projet':modele_projet, 'moyenne':moyenne})
    filename = "Rapport des projets %s %s %s.xls" % (nom_projet,modele_projet,datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response   
    
@permission_required('feuilledetemps.afficher_rapport_temps')    
def liste_clients(request):
    liste_clients = Client.objects.values('id','compagnie').order_by('compagnie')
    for client in liste_clients:
        liste_projets = Projet.objects.filter(client=client['id']).order_by('numero')
        client.update({'liste_projets' : liste_projets})
    return render(request, 'feuilledetemps/liste_clients.html', {'liste_clients':liste_clients})
    
@permission_required('feuilledetemps.afficher_rapport_temps')    
def liste_clients_csv(request):
    liste_clients = Client.objects.values('id','compagnie').order_by('compagnie')
    for client in liste_clients:
        liste_projets = Projet.objects.filter(client=client['id']).order_by('numero')
        client.update({'liste_projets' : liste_projets})
    response = render_to_response("feuilledetemps/liste_clients_csv.html", {'liste_clients':liste_clients})
    filename = "Rapport des projets par client %s.xls" % (datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response
    
@permission_required('feuilledetemps.afficher_rapport_temps')    
def client_details(request, client_id):
    client = Client.objects.get(id=client_id)
    liste_projets = list()
    for projet in client.projet_set.all():
        heures = Bloc.objects.filter(projet=projet).aggregate(total=Sum('temps'))
        liste_projets.append({'projet':projet,'heures':heures})
    return render(request, 'feuilledetemps/client_details.html', {'client':client,'liste_projets':liste_projets})

@permission_required('feuilledetemps.afficher_rapport_temps')    
def client_details_csv(request, client_id):
    client = Client.objects.get(id=client_id)
    liste_projets = list()
    for projet in client.projet_set.all():
        heures = Bloc.objects.filter(projet=projet).aggregate(total=Sum('temps'))
        liste_projets.append({'projet':projet,'heures':heures})
    response = render_to_response("feuilledetemps/client_details_csv.html", {'client':client,'liste_projets':liste_projets})
    filename = "Rapport des projets %s %s.xls" % (client.compagnie,datetime.now().strftime("%Y-%m-%d"))
    response['Content-Disposition'] = 'attachment; filename='+filename
    response['Content-Type'] = 'application/vnd.ms-excel; charset=utf-8'
    return response    
    
@permission_required('feuilledetemps.afficher_rapport_temps')    
def rapport_complet(request, numero_projet):
    projet = Projet.objects.get(numero=numero_projet)
    liste_bloc = Bloc.objects.filter(projet=projet).order_by('tache','date','employe')
    total_temps = liste_bloc.values('tache__numero','tache__description').annotate(total_tache=Sum('temps')).order_by('tache')
    total_projet = Bloc.objects.filter(projet=projet).aggregate(total=Sum('temps'))
    return render(request, 'feuilledetemps/rapport_complet.html', {'projet':projet,'liste_bloc':liste_bloc, 'total_temps':total_temps, 'total_projet':total_projet})






