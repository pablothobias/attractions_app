# Generated by Django 5.0 on 2023-12-21 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_attraction_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attraction',
            name='reviews',
        ),
        migrations.AddField(
            model_name='attraction',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='attractions'),
        ),
    ]