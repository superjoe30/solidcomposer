# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Profile.tips_on'
        db.add_column('main_profile', 'tips_on', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Profile.tips_on'
        db.delete_column('main_profile', 'tips_on')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'chat.chatroom': {
            'Meta': {'object_name': 'ChatRoom'},
            'blacklist': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'blacklisted_users'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permission_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'whitelist': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'whitelisted_users'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['auth.User']"})
        },
        'competitions.competition': {
            'Meta': {'object_name': 'Competition'},
            'chat_room': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['chat.ChatRoom']", 'null': 'True', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'have_listening_party': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'host': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'listening_party_end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'listening_party_start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'preview_rules': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'preview_theme': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'rules': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'submit_deadline': ('django.db.models.fields.DateTimeField', [], {}),
            'theme': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'vote_deadline': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'vote_period_length': ('django.db.models.fields.BigIntegerField', [], {})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.accountplan': {
            'Meta': {'object_name': 'AccountPlan'},
            'band_count_limit': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'total_space': ('django.db.models.fields.BigIntegerField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'usd_per_month': ('django.db.models.fields.FloatField', [], {})
        },
        'main.band': {
            'Meta': {'object_name': 'Band'},
            'abandon_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'concurrent_editing': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'openness': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'total_space': ('django.db.models.fields.BigIntegerField', [], {}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '110', 'unique': 'True', 'null': 'True'}),
            'used_space': ('django.db.models.fields.BigIntegerField', [], {'default': '0'})
        },
        'main.bandmember': {
            'Meta': {'object_name': 'BandMember'},
            'band': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Band']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'space_donated': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'main.profile': {
            'Meta': {'object_name': 'Profile'},
            'account_expire_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'activate_code': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'activated': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'active_transaction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Transaction']", 'null': 'True', 'blank': 'True'}),
            'assume_uploaded_plugins_owned': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'band_count_limit': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'competitions_bookmarked': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'competitions_bookmarked'", 'blank': 'True', 'to': "orm['competitions.Competition']"}),
            'date_activity': ('django.db.models.fields.DateTimeField', [], {}),
            'email_newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'email_notifications': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.AccountPlan']", 'null': 'True', 'blank': 'True'}),
            'plugins': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'profile_plugins'", 'blank': 'True', 'to': "orm['workshop.PluginDepenency']"}),
            'purchased_bytes': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'solo_band': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Band']"}),
            'studios': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'profile_studios'", 'blank': 'True', 'to': "orm['workshop.Studio']"}),
            'tips_on': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'usd_per_month': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'main.song': {
            'Meta': {'object_name': 'Song'},
            'album': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'band': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Band']"}),
            'comment_node': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'song_comment_node'", 'null': 'True', 'to': "orm['main.SongCommentNode']"}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_open_for_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_open_source': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {}),
            'mp3_file': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'plugins': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'song_plugins'", 'blank': 'True', 'to': "orm['workshop.PluginDepenency']"}),
            'source_file': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'studio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workshop.Studio']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'waveform_img': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        },
        'main.songcommentnode': {
            'Meta': {'object_name': 'SongCommentNode'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '9000', 'blank': 'True'}),
            'date_created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_edited': ('django.db.models.fields.DateTimeField', [], {}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.SongCommentNode']", 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'reply_disabled': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Song']", 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workshop.ProjectVersion']", 'null': 'True', 'blank': 'True'})
        },
        'main.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'main.tempfile': {
            'Meta': {'object_name': 'TempFile'},
            'death_time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2010, 8, 27, 16, 6, 27, 454338)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'main.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'amount': ('django.db.models.fields.FloatField', [], {}),
            'confirmed': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'expiry': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.AccountPlan']"}),
            'request_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'token_id': ('django.db.models.fields.CharField', [], {'max_length': '65', 'null': 'True', 'blank': 'True'}),
            'transaction_id': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'workshop.plugindepenency': {
            'Meta': {'object_name': 'PluginDepenency'},
            'comes_with_studio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workshop.Studio']", 'null': 'True', 'blank': 'True'}),
            'external_url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'plugin_type': ('django.db.models.fields.IntegerField', [], {}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'screenshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '256'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'workshop.project': {
            'Meta': {'object_name': 'Project'},
            'band': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Band']"}),
            'checked_out_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'checked_out_to'", 'null': 'True', 'to': "orm['auth.User']"}),
            'date_activity': ('django.db.models.fields.DateTimeField', [], {}),
            'date_checked_out': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'forked_from': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'forked_from'", 'null': 'True', 'to': "orm['workshop.ProjectVersion']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latest_version': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'latest_version'", 'null': 'True', 'to': "orm['workshop.ProjectVersion']"}),
            'merged_from': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'merged_from'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['workshop.ProjectVersion']"}),
            'promote_voters': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'promote_voters'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'scrap_voters': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'scrap_voters'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'project_subscribers'", 'blank': 'True', 'to': "orm['auth.User']"}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['main.Tag']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'visible': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'})
        },
        'workshop.projectversion': {
            'Meta': {'object_name': 'ProjectVersion'},
            'comment_node': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.SongCommentNode']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'new_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'old_title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workshop.Project']"}),
            'provided_samples': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'provided_samples'", 'blank': 'True', 'to': "orm['workshop.UploadedSample']"}),
            'song': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Song']", 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {})
        },
        'workshop.samplefile': {
            'Meta': {'object_name': 'SampleFile'},
            'hex_digest': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mp3_preview': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'workshop.studio': {
            'Meta': {'object_name': 'Studio'},
            'canMerge': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'canReadFile': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'canRender': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'external_url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'logo_16x16': ('django.db.models.fields.files.ImageField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'logo_large': ('django.db.models.fields.files.ImageField', [], {'max_length': '512', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'workshop.uploadedsample': {
            'Meta': {'object_name': 'UploadedSample'},
            'band': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Band']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sample_file': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['workshop.SampleFile']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['main']
