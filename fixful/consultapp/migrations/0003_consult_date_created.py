# Generated by Django 4.2.3 on 2023-08-01 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("consultapp", "0002_consult_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="consult",
            name="date_created",
            field=models.DateField(auto_now_add=True, max_length=11, null=True),
        ),
    ]
