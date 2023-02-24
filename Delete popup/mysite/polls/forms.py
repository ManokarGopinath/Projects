from django import forms
from .models import Genre, Film

class Genreform(forms.ModelForm):
    class Meta:
        model=Genre
        fields="__all__"

class Filmform(forms.ModelForm):
    class Meta:
        model=Film
        fields="__all__"