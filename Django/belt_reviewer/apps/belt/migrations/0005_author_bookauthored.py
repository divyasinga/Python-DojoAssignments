# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-21 17:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt', '0004_remove_author_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='bookauthored',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookauthored', to='belt.Book'),
        ),
    ]
