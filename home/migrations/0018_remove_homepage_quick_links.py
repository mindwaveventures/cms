# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-22 11:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_homepage_quick_links'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='quick_links',
        ),
    ]
