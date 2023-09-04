# Generated by Django 4.2.4 on 2023-08-29 22:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("requestapp", "0008_repair_category_phone_number2"),
    ]

    operations = [
        migrations.AddField(
            model_name="repair_category",
            name="staff_in_charge",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staff_in_charge",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]