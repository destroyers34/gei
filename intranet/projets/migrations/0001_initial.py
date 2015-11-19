# -*- coding: utf-8 -*-
from south.db import db
from south.utils import datetime_utils as datetime
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Projet_Eugenie'
        db.create_table(u'projets_projet_eugenie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('nom', self.gf('django.db.models.fields.CharField')(default='X', max_length=30)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clients.Compagnie'], null=True, blank=True)),
            ('date_soumission', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_debut', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2015, 11, 18, 0, 0))),
            ('date_fin', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2015, 11, 18, 0, 0))),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('en_attente', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('modele', self.gf('django.db.models.fields.CharField')(default='X', max_length=30)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('budget_mat', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=11, decimal_places=2)),
            ('budget_mo', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=11, decimal_places=2)),
            ('priority', self.gf('django.db.models.fields.DecimalField')(default='9', max_digits=2, decimal_places=0)),
        ))
        db.send_create_signal(u'projets', ['Projet_Eugenie'])

        # Adding model 'Projet_TPE'
        db.create_table(u'projets_projet_tpe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('nom', self.gf('django.db.models.fields.CharField')(default='X', max_length=30)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clients.Compagnie'], null=True, blank=True)),
            ('date_soumission', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_debut', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2015, 11, 18, 0, 0))),
            ('date_fin', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2015, 11, 18, 0, 0))),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('en_attente', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('description', self.gf('django.db.models.fields.CharField')(default='X', max_length=30)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('budget_mat', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=11, decimal_places=2)),
            ('budget_mo', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=11, decimal_places=2)),
        ))
        db.send_create_signal(u'projets', ['Projet_TPE'])


    def backwards(self, orm):
        # Deleting model 'Projet_Eugenie'
        db.delete_table(u'projets_projet_eugenie')

        # Deleting model 'Projet_TPE'
        db.delete_table(u'projets_projet_tpe')


    models = {
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
            'date_debut': (
            'django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2015, 11, 18, 0, 0)'}),
            'date_fin': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2015, 11, 18, 0, 0)'}),
            'date_soumission': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'en_attente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modele': ('django.db.models.fields.CharField', [], {'default': "'X'", 'max_length': '30'}),
            'nom': ('django.db.models.fields.CharField', [], {'default': "'X'", 'max_length': '30'}),
            'numero': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'priority': ('django.db.models.fields.DecimalField', [], {'default': "'9'", 'max_digits': '2', 'decimal_places': '0'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'projets.projet_tpe': {
            'Meta': {'ordering': "['-numero']", 'object_name': 'Projet_TPE'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'budget_mat': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '11', 'decimal_places': '2'}),
            'budget_mo': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '11', 'decimal_places': '2'}),
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clients.Compagnie']", 'null': 'True', 'blank': 'True'}),
            'date_debut': (
            'django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2015, 11, 18, 0, 0)'}),
            'date_fin': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2015, 11, 18, 0, 0)'}),
            'date_soumission': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'X'", 'max_length': '30'}),
            'en_attente': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'default': "'X'", 'max_length': '30'}),
            'numero': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['projets']