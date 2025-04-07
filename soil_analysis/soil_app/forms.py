from django import forms
from .models import SoilAnalysis

class SoilUploadForm(forms.ModelForm):
    class Meta:
        model = SoilAnalysis
        fields = ['csv_file']


        