# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loggy', '0002_auto_20170317_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
