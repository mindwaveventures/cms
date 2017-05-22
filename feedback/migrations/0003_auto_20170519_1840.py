# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-19 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20170519_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbackpage',
            name='intro',
        ),
        migrations.AddField(
            model_name='feedbackpage',
            name='form_title',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='feedbackpage',
            name='from_address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='feedbackpage',
            name='subject',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='feedbackpage',
            name='to_address',
            field=models.TextField(blank=True),
        ),
    ]
