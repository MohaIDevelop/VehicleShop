# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20171216_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle_image'),
        ),
    ]