# Generated by Django 4.2.3 on 2023-08-22 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("requestapp", "0007_remove_repair_category_complaint"),
    ]

    operations = [
        migrations.AddField(
            model_name="repair_category",
            name="phone_number2",
            field=models.CharField(max_length=15, null=True),
        ),
    ]