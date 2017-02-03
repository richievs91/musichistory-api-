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
    artist = models.ForeignKey(Artist, blank=True, default='')
    genre = models.ForeignKey(Genre, blank=True, default='')

    def __str__(self):
        return '{} {} {} {}'.format(self.album_title, self.release_date, self.album_length, self.label)

class Song(models.Model):
    song_title = models.CharField(max_length=55)
    song_length = models.CharField(max_length=55)
    release_date = models.CharField(max_length=55)
    genre = models.ForeignKey(Genre, blank=True, default='')
    artist = models.ForeignKey(Artist, blank=True, default='')
    album = models.ForeignKey(Album, blank=True, default='')

    def __str__(self):
        return '{} {} {}'.format(self.song_title, self.song_length, self.release_date)