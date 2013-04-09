# -*- coding: utf8 -*-
from django.db import models

# Create your models here.

class Client(models.Model):
	compagnie = models.CharField(max_length=50,verbose_name=u"Compagnie")
	adresse = models.CharField(max_length=50,verbose_name=u"Adresse", blank=True)
	ville = models.CharField(max_length=50,verbose_name=u"Ville", blank=True)
	province_etat = models.CharField(max_length=50,verbose_name=u"Province/État", blank=True)
	postal_code = models.CharField(max_length=50,verbose_name=u"Code Postal", blank=True)
	pays = models.CharField(max_length=50,verbose_name=u"Pays", blank=True)
	telephonne = models.CharField(max_length=50,verbose_name=u"Téléphonne", blank=True)
	fax = models.CharField(max_length=50,verbose_name=u"Fax", blank=True)
	
	def __unicode__(self):
		return u'%s' % (self.compagnie)

	class Meta:
		verbose_name = u"Client"