# Generated by Django 5.0 on 2023-12-11 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttractionsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('descriptions', models.TextField()),
                ('open_days', models.TextField()),
                ('open_hour', models.TimeField()),
                ('close_hour', models.TimeField()),
                ('min_age_enter', models.IntegerField()),
            ],
        ),
    ]
