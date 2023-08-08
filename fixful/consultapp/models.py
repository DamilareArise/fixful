from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Consult(models.Model):
    repair_category = [
        ('Laptop Repair', 'Laptop Repair'),
        ('Phone Repair','Phone Repair'),
        ('Others','Others'),
    ]

    def select_staff():
        staff_list = [("--------","")]
        staffs = User.objects.filter(is_staff=True).values()
        for staff in staffs:
            staff_list.append((staff['username'],staff['username']))
        return staff_list


    service_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    device_name = models.CharField(unique=False, max_length=50, null=False)
    complaint = models.CharField(unique=False, max_length=300, null=True)
    category = models.CharField(choices=repair_category, unique=False, max_length=50, null=True)
    date_created = models.DateField(auto_now_add=True, unique=False, max_length=11, null=True)
    agent_incharge = models.CharField(choices=select_staff(), unique=False, max_length=50, null=True)