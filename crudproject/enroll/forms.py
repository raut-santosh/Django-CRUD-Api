from .models import Student
from django import forms

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll', 'school']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'roll':forms.TextInput(attrs={'class':'form-control'}),
            'school':forms.TextInput(attrs={'class':'form-control'})
        }