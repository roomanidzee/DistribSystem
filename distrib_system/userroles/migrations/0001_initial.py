# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 10:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('choose_distrib', '0001_initial'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperator',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('work', models.CharField(max_length=100)),
            ],
            options={
                'permissions': {},
                'verbose_name_plural': 'Cooperators',
                'ordering': ['name'],
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('education_course', models.CharField(max_length=100)),
            ],
            options={
                'permissions': {},
                'verbose_name_plural': 'Professors',
                'ordering': ['name'],
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='ScientificDirector',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('education_course', models.CharField(max_length=100)),
            ],
            options={
                'permissions': {},
                'verbose_name_plural': 'Scientific directors',
                'ordering': ['name'],
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('group', models.CharField(max_length=10)),
            ],
            options={
                'permissions': {},
                'verbose_name_plural': 'Students',
                'ordering': ['name'],
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('containers', models.ManyToManyField(to='choose_distrib.Container')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]