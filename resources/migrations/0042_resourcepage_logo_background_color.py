# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-04-19 11:21
from __future__ import unicode_literals

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0041_merge_20180419_0636'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcepage',
            name='logo_background_color',
            field=colorful.fields.RGBColorField(blank=True, default='#ffffff', help_text='The background colour of brand_logo', null=True),
        ),
    ]
