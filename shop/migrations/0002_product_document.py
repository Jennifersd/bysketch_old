# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-20 20:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='document',
            field=models.FileField(blank=True, upload_to='downloads/%Y/%m/%d'),
        ),
    ]
