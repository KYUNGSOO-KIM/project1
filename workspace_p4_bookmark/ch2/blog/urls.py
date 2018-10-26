from django.urls import path, re_path
from blog.views import *		# 뷰 모듈의 클래스가 많을 때


app_name='blog' 	# reverse를 위해 반드시 필요

urlpatterns= [

	re_path(r'^$',PostLV.as_view(),name='index'),	# /blog/로 요청이 오면 뷰의 PostLV로 가라. URL패턴의 이름은 blog:index임

	re_path(r'^post/$',PostLV.as_view(),name='post_list'),	# /blog/ 와 /blog/post/ 2가지 요청 모두 처리. 요청이 오면 뷰의 PostLV로 가라. URL패턴의 이름은 blog:post_list

	re_path(r'^post/(?P<slug>[-\w]+)/$',PostDV.as_view(),name='post_detail'), # /blog/post/영단어/ 요청이 오면, 뷰 클래스 PostDV로 지정. URL패턴의 이름은 blog:post_detail

	re_path(r'^archive/$',PostAV.as_view(),name='post_archive'), # /blog/archive 요청이 오면, 뷰 클래스 PostAV로 지정. URL패턴의 이름은 blog:post_archive

	re_path(r'^(?P<year>\d{4})/$',PostYAV.as_view(),name='post_year_archive'), # /blog/4자리 숫자 요청이 오면, 뷰 클래스 PostYAV로 지정. URL패턴의 이름은 blog:post_year_arc

	re_path(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',PostMAV.as_view(),name='post_month_archive'), # /blog/4숫자/3소문자/ 요청시 PostMAV 뷰로.

	re_path(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$',PostDAV.as_view(),name='post_day_archive'), # /blog/4숫자/3소문자/1-2숫자 시 PostDAV뷰로

	re_path(r'^today/$',PostTAV.as_view(),name='post_today_archive'), # /blog/today 요청 시 PostTAV로. url 패턴은 blog:post_today_archive

	re_path(r'^tag/$',TagTV.as_view(),name='tag_cloud'),	# /blog/tag 시 처리할 뷰 클래스를 TagTV로 지정. TagTV클래스형 뷰는 태그 클라우드를 보여주기 위한 뷰
															# 템플릿 처리만 하면 되므로 TemplateView를 상속받아 정의할 것임 . url패턴은 blog:tag_cloud

	re_path(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(),name='tagged_object_list'), #/blog/post/tagname 요청시 PostTOL 클래스 뷰로 지정. 태그 단어를 인자로 받아서
															# 해당 태그가 달린 포스트들의 리스트를 보여줌. tagging앱에서 정의하고 있는 TaggedObjectList(ListView)클래스를 
															# 상속받아 정의할 예정. 
    re_path(r'^search/$', SearchFormView.as_view(), name='search'), # /search/ 요청 시 뷰 클래스를 SearchFormView로 지정. URL 패턴은 blog:search임. 
    														# SearchFormView 클래스형 뷰는 폼을 보여주고 폼에 들어 있는 데이터를 처리하기 위한 뷰이므로 FormView를상속받아 정의



]