# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 21:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20170128_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nr_st',
            name='photo',
            field=models.ImageField(null=True, upload_to='static/img'),
        ),
    ]
