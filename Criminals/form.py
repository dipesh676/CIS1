from django import forms
from django.forms import ModelForm
from .models import FIR

class complainform(forms.Form):
    c_type = forms.CharField(label='Crime-Type', max_length=50)
    c_addr = forms.CharField(label='Crime-Location', max_length=50)
    report = forms.CharField(label='Full-Report', max_length=200,
            widget=forms.Textarea)
    reported_by = forms.CharField(label='Reported-By', max_length=50)
    contact = forms.CharField(label='Contact', max_length=50)

    def save(self, data):
        fir = FIR()
        fir.crime_type = data['c_type']
        fir.crime_addr = data['c_addr']
        fir.full_report = data['report']
        fir.reported_by = data['reported_by']
        fir.contact = data['contact']
        fir.save()
