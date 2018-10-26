"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path,include

from mysite.views import HomeView	# 인덱스를 위해
from django.conf.urls.static import static
from django.conf import settings

#from bookmark.views import BookmarkLV, BookmarkDV

urlpatterns = [
	path('', HomeView.as_view(),name='home'),
    path('admin/', admin.site.urls),
    re_path(r'^bookmark/',include('bookmark.urls'),name='bookmark'),
    re_path(r'^blog/',include('blog.urls'),name='blog'),
    #re_path(r'^bookmark/$',BookmarkLV.as_view(),name='index'),
    #re_path(r'^bookmark/(?P<pk>\d+)/$',BookmarkDV.as_view(),name='detail'),
    re_path(r'^photo/', include('photo.urls', namespace='photo')),  #이렇게 해도 되나봄

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
