# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-09-18 09:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import resources.models.home
import uuid

class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('resources', '0024_auto_20170912_1224'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainLocationImages',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('first_letters_of_zip', resources.models.home.TwoCharsZipcodeField(blank=True, help_text='\n            The first letter or letters of the postcode\n            you would like to match with, e.g. TW or E\n        ', max_length=255)),
                ('location_image', models.ForeignKey(blank=True, help_text='\n            Max file size: 10MB. Choose from: GIF, JPEG, PNG\n            (but pick PNG if you have the choice)\n        ', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='resourcepage',
            name='video_url',
        ),
        migrations.AddField(
            model_name='home',
            name='mobile_title',
            field=models.TextField(blank=True, help_text='Title to show on mobile'),
        ),
        migrations.AlterField(
            model_name='home',
            name='header',
            field=models.TextField(blank=True, help_text='Hero title'),
        ),
        migrations.AlterField(
            model_name='main',
            name='header',
            field=models.TextField(blank=True, help_text='Hero title'),
        ),
        migrations.AddField(
            model_name='mainlocationimages',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_images', to='resources.Main'),
        ),
    ]
