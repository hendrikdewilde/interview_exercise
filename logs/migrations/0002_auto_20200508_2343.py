# Generated by Django 2.2.10 on 2020-05-08 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smslogging',
            name='from_number',
            field=models.CharField(blank=True, db_column='from_number', max_length=15, null=True, verbose_name='From number'),
        ),
        migrations.AlterField(
            model_name='smslogging',
            name='to_number',
            field=models.CharField(blank=True, db_column='to_number', max_length=15, null=True, verbose_name='To number'),
        ),
    ]
