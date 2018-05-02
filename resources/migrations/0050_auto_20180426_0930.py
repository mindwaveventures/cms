# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-04-26 09:30
from __future__ import unicode_literals

from django.db import migrations
from wagtail.wagtailcore.rich_text import RichText
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks

class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0049_results_cover_image'),
    ]
def convert_to_streamfield(apps, schema_editor):
   ResourcePage = apps.get_model("resources", "ResourcePage")
   for page in ResourcePage.objects.all():
       if page.body.raw_text and not page.body:
           page.body = [('rich_text', RichText(page.body.raw_text))]
           page.save()


def convert_to_richtext(apps, schema_editor):
   ResourcePage = apps.get_model("resources", "ResourcePage")
   for page in ResourcePage.objects.all():
       if page.body.raw_text is None:
           raw_text = ''.join([
               child.value.source for child in page.body
               if child.block_type == 'rich_text'
           ])
           page.body = raw_text
           page.save()

class Migration(migrations.Migration):

    dependencies = [
       ('resources', '0049_results_cover_image'),
    ]
    
    operations = [
        migrations.AlterField(
            model_name='resourcepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('rich_text', wagtail.wagtailcore.blocks.RichTextBlock()), ('heading', wagtail.wagtailcore.blocks.RichTextBlock()), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(template='static/display.html')), ('column_left', wagtail.wagtailcore.blocks.RichTextBlock(template='static/display.html')), ('column_right', wagtail.wagtailcore.blocks.RichTextBlock(template='static/display.html')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()))),
        ),
        migrations.RunPython(
            convert_to_streamfield,
            convert_to_richtext,
        ),
    ]
