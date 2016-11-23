from django import forms
import datetime
from .models import usuario

class UsuarioForm(forms.ModelForm):

    nome = forms.CharField(max_length=128, help_text='Nome:')
    sobrenome = forms.CharField(max_length=128, help_text='Sobrenome:')
    dataNasc = forms.DateField(initial=datetime.date.today, help_text='Data:')
    rua = forms.CharField(max_length=128, help_text='Rua:')
    numero = forms.IntegerField(help_text='Numero:')
    bairro = forms.CharField(max_length=128, help_text='Bairro:')
    cidade = forms.CharField(max_length=128, help_text='Cidade:')
    estado = forms.CharField(max_length=128, help_text='Estado:')
    email = forms.CharField(max_length=128, help_text='E-mail:')
    senha = forms.CharField(max_length=128, widget=forms.PasswordInput, help_text='Senha:')

    class Meta:
        model = usuario
        fields = ('nome','sobrenome','dataNasc','rua','numero','bairro','cidade','estado','email','senha')
