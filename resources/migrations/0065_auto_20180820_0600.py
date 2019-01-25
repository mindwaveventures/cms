# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-08-20 06:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0007_merge'),
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('resources', '0064_auto_20180611_0712'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='bottom_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page'),
        ),
        migrations.AddField(
            model_name='home',
            name='bottom_link_text',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='\n        Link Text of PDF block\n    '),
        ),
        migrations.AddField(
            model_name='home',
            name='pdf_body',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='\n        Body of PDF block\n    '),
        ),
        migrations.AddField(
            model_name='home',
            name='pdf_file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
        migrations.AddField(
            model_name='home',
            name='pdf_heading',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, help_text='\n        Heading of PDF block\n    '),
        ),
    ]
