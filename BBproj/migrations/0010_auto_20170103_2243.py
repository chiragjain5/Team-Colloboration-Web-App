# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-03 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBproj', '0009_auto_20170103_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timestamp',
            name='Logintime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='Logouttime',
            field=models.TimeField(),
        ),
    ]
