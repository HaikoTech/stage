# Generated by Django 5.1 on 2024-08-16 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_lahatra', '0002_alter_personne_guichet'),
    ]

    operations = [
        migrations.AddField(
            model_name='guichet',
            name='alpha',
            field=models.CharField(default='?', max_length=1),
        ),
        migrations.AddField(
            model_name='personne',
            name='numero',
            field=models.CharField(default='?000', max_length=4),
        ),
    ]
