# Generated by Django 5.1 on 2024-08-16 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_lahatra', '0003_guichet_alpha_personne_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='numero',
            field=models.CharField(default='000', max_length=3),
        ),
    ]
