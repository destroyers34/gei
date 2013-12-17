# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categorie'
        db.create_table(u'listes_de_prix_categorie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('nom_en', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal(u'listes_de_prix', ['Categorie'])

        # Adding model 'Fournisseur'
        db.create_table(u'listes_de_prix_fournisseur', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('telephonne', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('siteweb', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('devise', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ressources.Devise'])),
            ('ratio', self.gf('django.db.models.fields.DecimalField')(default='1', max_digits=5, decimal_places=2)),
            ('ratio_us', self.gf('django.db.models.fields.DecimalField')(default='1', max_digits=5, decimal_places=2)),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'listes_de_prix', ['Fournisseur'])

        # Adding model 'Machine'
        db.create_table(u'listes_de_prix_machine', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('details', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('details_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fournisseur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['listes_de_prix.Fournisseur'])),
            ('prix_fournisseur', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('dateprix', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('escompte', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=5, decimal_places=2)),
            ('ratio', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=5, decimal_places=2)),
            ('ratio_us', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=5, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('categorie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['listes_de_prix.Categorie'])),
            ('actif', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'listes_de_prix', ['Machine'])

        # Adding model 'Option'
        db.create_table(u'listes_de_prix_option', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('details', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('details_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('fournisseur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['listes_de_prix.Fournisseur'])),
            ('prix_fournisseur', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('dateprix', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('escompte', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=5, decimal_places=2)),
            ('ratio', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=5, decimal_places=2)),
            ('ratio_us', self.gf('django.db.models.fields.DecimalField')(default='0', max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'listes_de_prix', ['Option'])

        # Adding M2M table for field machines on 'Option'
        m2m_table_name = db.shorten_name(u'listes_de_prix_option_machines')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('option', models.ForeignKey(orm[u'listes_de_prix.option'], null=False)),
            ('machine', models.ForeignKey(orm[u'listes_de_prix.machine'], null=False))
        ))
        db.create_unique(m2m_table_name, ['option_id', 'machine_id'])


    def backwards(self, orm):
        # Deleting model 'Categorie'
        db.delete_table(u'listes_de_prix_categorie')

        # Deleting model 'Fournisseur'
        db.delete_table(u'listes_de_prix_fournisseur')

        # Deleting model 'Machine'
        db.delete_table(u'listes_de_prix_machine')

        # Deleting model 'Option'
        db.delete_table(u'listes_de_prix_option')

        # Removing M2M table for field machines on 'Option'
        db.delete_table(db.shorten_name(u'listes_de_prix_option_machines'))


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