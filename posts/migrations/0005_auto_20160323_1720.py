# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-24 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20160323_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateField(),
        ),
    ]
