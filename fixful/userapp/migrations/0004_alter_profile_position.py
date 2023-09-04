# Generated by Django 4.2.4 on 2023-08-30 22:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userapp", "0003_alter_profile_means_of_identity_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="position",
            field=models.CharField(
                choices=[
                    ("HOD", "HOD"),
                    ("HR", "HR"),
                    ("Accountant", "Accountant"),
                    ("Admin", "Admin"),
                    ("Consultant", "Consultant"),
                    ("Engineer", "Engineer"),
                ],
                max_length=25,
                null=True,
            ),
        ),
    ]