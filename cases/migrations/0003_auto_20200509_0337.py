# Generated by Django 2.2.10 on 2020-05-09 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file_name',
            field=models.FileField(upload_to=''),
        ),
    ]