from django.urls import path, re_path
from photo.views import *

app_name='photo' 	# reverse를 위해 반드시 필요

urlpatterns= [
	re_path(r'^$',AlbumLV.as_view(), name='index'),

	re_path(r'^album/$', AlbumLV.as_view(), name='album_list'),

	re_path(r'^album/(?P<pk>\d+)/$', AlbumDV.as_view(), name='album_detail'),

	re_path(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail'),


]