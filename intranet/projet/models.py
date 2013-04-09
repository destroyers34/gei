# -*- coding: utf8 -*-
from django.db import models
from client.models import Client
from employe.models import Compagnie
from datetime import datetime, time
# Create your models here.

class Projet(models.Model):
    numero = models.CharField(max_length=30,unique=True,verbose_name=u"Numéro du Projet")
    nom = models.CharField(max_length=30,verbose_name=u"Nom")
    modele = models.CharField(max_length=30,verbose_name=u"Modèle")
    serial_number = models.CharField(max_length=30,verbose_name=u"Numéro de Série", blank=True)
    client = models.ForeignKey(Client,verbose_name=u"Client", null=True, blank=True)
    budget_mat = models.DecimalField(max_digits=11,decimal_places=2,verbose_name=u"Budget MAT",)
    budget_mo = models.DecimalField(max_digits=11,decimal_places=2,verbose_name=u"Budget MO",)
    date_soumission = models.DateField(verbose_name=u"Date de Soumission", null=True, blank=True)
    date_debut = models.DateField(verbose_name=u"Date de Début", null=True, blank=True)
    date_fin = models.DateField(verbose_name=u"Date de Fin", null=True, blank=True)
    actif = models.BooleanField(verbose_name=u"Actif")

    def __unicode__(self):
        return u'%s : %s %s' % (self.numero, self.nom, self.modele)
    
    def jours_restant(self):
        if self.date_fin is not None:
            return self.date_fin.timetuple().tm_yday - datetime.now().timetuple().tm_yday
        else:
            return u'Indéterminé'
    
    class Meta:
        verbose_name = u"Projet"
        ordering = ['-numero']