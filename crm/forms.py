from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

        widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'department': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'address': forms.Textarea(attrs={'class': 'form-control',"rows":3}),
        'salary': forms.TextInput(attrs={'class': 'form-control'}),
        'gender': forms.Select(attrs={'class': 'form-select'}),
        'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
    }
        labels={
            "name":"NAME"
        }