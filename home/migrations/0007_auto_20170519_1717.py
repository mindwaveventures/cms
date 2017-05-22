# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-19 17:17
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage_lookingfor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='alphatext',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Explanation of the Alpha section'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Description of page'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='footer',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Footer text'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='lookingfor',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='Information on how to leave suggestions and what the suggestions are for'),
        ),
    ]
