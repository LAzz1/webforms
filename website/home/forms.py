from socket import fromshare
from django import forms
from .models import owasp

class VulForms(forms.ModelForm):
    class Meta:
        model = owasp
        fields = ['code','year','title','description']