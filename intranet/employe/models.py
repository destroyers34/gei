# -*- coding: utf8 -*-
from django.db import models
from django.contrib.auth.models import User

class Compagnie(models.Model):
    nom = models.CharField(max_length=60,verbose_name=u"Nom")
    
    def __unicode__(self):
        return u'%s' % (self.nom)
            
    class Meta:
        verbose_name = u"Compagnie"

class Employe(models.Model):
    user = models.OneToOneField(User)
    compagnie = models.ForeignKey(Compagnie,verbose_name=u"Compagnie", blank=True, null=True)
    hire_date = models.DateField(blank=True,verbose_name=u"Date d'Embauche")
    banque_heure = models.DecimalField(max_digits=11,decimal_places=2,blank=True,verbose_name=u"Heure en Banque",default='0')
    
    def __unicode__(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)
            
    class Meta:
        verbose_name = u"Employé"

    def get_Name(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)
    get_Name.short_description = 'Nom'
    
#class Superviseur(models.Model):
#    superviseur = models.ForeignKey(Employe,related_name=u"Superviseur", verbose_name=u"Superviseur", blank=True, null=True)
#    employe = models.ForeignKey(Employe,related_name=u"Employe", verbose_name=u"Employe", blank=True, null=True)
#    
#    def __unicode__(self):
#        return u'%s supervise %s' % (self.superviseur, self.employe)
#            
#    class Meta:
#        verbose_name = u"Superviseur"
