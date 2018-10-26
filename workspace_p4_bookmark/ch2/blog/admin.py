from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):			# 클래스로 정의
	list_display=('title','modify_date')		# Post 객체의 title과 modify_date를 출력
	list_filter=('modify_date',)				# modify_date 컬럼을 사용하는 필터 사이드바를 출력
	search_fields=('title','content')			# 검색 박스를 표시, title과 content 컬럼에서 검색
	prepopulated_fields={'slug':('title',)}		# title필드로 slug필드를 미리 채움

admin.site.register(Post,PostAdmin)