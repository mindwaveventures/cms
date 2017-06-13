# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-08 14:11
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20170607_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='crisis_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Label for sleep crisis page link'),
        ),
    ]