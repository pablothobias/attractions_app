# Generated by Django 5.0 on 2023-12-20 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('core', '0003_attraction_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='address.address'),
        ),
    ]
