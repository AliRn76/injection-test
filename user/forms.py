from django import forms
from .models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())

class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=200, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password']
