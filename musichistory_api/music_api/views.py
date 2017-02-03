from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from music_api.serializers import *
from music_api.models import *

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AlbumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Albums to be viewed or edited.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Artists to be viewed or edited.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class SongViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Songs to be viewed or edited.
    """    
    queryset = Song.objects.all()
    serializer_class = SongSerializer 

class GenreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Genres to be viewed or edited.
    """ 
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer