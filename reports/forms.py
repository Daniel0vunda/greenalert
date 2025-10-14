from django import forms
from .models import WasteReport

class WasteReportForm(forms.ModelForm):
    class Meta:
        model = WasteReport
        fields = ['name', 'location', 'description', 'image']
        