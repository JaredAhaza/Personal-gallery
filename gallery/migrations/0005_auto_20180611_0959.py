# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-11 06:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20180609_1411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='locaton',
            new_name='location',
        ),
    ]
