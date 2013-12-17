# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Option.options'
        db.add_column(u'listes_de_prix_option', 'options',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Machine.options'
        db.add_column(u'listes_de_prix_machine', 'options',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Option.options'
        db.delete_column(u'listes_de_prix_option', 'options')

        # Deleting field 'Machine.options'
        db.delete_column(u'listes_de_prix_machine', 'options')


    models = {
        u'listes_de_prix.categorie': {
            'Meta': {'ordering': "['nom', 'nom_en']", 'object_name': 'Categorie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'nom_en': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'listes_de_prix.fournisseur': {
            'Meta': {'ordering': "['nom']", 'object_name': 'Fournisseur'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'devise': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ressources.Devise']"}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ratio': ('django.db.models.fields.DecimalField', [], {'default': "'1'", 'max_digits': '5', 'decimal_places': '2'}),
            'ratio_us': ('django.db.models.fields.DecimalField', [], {'default': "'1'", 'max_digits': '5', 'decimal_places': '2'}),
            'siteweb': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'telephonne': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'listes_de_prix.machine': {
            'Meta': {'ordering': "['numero']", 'object_name': 'Machine'},
            'actif': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'categorie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listes_de_prix.Categorie']"}),
            'dateprix': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'details_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'escompte': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '5', 'decimal_places': '2'}),
            'fournisseur': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listes_de_prix.Fournisseur']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'options': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prix_fournisseur': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'ratio': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '5', 'decimal_places': '2'}),
            'ratio_us': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '5', 'decimal_places': '2'})
        },
        u'listes_de_prix.option': {
            'Meta': {'ordering': "['numero']", 'object_name': 'Option'},
            'dateprix': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'details_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'escompte': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '5', 'decimal_places': '2'}),
            'fournisseur': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['listes_de_prix.Fournisseur']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'machines': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'options_machine'", 'symmetrical': 'False', 'to': u"orm['listes_de_prix.Machine']"}),
            'numero': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'options': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'prix_fournisseur': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'ratio': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '5', 'decimal_places': '2'}),
            'ratio_us': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '5', 'decimal_places': '2'})
        },
        u'ressources.devise': {
            'Meta': {'object_name': 'Devise'},
            'code_iso': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'date_taux': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'symbole': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'taux_inverse': ('django.db.models.fields.DecimalField', [], {'default': "'1'", 'max_digits': '13', 'decimal_places': '10'}),
            'taux_toCAD': ('django.db.models.fields.DecimalField', [], {'default': "'1'", 'max_digits': '13', 'decimal_places': '10'})
        }
    }

    complete_apps = ['listes_de_prix']