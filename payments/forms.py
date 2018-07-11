from django import forms
from .models import BillerProfile

class BillerProfileForm(forms.ModelForm):
    class Meta:
        model = BillerProfile
        exclude = ('user','biller_name')