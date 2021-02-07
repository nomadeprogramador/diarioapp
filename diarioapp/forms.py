from django import forms
from .models import Diario
from django.forms import ModelForm
class LoginForm(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=30,widget=forms.PasswordInput)
class DiarioForm(ModelForm):
    class Meta:
        model=Diario
        fields=('conteudo',)
