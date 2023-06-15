from django import forms
from .models import Movie

class movie_form(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['name','dis','year','img']

