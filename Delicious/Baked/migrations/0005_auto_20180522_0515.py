# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-22 05:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Baked', '0004_contact_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='File',
            field=models.ImageField(blank=True, upload_to='photos'),
        ),
    ]
