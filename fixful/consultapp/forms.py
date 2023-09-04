from django import forms
from .models import Consult
# from django.contrib.auth.models import User

class consultation_form(forms.ModelForm):

    class Meta:
        model = Consult
        fields = [
            'category',
            'complaint',
            'device_name',
        ]
       
        widgets = {
            "complaint": forms.Textarea(attrs={'cols':60, 'row':3})
        }

