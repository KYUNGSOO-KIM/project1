from django.db import models
from django.urls import reverse
from tagging.fields import TagField	# 자체 필드인 TagField를 정의하고 있음

class Post(models.Model):
	title=models.CharField('TITLE',max_length=50)  		# CharField는 한 줄로 입력을 의미, TITLE은 컬럼에 대한 레이블(폼 화면에 나타나는 문구, Admin사이트에서 확인)
	slug=models.SlugField('SLUG',unique=True, allow_unicode=True, help_text='one word for title alias')
	# slug는 제목의 별칭. slugfield에 unique 옵션을 추가해, 특정 포스트 검색 시 기본 키 대신에 사용, allow_unicode는 한글 처리, help_text는 해당 컬럼을 설명으로 폼 화면에 나타남(admin)
	description=models.CharField('DESCRIPTION',max_length=100, blank=True, help_text='simple description text') # blank는 빈칸 가능
	content=models.TextField('CONTENT') # TextField는 여러 줄 입력 가능
	create_date=models.DateTimeField('Create Date',auto_now_add=True) # 객체가 생성 될 때의 시각
	modify_date=models.DateTimeField('Modify Date',auto_now=True) # 객체가 변경 될 때의 시각
	tag=TagField() # tag컬럼을 TagField로 정의 함. CharField 필드를 상속받아서 디폴트로 max_length=255, Blank=True로 정의하고 있어 tag컬럼은 내용 안채워도 됨

	class Meta:		# 필드 속성 외에 필요한 파라미터는 Meta 내부 클래스로 정의함
		verbose_name='post'			#테이블의 단수 별칭을 post
		verbose_name_plural='posts'	#테이블의 복수 별칭을 posts
		db_table='my_post'			#기존 blog_post을 테이블 이름으로 db에 저장 하지만 my_post로 저장
		ordering=('-modify_date',)	#modify_date컬럼 기준으로 내림차순 정렬

	def __str__(self):
		return self.title

	def get_absolute_url(self):		# 이 메소드가 정의된 객체를 지칭하는 URL을 반환 (템플릿에서 써먹음)
		return reverse('blog:post_detail', args=(self.slug,))	# reverse를 호출

	def get_previous_post(self):	# modify_date 컬럼 기준으로 이전 포스트를 반환 (템플릿에서 써먹음)
		return self.get_previous_by_modify_date() # 장고의 내장 함수 get_previous_by_modify_date

	def get_next_post(self):		# modify_date 컬럼 기준으로 다음 포스트를 반환 (템플릿에서 써먹음)
		return self.get_next_by_modify_date()	# 장고의 내장 함수 get_next_by_modify_date