from django import forms
from .models import GoodMorning

class Form1(forms.ModelForm):
    class Meta:
        model = GoodMorning
        fields = ['time_hour', 'am_pm']

        widgets = {
            'time_hour': forms.NumberInput(attrs={'class':'form-control',}) ,
            'am_pm': forms.Select(attrs={'class':'form-select',})
        }