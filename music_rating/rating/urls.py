from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
  #path('users/', UserList.as_view(), name=UserList.name),
  #path('user/<int:pk>', UserDetail.as_view(), name=UserDetail.name),
  path('', ApiRoot.as_view(), name=ApiRoot.name),
  path('artists/', ArtistList.as_view(), name=ArtistList.name),
  path('artist/<int:pk>', ArtistDetail.as_view(), name=ArtistDetail.name),
  path('albums', AlbumList.as_view(), name=AlbumList.name),
  path('album/<int:pk>', AlbumDetail.as_view(), name=AlbumDetail.name),
  path('songs', SongList.as_view(), name=SongList.name),
  path('song/<int:pk>', SongDetail.as_view(), name=SongDetail.name),
  path('profiles', ProfileList.as_view(), name=ProfileList.name),
  path('profile/<int:pk>', ProfileDetail.as_view(), name=ProfileDetail.name),
  path('ratings/', RatingList.as_view(), name=RatingList.name),
  path('rating/<int:pk>', RatingDetail.as_view(), name=RatingDetail.name),
  path('music_rating-token-auth', obtain_auth_token),
  path('music_rating/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('music_rating/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]