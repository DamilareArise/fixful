from django import forms
from .models import Repair_category
 

class Request_form(forms.ModelForm):

    class Meta:
        model = Repair_category
        fields = [
            'device_name',
            'category',
            'description',
            'phone_number',
            'address',
        ]
       
        widgets = {
            "description": forms.Textarea(attrs={'cols':60, 'row':3})
        }