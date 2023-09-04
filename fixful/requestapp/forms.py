from django import forms
from .models import Repair_category
from django.contrib.auth.models import User
from fixful.userapp.models import Profile
 

class Request_form(forms.ModelForm):

    phone_number2 = forms.CharField(required=False, max_length=15,)
    class Meta:
        model = Repair_category
        fields = [
            'device_name',
            'category',
            'description',
            'phone_number',
            'phone_number2',
            'address',
        ]
        
        widgets = {
            "description": forms.Textarea(attrs={'cols':60, 'row':3})
        }


class AcceptFix_forms(forms.ModelForm):
    list_engineer = [("", "---------------")]

    for user in User.objects.filter(is_staff=True):
        if user.profile.position =="Engineer":
            _id = user.id
            
            engineer_user = User.objects.get(id=_id)
     
            list_engineer.append((engineer_user.first_name + " " + engineer_user.last_name, engineer_user.first_name + " " + engineer_user.last_name ))
   

    engineer = forms.ChoiceField(choices=list_engineer, required = False) 
    class Meta:
        model = Repair_category
        fields = [
            'engineer',
            'status'
        ]
        
        labels = {
            'status': 'Repair Status',
            'engineer': 'Engineer Name',
        }