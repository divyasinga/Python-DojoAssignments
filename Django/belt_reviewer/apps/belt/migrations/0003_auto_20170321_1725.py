# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 17:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0002_auto_20170321_1705'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author',
            new_name='book',
        ),
    ]
