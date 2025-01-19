from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    Email = forms.EmailField(required=True)

    class Meta:
        Model = User
        Fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    Username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
