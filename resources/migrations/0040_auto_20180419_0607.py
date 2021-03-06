# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-04-19 06:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
        ('wagtailimages', '0019_delete_filter'),
        ('resources', '0039_auto_20180419_0453'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeFooterLinks',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('footer_link', models.URLField(blank=True)),
                ('footer_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='footer_links', to='resources.Main')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HomeSiteMap',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('link_text', models.TextField(blank=True)),
                ('link_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='site_map', to='resources.Main')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='homefooterlinksone',
            name='link_page',
        ),
        migrations.RemoveField(
            model_name='homefooterlinksone',
            name='page',
        ),
        migrations.RemoveField(
            model_name='homefooterlinkstwo',
            name='footer_image',
        ),
        migrations.RemoveField(
            model_name='homefooterlinkstwo',
            name='page',
        ),
        migrations.DeleteModel(
            name='HomeFooterLinksOne',
        ),
        migrations.DeleteModel(
            name='HomeFooterLinksTwo',
        ),
    ]
