from django.shortcuts import render
from rest_framework import generics, filters, status
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter 
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.authentication import *
from .serializers import *
from .permissions import *
from .models import *


class ArtistList(generics.ListCreateAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    name = 'artist-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsAdminOrReadOnly,)
    pagination_class = LimitOffsetPagination

    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    name = 'artist-detail'
    permission_classes = (IsAdminOrReadOnly,)

class AlbumList(generics.ListCreateAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    name = 'album-list'
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = LimitOffsetPagination

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    name = 'album-detail'
    permission_classes = (IsAdminOrReadOnly,)

class SongList(generics.ListCreateAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    name = 'song-list'
    permission_classes = (IsAdminOrReadOnly,)
    pagination_class = LimitOffsetPagination

    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)

class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    name = 'song-detail'
    permission_classes = (IsAdminOrReadOnly,)

class ProfileList(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    name = 'profile-list'
    permission_classes = (IsAdminOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    name = 'profile-detail'
    permission_classes = (IsUserOrReadOnly,)

class RatingList(generics.ListCreateAPIView):
    serializer_class = RatingSerializer
    queryset = Rate.objects.all()
    name = 'rate-list'
    permission_classes = (IsUserOrReadOnly, permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = LimitOffsetPagination

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingSerializer
    queryset = Rate.objects.all()
    name = 'rate-detail'
    permission_classes = (IsAdminOrReadOnly,)

class ApiRoot(APIView):
    name = 'api-root'
    
    def get(self, request, *args, **kwargs):
        return Response({
            'artists': reverse(ArtistList.name, request=request),
            'albums': reverse(AlbumList.name, request=request),
            'songs': reverse(SongList.name, request=request),
            'profile': reverse(ProfileList.name, request=request),
            'ratings': reverse(RatingList.name, request=request)
        })
