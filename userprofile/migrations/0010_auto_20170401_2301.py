# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-01 17:31
from __future__ import unicode_literals

from django.db import migrations
import userprofile.manager


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_auto_20170401_1209'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', userprofile.manager.CustomUserManager()),
            ],
        ),
    ]