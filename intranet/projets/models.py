﻿from django.db import models
from clients.models import Client
from datetime import datetime

class Projet(models.Model):
    numero = models.CharField(max_length=30,unique=True,verbose_name=u"Numéro du projet")
    nom = models.CharField(max_length=30,verbose_name=u"Nom du projet")
    client = models.ForeignKey(Client,verbose_name=u"Client")
    date_soumission = models.DateField(verbose_name=u"Date de soumission", null=True, blank=True)
    date_debut = models.DateField(verbose_name=u"Date de début", null=True, blank=True)
    date_fin = models.DateField(verbose_name=u"Date de fin", null=True, blank=True)
    actif = models.BooleanField(verbose_name=u"Actif")
    en_attente = models.BooleanField(verbose_name=u"En attente") 
    class Meta:
            abstract = True

class Projet_Eugenie(Projet):
    modele = models.CharField(max_length=30,verbose_name=u"Modèle")
    serial_number = models.CharField(max_length=30,verbose_name=u"Numéro de série", blank=True, null=True)
    budget_mat = models.DecimalField(max_digits=11,decimal_places=2,verbose_name=u"Budget MAT ($)",)
    budget_mo = models.DecimalField(max_digits=11,decimal_places=2,verbose_name=u"Budget MO (H)",)
    def __unicode__(self):
        return u'%s : %s %s' % (self.numero, self.nom, self.modele)
    
    def jours_restant(self):
        if self.date_fin is not None:
            return (self.date_fin - datetime.now().date()).days
        else:
            return "Indéterminé"
    
    class Meta:
        verbose_name = u"Projet EuGénie"
        ordering = ['-numero']

class Projet_TPE(Projet):
    description = models.CharField(max_length=30,verbose_name=u"Nom")
    serial_number = models.CharField(max_length=30,verbose_name=u"Numéro de série", blank=True, null=True)
    budget_mat = models.DecimalField(max_digits=11,decimal_places=2,verbose_name=u"Budget MAT ($)",)
    budget_mo = models.DecimalField(max_digits=11,decimal_places=2,verbose_name=u"Budget MO (H)",)
    def __unicode__(self):
        return u'%s : %s - %s' % (self.numero, self.nom, self.description)
    
    def jours_restant(self):
        if self.date_fin is not None:
            return (self.date_fin - datetime.now().date()).days
        else:
            return "Indéterminé"
    
    class Meta:
        verbose_name = u"Projet Techno-Pro Experts"
        ordering = ['-numero']
        
#class Projet_JRC(Projet):