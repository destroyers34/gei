from django.db import models
from fournisseurs.models import Fournisseur
from decimal import *

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return u"%s" % self.nom

class Option(models.Model):
    code = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    prixliste = models.DecimalField(max_digits=9, decimal_places=2)
    escompte = models.DecimalField(max_digits=5, decimal_places=2)
    ratio = models.DecimalField(max_digits=5, decimal_places=2)
    fournisseur = models.ForeignKey(Fournisseur)
    
    def __unicode__(self):
        return u"%s %s" % (self.code, self.description)

    def prixCAD(self):
        return format(self.fournisseur.devise.toCAD(self.prixliste), '.2f')
    prixCAD.short_description = 'Prix ($ CAD)'
    
    def cost(self):
        pourcentage = (self.escompte/100)
        escompte = Decimal(self.prixCAD())*pourcentage
        return format(Decimal(self.prixCAD())-escompte, '.2f')
    cost.short_description = 'Cost ($ CAD)'
    
    def ratioEffectif(self):
        if(self.ratio == 0):
            ratio = self.fournisseur.ratio
        else:
            ratio = self.ratio
        return ratio
    ratioEffectif.short_description = 'Ratio Effectif'
    
    def plMin(self):
        return format(Decimal(Decimal(self.prixCAD())*self.ratioEffectif()), '.2f')
    plMin.short_description = 'Prix Vente ($ CAD)'

    def profit(self):
        return format(Decimal(self.plMin())-Decimal(self.cost()), '.2f')
    profit.short_description = 'Profit ($ CAD)'
    
    def profit_pourcent(self):
        return format(Decimal(self.profit())/Decimal(self.plMin())*100, '.2f')
    profit_pourcent.short_description = 'Profit (% Brute)'
    
class Machine(models.Model):
    code = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    fournisseur = models.ForeignKey(Fournisseur)
    prixliste = models.DecimalField(max_digits=9, decimal_places=2)
    dateprix = models.DateField()
    escompte = models.DecimalField(max_digits=5, decimal_places=2)
    ratio = models.DecimalField(max_digits=5, decimal_places=2)
    categorie = models.ForeignKey(Categorie)
    options = models.ManyToManyField(Option, through='Machine_Option')
    
    class Meta:
        permissions = (
                ("afficher_listes_prix","Afficher les listes de prix"),
        )
        
    def __unicode__(self):
        return u"%s %s" % (self.code, self.description)
    
    def prixCAD(self):
        return format(self.fournisseur.devise.toCAD(self.prixliste), '.2f')
    prixCAD.short_description = 'Prix ($ CAD)'
    
    def cost(self):
        pourcentage = (self.escompte/100)
        escompte = Decimal(self.prixCAD())*pourcentage
        return format(Decimal(self.prixCAD())-escompte, '.2f')
    cost.short_description = 'Cost ($ CAD)'
    
    def ratioEffectif(self):
        if(self.ratio == 0):
            ratio = self.fournisseur.ratio
        else:
            ratio = self.ratio
        return ratio
    ratioEffectif.short_description = 'Ratio Effectif'
    
    def plMin(self):
        return format(Decimal(self.prixCAD())*self.ratioEffectif(), '.2f')
    plMin.short_description = 'Prix Vente ($ CAD)'

    def profit(self):
        return format(Decimal(self.plMin())-Decimal(self.cost()), '.2f')
    profit.short_description = 'Profit ($ CAD)'

    def profit_pourcent(self):
        return format(Decimal(self.profit())/Decimal(self.plMin())*100, '.2f')
    profit_pourcent.short_description = 'Profit (% Brute)'
    
class Machine_Option(models.Model):
    machine = models.ForeignKey(Machine)
    option = models.ForeignKey(Option)