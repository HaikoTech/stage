# Generated by Django 5.1 on 2024-08-14 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_lahatra', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personne',
            name='guichet',
            field=models.CharField(max_length=255),
        ),
    ]
