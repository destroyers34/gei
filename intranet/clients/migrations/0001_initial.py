# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Compagnie'
        db.create_table(u'clients_compagnie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('adresse', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('ville', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('province_etat', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('pays', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('telephonne', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'clients', ['Compagnie'])

        # Adding model 'Contact'
        db.create_table(u'clients_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('fonction', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('telephonne', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('compagnie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clients.Compagnie'])),
        ))
        db.send_create_signal(u'clients', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Compagnie'
        db.delete_table(u'clients_compagnie')

        # Deleting model 'Contact'
        db.delete_table(u'clients_contact')


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
        u'clients.contact': {
            'Meta': {'ordering': "['prenom', 'nom']", 'object_name': 'Contact'},
            'compagnie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clients.Compagnie']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'fonction': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'telephonne': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        }
    }

    complete_apps = ['clients']