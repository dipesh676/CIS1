# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 10:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Criminals', '0003_auto_20160826_1010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='victim',
            old_name='victim',
            new_name='case_no',
        ),
    ]
