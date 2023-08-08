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

# class Select_staff:
#     def select_staff(self):
#         staff_list = [("--------","")]
#         staffs = User.objects.all().values()
#         for staff in staffs:
#             staff_list.append((staff['username'],staff['username']))
#         return staff_list

# class display_staff(forms.Form):
#     param = Select_staff()
#     staffs = forms.ChoiceField(choices=param.select_staff(), label="Assign Staff")
