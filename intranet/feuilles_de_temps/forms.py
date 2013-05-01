from django import forms
from django.forms.models import BaseModelFormSet
from django.contrib.auth.models import User
from projets.models import Projet_Eugenie
from feuilles_de_temps.models import Bloc_Eugenie, Banque
from ressources.models import Employe
    
class BlocEugenieForm(forms.ModelForm):
    projet = forms.ModelChoiceField(queryset=Projet_Eugenie.objects.order_by('-actif','-numero'))
    employe = forms.ModelChoiceField(queryset=Employe.objects.filter(user__is_active=True).order_by('user__first_name'))
    class Meta:
        model = Bloc_Eugenie
        
class BaseBlocEugenieFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseBlocEugenieFormSet, self).__init__(*args, **kwargs)
        self.queryset = Bloc_Eugenie.objects.none()

class BanqueForm(forms.ModelForm):
    employe = forms.ModelChoiceField(queryset=Employe.objects.filter(user__is_active=True).order_by('user__first_name'))
    class Meta:
        model = Banque
        
class BaseBanqueFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseBanqueFormSet, self).__init__(*args, **kwargs)
        self.queryset = Banque.objects.none()