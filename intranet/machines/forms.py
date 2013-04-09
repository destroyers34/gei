from django import forms
from django.forms.models import BaseModelFormSet
from django.contrib.auth.models import User
from machines.models import *
    
class OptionForm(forms.ModelForm):
    calcul = forms.BooleanField(required=False)
        
    class Meta:
        model = Option
        exclude=('ratio','fournisseur','escompte','description','prixliste')
    
    def __init__(self, *args, **kwargs):
        super(OptionForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['code'].widget.attrs['readonly'] = True
        
class BaseOptionFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseOptionFormSet, self).__init__(*args, **kwargs)