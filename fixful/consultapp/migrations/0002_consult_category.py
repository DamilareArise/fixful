# Generated by Django 4.2.3 on 2023-07-31 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("consultapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="consult",
            name="category",
            field=models.CharField(
                choices=[
                    ("Laptop Repair", "Laptop Repair"),
                    ("Phone Repair", "Phone Repair"),
                    ("Others", "Others"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]