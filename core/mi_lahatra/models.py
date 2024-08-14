from django.db import models

class Guichet(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Personne(models.Model):
    nom = models.CharField(max_length=255)
    guichet = models.CharField(max_length=255) 