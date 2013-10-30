from django.db import models
from ressources.models import Devise
from decimal import *


class Categorie(models.Model):
    nom = models.CharField(verbose_name=u"Nom", max_length=30, unique=True)
    nom_en = models.CharField(verbose_name=u"Nom Anglais", max_length=30, unique=True)

    def __unicode__(self):
        return u"%s" % self.nom


class Fournisseur(models.Model):
    nom = models.CharField(verbose_name=u"Nom", max_length=100)
    telephonne = models.CharField(verbose_name=u"Numéro de téléphonne", max_length=100, blank=True, null=True)
    fax = models.CharField(verbose_name=u"Numéro de fax", max_length=100, blank=True, null=True)
    siteweb = models.CharField(verbose_name=u"Site web", max_length=100, blank=True, null=True)
    devise = models.ForeignKey(Devise,verbose_name=u"Devise")
    ratio = models.DecimalField(verbose_name=u"Ratio", max_digits=5, decimal_places=2, default='1')
    actif = models.BooleanField(verbose_name=u"Actif")

    def __unicode__(self):
        return u"%s" % self.nom


class Machinerie(models.Model):
    numero = models.CharField(verbose_name=u"Numéro", max_length=100, unique=True)
    description = models.TextField(verbose_name=u"Description")
    details = models.TextField(verbose_name=u"Détails", blank=True, null=True)
    fournisseur = models.ForeignKey(Fournisseur, verbose_name=u"Fournisseur")
    prix_fournisseur = models.DecimalField(verbose_name=u"Prix du fournisseur", max_digits=9, decimal_places=2)
    dateprix = models.DateField(verbose_name=u"Date du prix", null=True, blank=True)
    escompte = models.DecimalField(verbose_name=u"Escompte (%)", max_digits=5, decimal_places=2,default='0')
    ratio = models.DecimalField(verbose_name=u"Ratio", max_digits=5, decimal_places=2, default='0')

    class Meta:
        abstract = True
        permissions = (("afficher_listes_prix", "Afficher les listes de prix"),)
        
    def __unicode__(self):
        return u"%s %s" % (self.numero, self.description)
    
    def prixCAD(self):
        return format(self.fournisseur.devise.toCAD(self.prix_fournisseur), '.2f')
    prixCAD.short_description = 'Prix ($ CAD)'
    
    def cost(self):
        pourcentage = (self.escompte / 100)
        escompte = Decimal(self.prixCAD()) * pourcentage
        return format(Decimal(self.prixCAD()) - escompte, '.2f')
    cost.short_description = 'Cost ($ CAD)'
    
    def ratioEffectif(self):
        if self.ratio == 0:
            ratio = self.fournisseur.ratio
        else:
            ratio = self.ratio
        return ratio
    ratioEffectif.short_description = 'Ratio Effectif'
    
    def plMin(self):
        return format(Decimal(self.prixCAD()) * self.ratioEffectif(), '.2f')
    plMin.short_description = 'Prix Vente ($ CAD)'

    def profit(self):
        return format(Decimal(self.plMin()) - Decimal(self.cost()), '.2f')
    profit.short_description = 'Profit ($ CAD)'

    def profit_pourcent(self):
        return format(Decimal(self.profit()) / Decimal(self.plMin())*100, '.2f')
    profit_pourcent.short_description = 'Profit (% Brute)'


class Machine(Machinerie):
    categorie = models.ForeignKey(Categorie, verbose_name=u"Catégorie")
    actif = models.BooleanField(verbose_name=u"Actif")


class Option(Machinerie):
    machines = models.ManyToManyField(Machine, related_name='options_machine')