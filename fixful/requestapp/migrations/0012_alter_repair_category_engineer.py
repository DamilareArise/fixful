# Generated by Django 4.2.4 on 2023-08-31 11:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("requestapp", "0011_repair_category_engineer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="repair_category",
            name="engineer",
            field=models.CharField(default="None", max_length=50),
        ),
    ]
