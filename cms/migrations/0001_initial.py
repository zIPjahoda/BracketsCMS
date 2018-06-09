# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 13:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('content', models.TextField()),
                ('publish_date', models.DateTimeField()),
                ('keywords', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=500)),
                ('thumbnail_path', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('keywords', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=500)),
                ('thumbnail_path', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=500)),
                ('icon_path', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('keywords', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=500)),
                ('publish_date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Category'),
        ),
    ]