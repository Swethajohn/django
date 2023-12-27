from django import forms
from .models import *

class studform(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'