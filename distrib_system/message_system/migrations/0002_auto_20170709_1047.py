# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-09 07:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message_system', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
