from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Compagnie(models.Model):
    nom = models.CharField(max_length=60, verbose_name=u"Nom")
    
    def __unicode__(self):
        return u'%s' % self.nom
            
    class Meta:
        verbose_name = u"Compagnie"


class Employe(models.Model):
    user = models.OneToOneField(User)
    compagnie = models.ForeignKey(Compagnie, verbose_name=u"Compagnie", blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True, verbose_name=u"Date d'embauche")
    banque_heure = models.DecimalField(max_digits=11, decimal_places=2, verbose_name=u"Heure(s) en banque", default=0.00)
    taux_horaire = models.DecimalField(max_digits=6, decimal_places=2, verbose_name=u"Taux horaire", default=0.00)
    superviseur = models.ForeignKey("self", blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)
            
    class Meta:
        verbose_name = u"Employé"
        ordering = ['user__first_name']

    def get_Name(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)
    get_Name.short_description = 'Nom'


class Devise(models.Model):
    nom = models.CharField(verbose_name=u"Nom", max_length=100)
    code_iso = models.CharField(verbose_name=u"Code ISO", max_length=3)
    symbole = models.CharField(verbose_name=u"Symbole", max_length=3)
    taux_toCAD = models.DecimalField(verbose_name=u"Taux vers ($CA)", max_digits=13, decimal_places=10, default='1')
    taux_inverse = models.DecimalField(verbose_name=u"Taux inverse", max_digits=13, decimal_places=10, default='1')
    date_taux = models.DateField(verbose_name=u"Date des taux")

    def __unicode__(self):
        return u"%s (%s)" % (self.nom, self.symbole)

    def toCAD(self, price):
        return price * self.taux_toCAD
    
    def toDevise(self, price):
        return price * self.taux_inverse


class Tache(models.Model):
    numero = models.CharField(max_length=10, verbose_name=u"Numéro")
    description = models.CharField(max_length=60, verbose_name=u"Description")

    def __unicode__(self):
        return u'%s %s' % (self.numero, self.description)

    class Meta:
        verbose_name = u"Tâche"
        ordering = ['numero']