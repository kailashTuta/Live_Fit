from django.core import validators
from django import forms
from .models import Report


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['name', 'age', 'height', 'weight',
                  'gender', 'exercise', 'diabetic']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Age', 'min': '18', 'max': '60'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Height in cm'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your Weight in kg'}),
            'gender': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Select'), ('male', 'Male'), ('female', 'Female')]),
            'diabetic': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Select'), ('yes', 'Yes'), ('no', 'No')]),
            'exercise': forms.Select(attrs={'class': 'form-control'}, choices=[('', 'Select'), ('sedentary', 'Sedentary'), ('lightlyactive', 'Lightly Active'), ('moderate', 'Moderate'), ('veryactive', 'Very Active'), ('superactive', 'Super Active')]),
        }

