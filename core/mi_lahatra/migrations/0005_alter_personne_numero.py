# Generated by Django 5.1 on 2024-08-16 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_lahatra', '0004_alter_personne_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='numero',
            field=models.IntegerField(max_length=3),
        ),
    ]
