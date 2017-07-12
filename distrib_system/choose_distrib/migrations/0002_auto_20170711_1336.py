# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('choose_distrib', '0001_initial'),
        ('userroles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userroles.UserProfile'),
        ),
        migrations.AddField(
            model_name='container',
            name='container_director',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userroles.UserProfile'),
        ),
    ]