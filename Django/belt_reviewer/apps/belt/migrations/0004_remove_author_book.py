# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 17:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0003_auto_20170321_1725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='book',
        ),
    ]
