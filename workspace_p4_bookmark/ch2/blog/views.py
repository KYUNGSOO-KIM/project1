from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post

from tagging.models import Tag, TaggedItem		# tagging 패키지에서 정의한 2개의 모델 클래스를 임포트 (패키지에서 2개의 클래스(model)를 임포트)
from tagging.views import TaggedObjectList		# tagging 패키지에서 정의한 뷰 클래스를 임포트 (패키지에서 1개의 클래스(view)를 임포트)


from django.views.generic.edit import FormView # FormView 클래스형 제네릭 뷰를 임포트	
from blog.forms import PostSearchForm # 검색 폼으로 사용할 PostSearchForm 폼 클래스를 임포트. forms.py 에서 이미 정의함
from django.db.models import Q # 검색 기능에 필요한 Q클래스
# from django.shortcuts import render 위에 있음 단축함수

class TagTV(TemplateView):		# TemplateView 제네릭 뷰를 상속받아 PostTV클래스형 뷰를 정의 함 TemplateView 제네릭 뷰는 테이블 처리 없이 단순히 템플릿 렌더링 처리만 하는 뷰임
	template_name='tagging/tagging_cloud.html'	#템플릿 파일을 지정함. 이 템플릿 파일에서 태그 클라우드를 보여주는 기능을 처리함.


class PostLV(ListView):			# ListView를 상속
	model=Post  						#PostLV의 대상 테이블은 Post 테이블
	template_name='blog/post_all.html'	# 템플릿 파일 지정. 디폴트는 blog/post_list.html
	context_object_name='posts'			# 템플릿 파일로 넘겨주는 객체리스트에 대한 컨텍스트변수명을 posts로 지정 디폴트 object_list
	paginate_by=2						# 한 페이지에 보여주는 객체 리스트의 숫자 2, 페이징 기능 활성화로 페이지 이동 버튼 생성

class PostTOL(TaggedObjectList):	# TaggedObjectList 클래스형 뷰를 상속받아 PostTOL 클래스형 뷰를 정의. TaggedObjectList클래스는 ListView를 상속받는 뷰임.
	model=Post                      # TaggedObjectList 뷰는 tagging 패키지의 views.py파일에 정의 되어 있는데, 그 기능은 모델과 태그가 주어지면 그 태그가 달려있는 모델의 
	template_name='tagging/tagging_post_list.html'	# 객체 리스트를 보여줌. 대상 테이블은 Post, 템플릿 파일을 지정.


class PostDV(DetailView):   # Detail 제네릭 뷰를 상속받아 클래스형 뷰를 정의. 특정 객체의 상세 정보 출력. slug속성을 사용
	model=Post  				# 대상 테이블은 Post

class PostAV(ArchiveIndexView): 	# 제네릭 뷰 상속하여 클래스뷰 정의. 테이블로부터 객체 리스트를 가져와 날짜 필드 기준으로 최신 객체 출력 
	model=Post 					# 대상 테이블은 Post
	date_field='modify_date'    # 기준 날짜는 변경 날짜로 정의. 최신 객체 먼저 출력 하도록

class PostYAV(YearArchiveView):  #제네릭 뷰 상속,클래스뷰정의. 테이블에서 연도를 기준으로 객체 리스트를 가져와 월을 리스트로 출력
	model=Post  				# 대상 테이블은 Post
	date_field='modify_date'    # 기준 날짜는 변경 날짜로 정의. 변경날짜 YYYY기준으로 변경 월을 출력
	make_object_list=True       #  해당 연도의 해당 객체 리스트를 만들어서 템플릿에 넘겨 줌. 템플릿파일에서 object_list 컨텍스트변수 사용 가능

class PostMAV(MonthArchiveView):  #연월 기준으로 객체 리스트를 가져와, 출력. 
	model=Post    				# 대상 테이블은 Post
	date_field='modify_date'   # 기준 날짜로 컬럼 사용. 연월 기준으로 리스트 출력 

class PostDAV(DayArchiveView): # 연월 일 기준
	model=Post
	date_field='modify_date'

class PostTAV(TodayArchiveView):   # 오늘 날짜 기준
	model=Post
	date_field='modify_date'

class SearchFormView(FormView): # FormView 제네릭 뷰를 상속받아 SearchFormView 클래스형 뷰를 정의. FormView 제네릭 뷰는 GET요청인 경우 폼을 화면에 보여주고 사용자의 입력을
								# 기다림. 사용자가 폼에 데이터 입력 후 제출하면 이는 POST요청으로 접수되어, FormView 클래스는 데이터에 대한 유효성 검사를 함. 
								# 데이터가 유효하면 form_valid()함수를 실행 한 후에 적절한 URL로 리다이렉트시키는 기능을 함
	form_class=PostSearchForm	# 폼으로 사용될 클래스를 PostSearchForm으로 지정
	template_name='blog/post_search.html'	# 템플릿 파일 지정

	def form_valid(self,form):	# POST요청으로 들어온 데이터에 대한 유효성 검사. 에러 없으면 form_valid()메소드를 실행함
		schWord='%s' % self.request.POST['search_word'] # POST요청의 search_word 파라미터 값을 추출해, schWord변수에 지정함. search_word 파라미터는 PostSearchForm클래스에서 정의한 필드 id
		post_list=Post.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()
	    # Q객체는 filter()메소드의 매칭 조건을 다양하게 줄 수 있도록 함. 3개의 조건을 OR로 연결. icontains는 대소문자 구분 안하도록
	    # distinct()메소드는 중복된 객체는 제외. 즉 Post테이블의 모든 레코드에 대해 title, description, content컬럼에 schWord가 포함된 레코드를 대소문자 구분없이 검색하여
	    # 서로 다른 레코드들만 리스트로 만들어서 post_list변수에 지정	

		context={} #템플릿에 넘겨줄 컨텍스트 변수를 사전 형식으로 정의
		context['form']=form # form 객체, 즉 PostSearchForm 객체를 컨텍스트 변수 form에 지정
		context['search_term']=schWord # 검색용 단어 schWord를 컨텍스트 변수 search_term에 지정함
		context['object_list']=post_list # 검색 결과 리스트인 post_list를 컨텍스트 변수 object_list에 지정
		return render(self.request, self.template_name, context) 	# No redirection
		#단축함수 render()는 템플릿 파일과 컨텍스트 변수를 처리해, 최종적으로 HttpResponse객체를 반환. form_valid()함수는 보통 리다이렉트 처리를 위해 HttpResponseRedirect
		#객체를 반환하는데, 이 render()함수에 의해 리다이렉트 처리가 되지 않음.

