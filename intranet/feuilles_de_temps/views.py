from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import permission_required, login_required
from django.forms.models import modelformset_factory
from feuilles_de_temps.models import Bloc_Eugenie, Banque, Bloc_TPE
from feuilles_de_temps.forms import BlocEugenieForm, BanqueForm, BlocTPEForm

@permission_required('feuilles_de_temps.add_bloc')    
def add_blocs_eci(request):
    BlocFormSet = modelformset_factory(Bloc_Eugenie, form=BlocEugenieForm)
    if request.method == 'POST':
        formset = BlocFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("success")
    else:
        formset = BlocFormSet(queryset=Bloc_Eugenie.objects.none())
    return render(request,"feuillesdetemps/add_blocs_eci.html", {"formset": formset,})

@permission_required('feuilles_de_temps.add_bloc')    
def add_blocs_tpe(request):
    BlocFormSet = modelformset_factory(Bloc_TPE, form=BlocTPEForm)
    if request.method == 'POST':
        formset = BlocFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("success")
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
            return HttpResponseRedirect("success")
    else:
        formset = BanqueFormSet(queryset=Banque.objects.none())
    return render(request,"feuillesdetemps/add_banque.html", {"formset": formset,})   