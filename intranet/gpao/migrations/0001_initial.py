# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Famille'
        db.create_table(u'gpao_famille', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reference', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'gpao', ['Famille'])

        # Adding model 'Fournisseur'
        db.create_table(u'gpao_fournisseur', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'gpao', ['Fournisseur'])

        # Adding model 'Piece'
        db.create_table(u'gpao_piece', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fournisseur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gpao.Fournisseur'], null=True, blank=True)),
            ('famille', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gpao.Famille'])),
            ('reference', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('plan', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('format_papier', self.gf('django.db.models.fields.CharField')(default='LT', max_length=2)),
            ('ref_commercial', self.gf('django.db.models.fields.CharField')(default='XXX', max_length=30)),
            ('ref_mecanique', self.gf('django.db.models.fields.CharField')(default='XXX', max_length=30)),
            ('brute', self.gf('django.db.models.fields.CharField')(default='XXX', max_length=30)),
            ('soudure', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('finition', self.gf('django.db.models.fields.CharField')(default='XX', max_length=2)),
            ('commentaires', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('prix', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2)),
        ))
        db.send_create_signal(u'gpao', ['Piece'])

        # Adding model 'Pe'
        db.create_table(u'gpao_pe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reference', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('plan', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'gpao', ['Pe'])

        # Adding model 'Nm'
        db.create_table(u'gpao_nm', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reference', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('pe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gpao.Pe'], null=True, blank=True)),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('categorie', self.gf('django.db.models.fields.CharField')(default='AS', max_length=2)),
        ))
        db.send_create_signal(u'gpao', ['Nm'])

        # Adding model 'LienNM'
        db.create_table(u'gpao_liennm', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_nm', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_nm', to=orm['gpao.Nm'])),
            ('to_nm', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_nm', to=orm['gpao.Nm'])),
            ('numero_pe', self.gf('django.db.models.fields.IntegerField')(max_length=6)),
            ('quantite', self.gf('django.db.models.fields.IntegerField')(max_length=6)),
        ))
        db.send_create_signal(u'gpao', ['LienNM'])

        # Adding model 'LienPiece'
        db.create_table(u'gpao_lienpiece', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_nm', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_nm_p', to=orm['gpao.Nm'])),
            ('to_piece', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_piece', to=orm['gpao.Piece'])),
            ('numero_pe', self.gf('django.db.models.fields.IntegerField')(max_length=6)),
            ('quantite', self.gf('django.db.models.fields.IntegerField')(max_length=6)),
        ))
        db.send_create_signal(u'gpao', ['LienPiece'])


    def backwards(self, orm):
        # Deleting model 'Famille'
        db.delete_table(u'gpao_famille')

        # Deleting model 'Fournisseur'
        db.delete_table(u'gpao_fournisseur')

        # Deleting model 'Piece'
        db.delete_table(u'gpao_piece')

        # Deleting model 'Pe'
        db.delete_table(u'gpao_pe')

        # Deleting model 'Nm'
        db.delete_table(u'gpao_nm')

        # Deleting model 'LienNM'
        db.delete_table(u'gpao_liennm')

        # Deleting model 'LienPiece'
        db.delete_table(u'gpao_lienpiece')


    models = {
        u'gpao.famille': {
            'Meta': {'ordering': "['reference']", 'object_name': 'Famille'},
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'gpao.fournisseur': {
            'Meta': {'object_name': 'Fournisseur'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'gpao.liennm': {
            'Meta': {'object_name': 'LienNM'},
            'from_nm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_nm'", 'to': u"orm['gpao.Nm']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_pe': ('django.db.models.fields.IntegerField', [], {'max_length': '6'}),
            'quantite': ('django.db.models.fields.IntegerField', [], {'max_length': '6'}),
            'to_nm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_nm'", 'to': u"orm['gpao.Nm']"})
        },
        u'gpao.lienpiece': {
            'Meta': {'object_name': 'LienPiece'},
            'from_nm': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_nm_p'", 'to': u"orm['gpao.Nm']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero_pe': ('django.db.models.fields.IntegerField', [], {'max_length': '6'}),
            'quantite': ('django.db.models.fields.IntegerField', [], {'max_length': '6'}),
            'to_piece': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_piece'", 'to': u"orm['gpao.Piece']"})
        },
        u'gpao.nm': {
            'Meta': {'ordering': "['reference']", 'object_name': 'Nm'},
            'categorie': ('django.db.models.fields.CharField', [], {'default': "'AS'", 'max_length': '2'}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liens': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_to'", 'symmetrical': 'False', 'through': u"orm['gpao.LienNM']", 'to': u"orm['gpao.Nm']"}),
            'liens_piece': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_piece'", 'symmetrical': 'False', 'through': u"orm['gpao.LienPiece']", 'to': u"orm['gpao.Piece']"}),
            'pe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gpao.Pe']", 'null': 'True', 'blank': 'True'}),
            'reference': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'gpao.pe': {
            'Meta': {'ordering': "['reference']", 'object_name': 'Pe'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plan': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'reference': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'gpao.piece': {
            'Meta': {'ordering': "['reference']", 'object_name': 'Piece'},
            'brute': ('django.db.models.fields.CharField', [], {'default': "'XXX'", 'max_length': '30'}),
            'commentaires': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'famille': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gpao.Famille']"}),
            'finition': ('django.db.models.fields.CharField', [], {'default': "'XX'", 'max_length': '2'}),
            'format_papier': ('django.db.models.fields.CharField', [], {'default': "'LT'", 'max_length': '2'}),
            'fournisseur': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gpao.Fournisseur']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plan': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'prix': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'}),
            'ref_commercial': ('django.db.models.fields.CharField', [], {'default': "'XXX'", 'max_length': '30'}),
            'ref_mecanique': ('django.db.models.fields.CharField', [], {'default': "'XXX'", 'max_length': '30'}),
            'reference': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'soudure': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['gpao']