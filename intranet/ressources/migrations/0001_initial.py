# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Compagnie'
        db.create_table(u'ressources_compagnie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal(u'ressources', ['Compagnie'])

        # Adding model 'Employe'
        db.create_table(u'ressources_employe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('compagnie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ressources.Compagnie'], null=True, blank=True)),
            ('hire_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('banque_heure', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=11, decimal_places=2)),
            ('taux_horaire', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=6, decimal_places=2)),
            ('superviseur', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ressources.Employe'], null=True, blank=True)),
        ))
        db.send_create_signal(u'ressources', ['Employe'])

        # Adding model 'Devise'
        db.create_table(u'ressources_devise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('code_iso', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('symbole', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('taux_toCAD', self.gf('django.db.models.fields.DecimalField')(default='1', max_digits=13, decimal_places=10)),
            ('taux_inverse', self.gf('django.db.models.fields.DecimalField')(default='1', max_digits=13, decimal_places=10)),
            ('date_taux', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'ressources', ['Devise'])

        # Adding model 'Tache'
        db.create_table(u'ressources_tache', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('numero', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('type', self.gf('django.db.models.fields.CharField')(default='PO', max_length=2)),
        ))
        db.send_create_signal(u'ressources', ['Tache'])


    def backwards(self, orm):
        # Deleting model 'Compagnie'
        db.delete_table(u'ressources_compagnie')

        # Deleting model 'Employe'
        db.delete_table(u'ressources_employe')

        # Deleting model 'Devise'
        db.delete_table(u'ressources_devise')

        # Deleting model 'Tache'
        db.delete_table(u'ressources_tache')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ressources.compagnie': {
            'Meta': {'object_name': 'Compagnie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60'})
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
        },
        u'ressources.employe': {
            'Meta': {'ordering': "['user__first_name']", 'object_name': 'Employe'},
            'banque_heure': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '11', 'decimal_places': '2'}),
            'compagnie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ressources.Compagnie']", 'null': 'True', 'blank': 'True'}),
            'hire_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'superviseur': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ressources.Employe']", 'null': 'True', 'blank': 'True'}),
            'taux_horaire': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '6', 'decimal_places': '2'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'ressources.tache': {
            'Meta': {'ordering': "['numero']", 'object_name': 'Tache'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'numero': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'PO'", 'max_length': '2'})
        }
    }

    complete_apps = ['ressources']