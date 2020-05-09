# Generated by Django 2.2 on 2020-05-08 01:33

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('ip_address', models.CharField(db_column='ip_address', max_length=255, unique=True, verbose_name='IP Address')),
                ('reason_for_block', models.TextField(blank=True, help_text='Optional reason for block', null=True)),
            ],
            options={
                'verbose_name': 'IPs to ban',
                'db_table': 'block_ip',
                'ordering': ['-date_creation'],
            },
        ),
        migrations.CreateModel(
            name='SafeIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('ip_address', models.CharField(db_column='ip_address', max_length=255, unique=True, verbose_name='IP Address')),
                ('reason_for_allow', models.TextField(blank=True, help_text='Optional reason to always Allow', null=True)),
            ],
            options={
                'verbose_name': 'IPs to always Allow',
                'db_table': 'save_ip',
                'ordering': ['-date_creation'],
            },
        ),
        migrations.CreateModel(
            name='StreamLogging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('level', models.CharField(blank=True, max_length=255, null=True)),
                ('traceback', models.TextField(blank=True, null=True)),
                ('error_time', models.DateTimeField(auto_now_add=True)),
                ('file_name', models.CharField(blank=True, max_length=255, null=True)),
                ('func_name', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('process_id', models.CharField(blank=True, max_length=255, null=True)),
                ('process_name', models.CharField(blank=True, max_length=255, null=True)),
                ('process_args', models.CharField(blank=True, max_length=255, null=True)),
                ('ip_address', models.CharField(blank=True, db_column='ip', max_length=255, null=True, verbose_name='IP')),
            ],
            options={
                'db_table': 'stream_logging',
                'ordering': ['-date_creation'],
            },
        ),
        migrations.CreateModel(
            name='UserLogging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(blank=True, db_column='username', max_length=255, null=True, verbose_name='UserName')),
                ('session_id', models.CharField(blank=True, db_column='session_id', max_length=45, null=True, verbose_name='Session ID')),
                ('access_token', models.CharField(blank=True, db_column='access_token', max_length=45, null=True, verbose_name='Access Token')),
                ('ip_address', models.CharField(blank=True, db_column='ip_address', max_length=255, null=True, verbose_name='IP Address')),
                ('host', models.CharField(blank=True, db_column='host', max_length=255, null=True, verbose_name='Host')),
                ('success', models.BooleanField(blank=True, db_column='success', default=False, verbose_name='Success')),
                ('user', models.ForeignKey(blank=True, db_column='user_fk', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_login_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'db_table': 'user_login',
                'ordering': ['-date_creation'],
            },
        ),
        migrations.CreateModel(
            name='SmsLogging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('from_number', models.CharField(blank=True, db_column='from_number', max_length=10, null=True, verbose_name='From number')),
                ('to_number', models.CharField(blank=True, db_column='to_number', max_length=10, null=True, verbose_name='To number')),
                ('message', models.CharField(blank=True, db_column='message', max_length=255, null=True, verbose_name='Message')),
                ('sms_id', models.CharField(blank=True, db_column='sms_id', max_length=255, null=True, verbose_name='SMS Id')),
                ('user', models.ForeignKey(blank=True, db_column='user_fk', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sms_logging_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'db_table': 'sms_logging',
                'ordering': ['-date_creation'],
            },
        ),
        migrations.CreateModel(
            name='ApiLogging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, db_column='status', db_index=True, max_length=5, null=True, verbose_name='Status')),
                ('method', models.CharField(blank=True, db_column='method', max_length=50, null=True, verbose_name='Method')),
                ('path', models.CharField(blank=True, db_column='path', max_length=255, null=True, verbose_name='Path')),
                ('ip_address', models.CharField(blank=True, db_column='ip', max_length=255, null=True, verbose_name='IP')),
                ('host', models.CharField(blank=True, db_column='host', max_length=255, null=True, verbose_name='Host')),
                ('cookie', models.CharField(blank=True, db_column='cookie', max_length=255, null=True, verbose_name='Cookie')),
                ('params', django.contrib.postgres.fields.jsonb.JSONField(blank=True, db_column='params', null=True, verbose_name='Params')),
                ('user', models.ForeignKey(blank=True, db_column='user_fk', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='api_logging_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'db_table': 'api_logging',
                'ordering': ['-date_creation'],
            },
        ),
    ]