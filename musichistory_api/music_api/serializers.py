from django.contrib.auth.models import User, Group
from rest_framework import serializers
from music_api.models import Album, Artist, Song, Genre 


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name', )


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Album 
        fields = ('album_title', 'release_date', 'album_length', 'label', 'artist_id', 'genre_id', )


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artist
        fields = ('artist_name', 'year_established', )


class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ('song_title', 'song_length', 'release_date', 'genre_id', 'artist_id', 'album_id', )


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre_type', )