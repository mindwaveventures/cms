# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-04 14:56
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0020_auto_20170904_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='description',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='\n        A short description of the page that will show on the homepage'),
        ),
        migrations.AddField(
            model_name='home',
            name='link_text',
            field=models.TextField(blank=True, help_text='Text to display for the link to this page'),
        ),
    ]