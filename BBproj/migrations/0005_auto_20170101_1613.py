# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-01 10:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BBproj', '0004_auto_20170101_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='userpp',
        ),
        migrations.AddField(
            model_name='work',
            name='userpp',
            field=models.ManyToManyField(null=True, related_name='userpp', to=settings.AUTH_USER_MODEL),
        ),
    ]
