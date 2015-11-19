# -*- coding: utf-8 -*-
from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Bloc_Eugenie'
        db.create_table(u'feuilles_de_temps_bloc_eugenie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ressources.Employe'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('tache', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ressources.Tache'])),
            ('temps', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('note', self.gf('django.db.models.fields.TextField')(max_length=200, blank=True)),
            ('banque', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('approuve', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('projet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projets.Projet_Eugenie'])),
        ))
        db.send_create_signal(u'feuilles_de_temps', ['Bloc_Eugenie'])

        # Adding model 'Bloc_TPE'
        db.create_table(u'feuilles_de_temps_bloc_tpe', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ressources.Employe'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('tache', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ressources.Tache'])),
            ('temps', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('note', self.gf('django.db.models.fields.TextField')(max_length=200, blank=True)),
            ('banque', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('approuve', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('projet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['projets.Projet_TPE'])),
        ))
        db.send_create_signal(u'feuilles_de_temps', ['Bloc_TPE'])

        # Adding model 'Banque'
        db.create_table(u'feuilles_de_temps_banque', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('employe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ressources.Employe'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('temps', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal(u'feuilles_de_temps', ['Banque'])


    def backwards(self, orm):
        # Deleting model 'Bloc_Eugenie'
        db.delete_table(u'feuilles_de_temps_bloc_eugenie')

        # Deleting model 'Bloc_TPE'
        db.delete_table(u'feuilles_de_temps_bloc_tpe')

        # Deleting model 'Banque'
        db.delete_table(u'feuilles_de_temps_banque')


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
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'feuilles_de_temps.banque': {
            'Meta': {'object_name': 'Banque'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'employe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ressources.Employe']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'temps': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        },
        u'feuilles_de_temps.bloc_eugenie': {
            'Meta': {'object_name': 'Bloc_Eugenie'},
            'approuve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'banque': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'employe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ressources.Employe']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'max_length': '200', 'blank': 'True'}),
            'projet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projets.Projet_Eugenie']"}),
            'tache': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ressources.Tache']"}),
            'temps': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
        },
        u'feuilles_de_temps.bloc_tpe': {
            'Meta': {'object_name': 'Bloc_TPE'},
            'approuve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'banque': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'employe': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ressources.Employe']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'max_length': '200', 'blank': 'True'}),
            'projet': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['projets.Projet_TPE']"}),
            'tache': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ressources.Tache']"}),
            'temps': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'})
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
        },
        u'ressources.compagnie': {
            'Meta': {'object_name': 'Compagnie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '60'})
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

    complete_apps = ['feuilles_de_temps']