from django import forms
from django.forms.models import BaseModelFormSet
from projet.models import *
from feuilledetemps.models import Bloc, Bloc_Banque
from django.contrib.auth.models import User
from employe.models import *

class DateRangeForm(forms.Form):
    date_debut = forms.DateField()
    date_fin = forms.DateField()
    
class FilterForm(forms.Form):
    date_debut = forms.DateField()
    date_fin = forms.DateField()
    projet = forms.ModelChoiceField(queryset=Projet.objects.all().order_by('numero'), empty_label=None)
    
class BlocForm(forms.ModelForm):
    projet = forms.ModelChoiceField(queryset=Projet.objects.order_by('-actif','-numero'))
    employe = forms.ModelChoiceField(queryset=Employe.objects.filter(user__is_active=True).order_by('user__first_name'))
    class Meta:
        model = Bloc
        
class BaseBlocFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseBlocFormSet, self).__init__(*args, **kwargs)
        self.queryset = Bloc.objects.none()

class Bloc_BanqueForm(forms.ModelForm):
    projet = forms.ModelChoiceField(queryset=Projet.objects.order_by('-actif','-numero'))
    employe = forms.ModelChoiceField(queryset=Employe.objects.filter(user__is_active=True).order_by('user__first_name'))
    class Meta:
        model = Bloc_Banque
        
class BaseBloc_BanqueFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseBloc_BanqueFormSet, self).__init__(*args, **kwargs)
        self.queryset = Bloc_Banque.objects.none()