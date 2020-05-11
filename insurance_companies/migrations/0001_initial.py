# Generated by Django 2.2.10 on 2020-05-11 02:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_column='name', db_index=True, max_length=50, unique=True, verbose_name='Name')),
                ('phone_number', models.CharField(blank=True, db_column='phone_number', max_length=15, null=True, verbose_name='Phone Number')),
                ('user_creation', models.ForeignKey(blank=True, db_column='user_creation_fk', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='insurance_companies_insurance_creation', to=settings.AUTH_USER_MODEL, verbose_name='User Creation')),
                ('user_modified', models.ForeignKey(blank=True, db_column='user_modified_fk', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='insurance_companies_insurance_modified', to=settings.AUTH_USER_MODEL, verbose_name='User Modified')),
            ],
            options={
                'db_table': 'insurance',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='InsuranceConsultant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_column='name', db_index=True, max_length=50, verbose_name='Name')),
                ('phone_number', models.CharField(blank=True, db_column='phone_number', max_length=15, null=True, verbose_name='Phone Number')),
                ('insurance', models.ForeignKey(db_column='insurance_fk', on_delete=django.db.models.deletion.PROTECT, related_name='insurance_consultant_insurance', to='insurance_companies.Insurance', verbose_name='Insurance')),
                ('linked_user', models.OneToOneField(db_column='linked_user_fk', on_delete=django.db.models.deletion.PROTECT, related_name='insurance_consultant_linked_user', to=settings.AUTH_USER_MODEL, verbose_name='Linked User')),
                ('user_creation', models.ForeignKey(blank=True, db_column='user_creation_fk', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='insurance_companies_insuranceconsultant_creation', to=settings.AUTH_USER_MODEL, verbose_name='User Creation')),
                ('user_modified', models.ForeignKey(blank=True, db_column='user_modified_fk', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='insurance_companies_insuranceconsultant_modified', to=settings.AUTH_USER_MODEL, verbose_name='User Modified')),
            ],
            options={
                'db_table': 'insurance_consultant',
                'ordering': ['insurance', 'name'],
                'unique_together': {('name', 'insurance')},
            },
        ),
    ]
