# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-28 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='nick_name',
            field=models.CharField(default=True, max_length=50),
        ),
    ]