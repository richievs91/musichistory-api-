from django.db import models
from django.contrib.auth.models import User


class Artist(models.Model):
    artist_name = models.CharField(max_length=55)
    year_established = models.CharField(max_length=55)

    def __str__(self):
        return '{} {}'.format(self.artist_name, self.year_established) 

class Genre(models.Model):
    genre_type = models.CharField(max_length=55)

    def __str__(self):
        return '{}'.format(self.genre_type)

class Album(models.Model):
    album_title = models.CharField(max_length=55)
    release_date = models.CharField(max_length=55)
    album_length = models.CharField(max_length=55)
    label = models.CharField(max_length=55)
    artist_id = models.ForeignKey(Artist, blank=True, default='')
    genre_id = models.ForeignKey(Genre, blank=True, default='')

    def __str__(self):
        return '{} {} {} {}'.format(self.album_title, self.release_date, self.album_length, self.label)

class Song(models.Model):
    song_title = models.CharField(max_length=55)
    song_length = models.CharField(max_length=55)
    release_date = models.CharField(max_length=55)
    genre_id = models.ForeignKey(Genre, blank=True, default='')
    artist_id = models.ForeignKey(Artist, blank=True, default='')
    album_id = models.ForeignKey(Album, blank=True, default='')

    def __str__(self):
        return '{} {} {}'.format(self.song_title, self.song_length, self.release_date)