from django.db import models
from django.utils.encoding import python_2_unicode_compatible

class Horaire(models.Model):
    horaire_heure = models.IntegerField(default=12)
    horaire_minute = models.IntegerField(default=59)

    def __str__(self):
        return "%i:%i" % (self.horaire_heure, self.horaire_minute)

class Ligne(models.Model):
    ligne_lettre = models.CharField(max_length=1)

    def __str__(self):
        return self.ligne_lettre

class Conducteur(models.Model):
    conducteur_nom = models.CharField(max_length=255)

    def __str__(self):
        return self.conducteur_nom

class Train(models.Model):
    train_name = models.CharField(max_length=255)
    train_ligne = models.ForeignKey(Ligne, on_delete=models.CASCADE, blank=True, null=True)
    train_horaire = models.ManyToManyField(Horaire, blank=True, null=True)
    train_conducteur = models.OneToOneField(Conducteur, blank=True, null=True)

    def __str__(self):
        return self.train_name
