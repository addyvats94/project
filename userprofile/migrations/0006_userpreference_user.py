# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-01 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0005_auto_20170301_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpreference',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.User'),
        ),
    ]