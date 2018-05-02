# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-04-26 11:09
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0050_auto_20180426_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('rich_text', wagtail.wagtailcore.blocks.RichTextBlock()), ('heading', wagtail.wagtailcore.blocks.RichTextBlock()), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), ('column_left', wagtail.wagtailcore.blocks.RichTextBlock()), ('column_right', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()))),
        ),
    ]
