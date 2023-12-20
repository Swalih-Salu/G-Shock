from django import forms
from .models import Sitedetails

class SiteForm(forms.ModelForm):
    class Meta:
         model=Sitedetails
         fields='__all__'