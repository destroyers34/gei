from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from django.forms.models import modelformset_factory
from feuilles_de_temps.models import Bloc_Eugenie, Banque, Bloc_TPE
from ressources.models import Employe
from feuilles_de_temps.forms import BlocEugenieForm, BanqueForm, BlocTPEForm, ConsultationBlocEugenieForm, ConsultationBlocTPEForm, BlocEugenieEmployeForm

@permission_required('feuilles_de_temps.add_bloc_eugenie')    
def blocs_eci(request):
    queryset = Bloc_Eugenie.objects.all()
    limit = 20
    count = queryset.count()
    if count > limit:
        last_blocs = queryset[count-limit:]
    else:
        last_blocs = queryset
    if request.method == 'POST':
        form = ConsultationBlocEugenieForm(request.POST)
        if form.is_valid():
            emp = form.cleaned_data['employe']
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = str(emp.user.username) + '/' + str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else: 
        form = ConsultationBlocEugenieForm()
    return render(request,"feuillesdetemps/blocs_eci.html", {"last_blocs": last_blocs,'form':form})


@permission_required('feuilles_de_temps.add_bloc_tpe')
def blocs_tpe(request):
    queryset = Bloc_TPE.objects.all()
    limit = 20
    count = queryset.count()
    if count > limit:
        last_blocs = queryset[count-limit:]
    else:
        last_blocs = queryset
    if request.method == 'POST':
        form = ConsultationBlocTPEForm(request.POST)
        if form.is_valid():
            emp = form.cleaned_data['employe']
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = str(emp.user.username) + '/' + str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else:
        form = ConsultationBlocTPEForm()
    return render(request,"feuillesdetemps/blocs_tpe.html", {"last_blocs": last_blocs,'form':form})


@permission_required('feuilles_de_temps.add_bloc_eugenie')   
def consultation_blocs_eci(request, username, date_debut, date_fin):
    blocs = Bloc_Eugenie.objects.filter(employe__user__username=username,date__gte=date_debut,date__lte=date_fin).order_by('-date')
    if request.method == 'POST':
        form = ConsultationBlocEugenieForm(request.POST)
        if form.is_valid():
            emp = form.cleaned_data['employe']
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = '../../../' + str(emp.user.username) + '/' + str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else: 
        form = ConsultationBlocEugenieForm()
    return render(request, 'feuillesdetemps/consultation_blocs_eci.html', {'blocs':blocs,'form':form,'username':username,'date_debut':date_debut,'date_fin':date_fin})   

@permission_required('feuilles_de_temps.add_bloc_tpe')
def consultation_blocs_tpe(request, username, date_debut, date_fin):
    blocs = Bloc_TPE.objects.filter(employe__user__username=username,date__gte=date_debut,date__lte=date_fin).order_by('-date')
    if request.method == 'POST':
        form = ConsultationBlocTPEForm(request.POST)
        if form.is_valid():
            emp = form.cleaned_data['employe']
            date_d = form.cleaned_data['date_debut']
            date_f = form.cleaned_data['date_fin']
            redirect_str = '../../../' + str(emp.user.username) + '/' + str(date_d) + '/' + str(date_f) + '/'
            return HttpResponseRedirect(redirect_str) # Redirect after POST
    else:
        form = ConsultationBlocTPEForm()
    return render(request, 'feuillesdetemps/consultation_blocs_tpe.html', {'blocs':blocs,'form':form,'username':username,'date_debut':date_debut,'date_fin':date_fin})

@permission_required('feuilles_de_temps.add_bloc_eugenie')    
def add_blocs_eci(request):
    BlocFormSet = modelformset_factory(Bloc_Eugenie, form=BlocEugenieForm)
    if request.method == 'POST':
        formset = BlocFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("../success/")
    else:
        formset = BlocFormSet(queryset=Bloc_Eugenie.objects.none())
    return render(request,"feuillesdetemps/add_blocs_eci.html", {"formset": formset,})

@permission_required('feuilles_de_temps.add_bloc_tpe')    
def add_blocs_tpe(request):
    BlocFormSet = modelformset_factory(Bloc_TPE, form=BlocTPEForm)
    if request.method == 'POST':
        formset = BlocFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("../success/")
    else:
        formset = BlocFormSet(queryset=Bloc_TPE.objects.none())
    return render(request,"feuillesdetemps/add_blocs_tpe.html", {"formset": formset,})    
    
@login_required    
def success(request):
    return render(request,"feuillesdetemps/success.html")    

@permission_required('feuilles_de_temps.add_bloc_banque')    
def add_banque(request):
    BanqueFormSet = modelformset_factory(Banque, form=BanqueForm)
    if request.method == 'POST':
        formset = BanqueFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("../success/")
    else:
        formset = BanqueFormSet(queryset=Banque.objects.none())
    return render(request, "feuillesdetemps/add_banque.html", {"formset": formset,})


def employe_add_bloc_eugenie(request):
    BlocFormSet = modelformset_factory(Bloc_Eugenie, form=BlocEugenieEmployeForm)
    if request.method == 'POST':
        formset = BlocFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                employe = Employe.objects.get(user_id=request.user.id)
                bloc = Bloc_Eugenie(
                    employe=employe,
                    date=form.cleaned_data['date'],
                    projet=form.cleaned_data['projet'],
                    tache=form.cleaned_data['tache'],
                    temps=form.cleaned_data['temps'],
                    note=form.cleaned_data['note'],
                    approuve=False
                )
                bloc.save()
            return HttpResponseRedirect("../success/")
    else:
        formset = BlocFormSet(queryset=Bloc_Eugenie.objects.none())
    return render(request,"feuillesdetemps/employe_add_bloc_eugenie.html", {"formset": formset,})