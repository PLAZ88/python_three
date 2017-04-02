# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg', '0001_initial'),
        ('quote', '0002_quote_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='quote',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='users',
        ),
        migrations.AddField(
            model_name='favorite',
            name='quote',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quote_favorite', to='quote.Quote'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='user_favorites', to='log_reg.User'),
        ),
    ]