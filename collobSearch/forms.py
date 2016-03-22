from django import forms

from .models import Searcher

class LoginForm(forms.ModelForm):

    class Meta:
        model = Searcher
        fields = ('username', 'password', 'areaOfInterest',)
