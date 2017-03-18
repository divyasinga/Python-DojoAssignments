# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 23:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loggy', '0004_auto_20170318_2200'),
        ('courses', '0002_course_user_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='user_student',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='course_enrolled',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='user_student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loggy.User'),
        ),
    ]
