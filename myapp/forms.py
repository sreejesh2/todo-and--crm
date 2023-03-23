from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class TodosForm(forms.Form):
    task=forms.CharField(max_length=100)
    user=forms.CharField(max_length=30)
    
    
class RegistrationForm(forms.ModelForm):
   class Meta:
    model=User
    fields=["first_name","last_name","username","email","password"]   

    
    widgets = {
    'username': forms.TextInput(attrs={'class': 'form-control '}),
    'first_name': forms.TextInput(attrs={'class': 'form-control'}),
    'email': forms.EmailInput(attrs={'class': 'form-control'}),
    'last_name': forms.TextInput(attrs={'class': 'form-control'}),
    'password': forms.PasswordInput(attrs={'class': 'form-control'}),
    
} 