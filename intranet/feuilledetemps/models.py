# -*- coding: utf-8 -*-
from django.db import models
from projet.models import Projet
from employe.models import Employe

class Tache(models.Model):
	numero = models.CharField(max_length=10,verbose_name=u"Numéro")
	description = models.CharField(max_length=60,verbose_name=u"Description")

	def __unicode__(self):
		return u'%s %s' % (self.numero, self.description)

	class Meta:
		verbose_name = u"Tâche"

#class Feuille(models.Model):
#	employe = models.ForeignKey(Employe,verbose_name=u"Employé",)
#	datedebut = models.DateField(verbose_name=u"Date de début")
#   datefin = models.DateField(verbose_name=u"Date de fin")
#	tempstotal = models.DecimalField(max_digits=4,decimal_places=2,verbose_name=u"Temps")
#	approuve = models.BooleanField(blank=True, verbose_name=u"Approuve")
#	def __unicode__(self):
#		return u'%s %s %s' % (self.id, self.employe, self.datedebut)

class Bloc(models.Model):
    employe = models.ForeignKey(Employe,verbose_name=u"Employé")
    date = models.DateField(verbose_name=u"Date")
    projet = models.ForeignKey(Projet,verbose_name=u"Projet")
    tache = models.ForeignKey(Tache,verbose_name=u"Tâche")
    temps = models.DecimalField(max_digits=4,decimal_places=2,verbose_name=u"Temps")
    note = models.TextField(max_length=200,blank=True,verbose_name=u"Commentaires")
    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.employe, self.date, self.projet, self.tache, self.temps)
        
    def get_Name(self):
        return self.employe.get_Name()
    get_Name.short_description = 'Nom'
    
    class Meta:
        permissions = (
                ("afficher_rapport_temps","Afficher un rapport de temps"),
        )
        
class Bloc_Banque(models.Model):
    employe = models.ForeignKey(Employe,verbose_name=u"Employé")
    date = models.DateField(verbose_name=u"Date")
    projet = models.ForeignKey(Projet,verbose_name=u"Projet")
    tache = models.ForeignKey(Tache,verbose_name=u"Tâche")
    temps = models.DecimalField(max_digits=4,decimal_places=2,verbose_name=u"Temps")
    note = models.TextField(max_length=200,blank=True,verbose_name=u"Commentaires")
    def __unicode__(self):
        return u'%s %s %s %s %s' % (self.employe, self.date, self.projet, self.tache, self.temps)
    
    def save(self, *args, **kwargs):
        employe = Employe.objects.get(id=self.employe.id)
        employe.banque_heure += self.temps
        employe.save()
        super(Bloc_Banque, self).save(*args, **kwargs)