from django import forms
from django.forms.models import BaseModelFormSet
from projets.models import Projet_Eugenie, Projet_TPE
from feuilles_de_temps.models import Bloc_Eugenie, Banque, Bloc_TPE
from ressources.models import Employe


class BlocEugenieForm(forms.ModelForm):
    projet = forms.ModelChoiceField(queryset=Projet_Eugenie.objects.order_by('-actif','-numero'))
    employe = forms.ModelChoiceField(queryset=Employe.objects.filter(user__is_active=True).order_by('user__first_name'))

    class Meta:
        model = Bloc_Eugenie


class BlocEugenieEmployeForm(forms.ModelForm):
    projet = forms.ModelChoiceField(queryset=Projet_Eugenie.objects.filter(actif=True).order_by('-numero'))

    class Meta:
        model = Bloc_Eugenie
        exclude = ['employe', 'approuve']

    def __init__(self, *arg, **kwarg):
        super(BlocEugenieEmployeForm, self).__init__(*arg, **kwarg)
        self.empty_permitted = False


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


class BlocTPEForm(forms.ModelForm):
    projet = forms.ModelChoiceField(queryset=Projet_TPE.objects.order_by('-actif','-numero'))
    employe = forms.ModelChoiceField(queryset=Employe.objects.filter(user__is_active=True).order_by('user__first_name'))

    class Meta:
        model = Bloc_TPE


class BaseBlocTPEFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseBlocTPEFormSet, self).__init__(*args, **kwargs)
        self.queryset = Bloc_TPE.objects.none()


class ConsultationBlocEugenieForm(forms.ModelForm):
    employe = forms.ModelChoiceField(queryset=Employe.objects.filter(user__is_active=True).order_by('user__first_name'))
    date_debut = forms.DateField()
    date_fin = forms.DateField()

    class Meta:
        model = Bloc_Eugenie
        fields = ['employe', 'date_debut', 'date_fin']


class ConsultationBlocTPEForm(forms.ModelForm):
    employe = forms.ModelChoiceField(queryset=Employe.objects.filter(user__is_active=True).order_by('user__first_name'))
    date_debut = forms.DateField()
    date_fin = forms.DateField()

    class Meta:
        model = Bloc_TPE
        fields = ['employe', 'date_debut', 'date_fin']