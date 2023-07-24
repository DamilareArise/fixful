from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Repair_category(models.Model):
    repair_category = [
        ('Laptop Repair', 'Laptop Repair'),
        ('Phone Repair','Phone Repair'),
        ('Others','Others'),
    ]


    service_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    device_name = models.CharField(unique=False, max_length=50, null=False)
    category = models.CharField(choices=repair_category, unique=False, max_length=50, null=False)
    description = models.CharField(unique=False, max_length=300, null=False)
    phone_number = models.CharField(unique=False, max_length=15, null=False)
    address =  models.CharField(unique=False, max_length=50, null=False)
    date_created = models.DateField(auto_now_add=True, unique=False, max_length=11, null=True)
    status = models.BooleanField(default=False, blank=True, null=True, unique=False)

