# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 22:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loggy', '0004_auto_20170318_2200'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user_student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='loggy.User'),
            preserve_default=False,
        ),
    ]