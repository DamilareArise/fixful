# Generated by Django 4.2.2 on 2023-07-05 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                ("profile", models.AutoField(primary_key=True, serialize=False)),
                ("status", models.CharField(max_length=20, null=True)),
                ("address", models.CharField(max_length=100, null=True)),
                ("phone", models.CharField(max_length=11, null=True)),
                ("date_of_birth", models.CharField(max_length=11, null=True)),
                ("gender", models.CharField(max_length=11, null=True)),
                (
                    "nationality",
                    models.CharField(
                        choices=[
                            ("Nigeria", "Nigeria"),
                            ("United Kingdom", "United Kingdom"),
                            ("USA", "USA"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("Oyo", "Oyo"),
                            ("Abia", "Abia"),
                            ("Ekiti", "Ekiti"),
                            ("Abuja", "Abuja"),
                        ],
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "means_of_identity",
                    models.ImageField(null=True, upload_to="identityImage/"),
                ),
                (
                    "particulars",
                    models.ImageField(null=True, upload_to="particularsImage/"),
                ),
                (
                    "profile_passport",
                    models.ImageField(null=True, upload_to="staffImage/"),
                ),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("HOD", "HOD"),
                            ("HR", "HR"),
                            ("Accountant", "Accountant"),
                            ("Admin", "Admin"),
                            ("Consultant", "Consultant"),
                        ],
                        max_length=25,
                        null=True,
                    ),
                ),
                (
                    "marital_status",
                    models.CharField(
                        choices=[
                            ("Single", "Single"),
                            ("Married", "Married"),
                            ("Engaged", "Engaged"),
                            ("Divorced", "Divorced"),
                        ],
                        max_length=25,
                        null=True,
                    ),
                ),
                ("staff", models.BooleanField(default=False)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
