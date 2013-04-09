from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import permission_required, login_required
from django.forms.models import modelformset_factory
from decimal import *
from fournisseurs.models import Fournisseur
from machines.models import Machine, Option
from machines.forms import *


def liste_fournisseurs(request):
    liste_fournisseurs = Fournisseur.objects.all().order_by('nom')
    return render(request, 'machines/liste_fournisseurs.html', {'liste_fournisseurs': liste_fournisseurs})

@permission_required('machines.afficher_listes_prix')
def liste_machines(request, fournisseur_id):
    fournisseur = Fournisseur.objects.get(id=fournisseur_id)
    liste_machines = Machine.objects.filter(fournisseur = fournisseur)
    return render(request, 'machines/liste_machines.html', {'liste_machines': liste_machines, 'fournisseur':fournisseur})

@permission_required('machines.afficher_listes_prix')
def detail_machine(request, fournisseur_id, machine_id):
    machine = Machine.objects.get(id=machine_id)
    liste = list()
    liste.append(machine)
    total = {'liste':liste,'prixliste':machine.prixliste,'plMin':Decimal(machine.plMin()),'cost':Decimal(machine.cost()),'profit':Decimal(machine.profit()),'profit_pourcent':Decimal(machine.profit_pourcent())}
    OptionFormSet = modelformset_factory(Option,extra=0,form=OptionForm)
    if request.method == 'POST':
        formset = OptionFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data['calcul']:
                    option = Option.objects.get(code=form.cleaned_data['code'])
                    total['liste'].append(option)
                    total['plMin'] += Decimal(option.plMin())
                    total['prixliste'] += Decimal(option.prixliste)
                    total['cost'] += Decimal(option.cost())
                    total['profit'] += Decimal(option.profit())
                    total['profit_pourcent'] = format(total['profit']/total['plMin']*100, '.2f')
            return render(request, 'machines/detail_machine.html', {'machine': machine, 'formset':formset,'total':total})  
    else:
        formset = OptionFormSet(queryset=machine.options.all())
    return render(request, 'machines/detail_machine.html', {'machine': machine, 'formset':formset, 'total':total})    