# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-03 11:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BBproj', '0008_auto_20170103_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timestamp',
            name='userp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
