from django.db import models

class Guichet(models.Model):
    nom = models.CharField(max_length=255)
    alpha = models.CharField(max_length=1, default="?")
    nb_now = models.IntegerField(default=0)
    nb_personne = models.IntegerField(default=0)


    def __str__(self):
        return self.nom

class Personne(models.Model):
    nom = models.CharField(max_length=255)
    guichet = models.CharField(max_length=255)
    numero = models.IntegerField()
    date_temps = models.CharField(max_length=255, default="")
    statut = models.CharField(max_length=255, default="New")
    