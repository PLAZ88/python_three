# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg', '0001_initial'),
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_quotes', to='log_reg.User'),
        ),
    ]
