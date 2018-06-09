# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-09 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='gallery/')),
                ('image_url', models.TextField(blank=True)),
                ('image_name', models.CharField(blank=True, max_length=30)),
                ('description', models.TextField(blank=True, max_length=100)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(blank=True, to='gallery.Category')),
            ],
            options={
                'ordering': ['-post_date'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='locaton',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Location'),
        ),
    ]
