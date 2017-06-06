# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'Profil', 'verbose_name_plural': 'Profile'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='position',
            field=models.CharField(default='', max_length=100, verbose_name='Stanowisko'),
        ),
    ]
