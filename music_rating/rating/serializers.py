from .models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
  
    class Meta:
        model = Artist
        fields = ('url', 'pk', 'name', 'origin', 'genre')

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    artist = serializers.SlugRelatedField(slug_field='name', queryset=Artist.objects.all())
    class Meta:
        model = Album
        fields =('url', 'pk', 'name', 'release_date', 'record_label', 'artist')

class RatingSongSerializer(serializers.HyperlinkedModelSerializer):
    #song = serializers.SlugRelatedField(queryset=Song.objects.all(), slug_field='name')

    class Meta:
        model = Rate
        fields = ('note','comment','profile')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    #ratings = RatingSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user_created = User.objects.create_user(username=validated_data['username'],
                                                email=validated_data['email'],
                                                password=validated_data['password'])
        return Profile.objects.create(user=user_created, **validated_data)
    
    class Meta:
        model = Profile
        fields = ('url', 'pk', 'username', 'email','password')


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    song = serializers.SlugRelatedField(queryset=Song.objects.all(), slug_field='name')
    profile = serializers.SlugRelatedField(queryset=Profile.objects.all(), slug_field='username')

    class Meta:
        model = Rate
        fields = ('url', 'pk', 'song', 'profile', 'note', 'comment')


class SongSerializer(serializers.HyperlinkedModelSerializer):
    album = serializers.SlugRelatedField(slug_field='name', queryset=Album.objects.all())
    ratings = RatingSongSerializer(many=True, read_only=True)
    class Meta:
        model = Song
        fields =('url', 'pk', 'name', 'release_date', 'album', 'ratings')
