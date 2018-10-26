from django.urls import path, re_path
from bookmark.views import BookmarkLV, BookmarkDV

app_name='bookmark'

urlpatterns = [
    re_path(r'^$',BookmarkLV.as_view(),name='index'),
    re_path(r'^(?P<pk>\d+)/$',BookmarkDV.as_view(),name='detail'),
]
