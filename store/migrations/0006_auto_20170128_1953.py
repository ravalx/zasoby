# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20170128_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nr_st',
            name='value_product',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
