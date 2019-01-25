# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-05-14 13:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackpage',
            name='hero_image',
            field=models.ForeignKey(blank=True, help_text='\n            Max file size: 10MB. Choose from: JPEG, PNG\n        ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
