from django import forms

#from .models import Searcher
from accounts.models import User

class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password', 'area_of_interest',)
