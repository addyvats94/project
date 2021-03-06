# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-26 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0002_auto_20170226_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photos', models.ImageField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel_name', models.CharField(max_length=100, null=True)),
                ('rooms', models.IntegerField(null=True)),
                ('warden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.User')),
            ],
        ),
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notices', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField(blank=True, null=True)),
                ('floor', models.CharField(choices=[(0, 'Ground Floor'), (1, '1st Floor'), (2, '2nd Floor'), (3, '3rd Floor'), (4, '4th Floor')], default=1, max_length=15)),
                ('is_vacant', models.BooleanField(default=False)),
                ('room_size', models.CharField(choices=[(1, 'Single Seater'), (2, 'Double Seater'), (3, 'Triple Seater')], default=1, max_length=15)),
                ('room_type', models.CharField(choices=[('NON-AC', 'NON-AC'), ('AC', 'AC')], default='NON_AC', max_length=15)),
                ('allocated_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.User')),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HostelActivities.Hostel')),
            ],
        ),
    ]
