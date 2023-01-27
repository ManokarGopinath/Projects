from django import forms
from .models import Paracheck, Grammercheck, Spellcheck, Filespellcheck

class GrammerForm(forms.ModelForm):
    class Meta:
        model = Grammercheck
        fields = '__all__'

class ParaForm(forms.ModelForm):
    class Meta:
        model = Paracheck
        fields = ('description', 'document',)

class SpellForm(forms.ModelForm):
    class Meta:
        model = Spellcheck
        fields = '__all__'

class FilespellForm(forms.ModelForm):
    class Meta:
        model = Filespellcheck
        fields = ('description', 'document',)