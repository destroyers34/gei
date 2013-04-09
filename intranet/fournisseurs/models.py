from django.db import models
from decimal import *

class Devise(models.Model):
    nom = models.CharField(max_length=100)
    codeiso = models.CharField(max_length=3)
    symbole = models.CharField(max_length=1)
    taux = models.DecimalField(max_digits=8, decimal_places=4, default='1')
    date = models.DateField()

    def __unicode__(self):
        return u"%s (%s)" % (self.nom, self.symbole)

    def toCAD(self, price):
        return price*self.taux
    
class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    telephonne = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    siteweb = models.CharField(max_length=100)
    devise = models.ForeignKey(Devise)
    ratio = models.DecimalField(max_digits=5, decimal_places=2, default='1')

    def __unicode__(self):
        return u"%s" % self.nom
        
