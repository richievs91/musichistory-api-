# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=55)),
                ('release_date', models.CharField(max_length=55)),
                ('album_length', models.CharField(max_length=55)),
                ('label', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=55)),
                ('year_established', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_type', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=55)),
                ('song_length', models.CharField(max_length=55)),
                ('release_date', models.CharField(max_length=55)),
                ('album_id', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='music_api.Album')),
                ('artist_id', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='music_api.Artist')),
                ('genre_id', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='music_api.Genre')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artist_id',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='music_api.Artist'),
        ),
        migrations.AddField(
            model_name='album',
            name='genre_id',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='music_api.Genre'),
        ),
    ]
