# Generated by Django 2.2.10 on 2020-05-11 02:23

import claims.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('insurance_assessor', '0001_initial'),
        ('insurance_companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('case_number', models.CharField(db_column='case_number', db_index=True, max_length=50, unique=True, verbose_name='Case Number')),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Close', 'Close')], db_column='status', max_length=10, verbose_name='Status')),
                ('open_date', models.DateField(db_column='open_date', verbose_name='Open Date')),
                ('close_date', models.DateField(blank=True, db_column='close_date', null=True, verbose_name='Close Date')),
                ('description', models.TextField(blank=True, db_column='description', null=True, verbose_name='Description')),
                ('resolution', models.TextField(blank=True, db_column='resolution', null=True, verbose_name='Resolution')),
                ('assessor', models.ForeignKey(db_column='assessor_fk', on_delete=django.db.models.deletion.PROTECT, related_name='case_assessor', to='insurance_assessor.Assessor', verbose_name='Assessor')),
            ],
            options={
                'db_table': 'case',
                'ordering': ['case_number'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('document_type', models.CharField(choices=[('Quote', 'Quote'), ('Cover Document', 'Cover Document')], db_column='document_type', max_length=50, verbose_name='Document Type')),
                ('name', models.CharField(db_column='name', max_length=50, verbose_name='Name')),
                ('file_name', models.FileField(upload_to=claims.models.Case.case_directory_path)),
                ('case', models.ForeignKey(db_column='case_fk', on_delete=django.db.models.deletion.PROTECT, related_name='document_case', to='claims.Case', verbose_name='Case')),
                ('user_creation', models.ForeignKey(blank=True, db_column='user_creation_fk', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='claims_document_creation', to=settings.AUTH_USER_MODEL, verbose_name='User Creation')),
                ('user_modified', models.ForeignKey(blank=True, db_column='user_modified_fk', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='claims_document_modified', to=settings.AUTH_USER_MODEL, verbose_name='User Modified')),
            ],
            options={
                'db_table': 'document',
                'ordering': ['case', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('client_number', models.IntegerField(db_column='client_number', db_index=True, unique=True, verbose_name='Client Number')),
                ('name', models.CharField(db_column='name', max_length=50, verbose_name='Name')),
                ('phone_number', models.CharField(blank=True, db_column='phone_number', max_length=15, null=True, verbose_name='Phone Number')),
                ('address', models.TextField(blank=True, db_column='address', null=True, verbose_name='Address')),
                ('user_creation', models.ForeignKey(blank=True, db_column='user_creation_fk', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='claims_client_creation', to=settings.AUTH_USER_MODEL, verbose_name='User Creation')),
                ('user_modified', models.ForeignKey(blank=True, db_column='user_modified_fk', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='claims_client_modified', to=settings.AUTH_USER_MODEL, verbose_name='User Modified')),
            ],
            options={
                'db_table': 'client',
                'ordering': ['client_number'],
            },
        ),
        migrations.AddField(
            model_name='case',
            name='client',
            field=models.ForeignKey(db_column='client_fk', on_delete=django.db.models.deletion.PROTECT, related_name='case_client', to='claims.Client', verbose_name='Client'),
        ),
        migrations.AddField(
            model_name='case',
            name='insurance',
            field=models.ForeignKey(db_column='insurance_fk', on_delete=django.db.models.deletion.PROTECT, related_name='case_insurance', to='insurance_companies.Insurance', verbose_name='Insurance'),
        ),
        migrations.AddField(
            model_name='case',
            name='insurance_consultant',
            field=models.ForeignKey(db_column='insurance_consultant_fk', on_delete=django.db.models.deletion.PROTECT, related_name='case_insurance_consultant', to='insurance_companies.InsuranceConsultant', verbose_name='Insurance Consultant'),
        ),
        migrations.AddField(
            model_name='case',
            name='user_creation',
            field=models.ForeignKey(blank=True, db_column='user_creation_fk', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='claims_case_creation', to=settings.AUTH_USER_MODEL, verbose_name='User Creation'),
        ),
        migrations.AddField(
            model_name='case',
            name='user_modified',
            field=models.ForeignKey(blank=True, db_column='user_modified_fk', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='claims_case_modified', to=settings.AUTH_USER_MODEL, verbose_name='User Modified'),
        ),
    ]
