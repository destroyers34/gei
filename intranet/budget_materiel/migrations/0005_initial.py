# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categorie'
        db.create_table(u'budget_materiel_categorie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'budget_materiel', ['Categorie'])

        # Adding model 'Fournisseur'
        db.create_table(u'budget_materiel_fournisseur', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('categorie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['budget_materiel.Categorie'])),
        ))
        db.send_create_signal(u'budget_materiel', ['Fournisseur'])

        # Adding model 'Materiel_Eugenie'
        db.create_table(u'budget_materiel_materiel_eugenie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('projet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projets.Projet_Eugenie'])),
            ('fournisseur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['budget_materiel.Fournisseur'], null=True)),
            ('montant', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
        ))
        db.send_create_signal(u'budget_materiel', ['Materiel_Eugenie'])


    def backwards(self, orm):
        # Deleting model 'Categorie'
        db.delete_table(u'budget_materiel_categorie')

        # Deleting model 'Fournisseur'
        db.delete_table(u'budget_materiel_fournisseur')

        # Deleting model 'Materiel_Eugenie'
        db.delete_table(u'budget_materiel_materiel_eugenie')


    models = {
        u'budget_materiel.categorie': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Categorie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        u'budget_materiel.fournisseur': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Fournisseur'},
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['budget_materiel.Categorie']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'budget_materiel.materiel_eugenie': {
            'Meta': {'object_name': 'Materiel_Eugenie'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'fournisseur': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['budget_materiel.Fournisseur']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'montant': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'projet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projets.Projet_Eugenie']"})
        },
        u'clients.compagnie': {
            'Meta': {'object_name': 'Compagnie'},
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pays': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'province_etat': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'telephonne': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'ville': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'projets.projet_eugenie': {
            'Meta': {'ordering': "['-numero']", 'object_name': 'Projet_Eugenie'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'budget_mat': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '11', 'decimal_places': '2'}),
            'budget_mo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '11', 'decimal_places': '2'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clients.Compagnie']", 'null': 'True', 'blank': 'True'}),
            'date_debut': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 11, 6, 0, 0)'}),
            'date_fin': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 11, 6, 0, 0)'}),
            'date_soumission': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'en_attente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modele': ('django.db.models.fields.CharField', [], {'default': "'X'", 'max_length': '30'}),
            'nom': ('django.db.models.fields.CharField', [], {'default': "'X'", 'max_length': '30'}),
            'numero': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'priority': ('django.db.models.fields.DecimalField', [], {'default': "'9'", 'max_digits': '2', 'decimal_places': '0'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['budget_materiel']