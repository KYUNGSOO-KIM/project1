from django.views.generic.base import TemplateView

class HomeView(TemplateView):	#TemplateView 제네릭 뷰를 상속. 필수로 template_name 클래스 변수를 오버라이딩 지정 해주어야 함
	template_name='home.html'	#mysite프로젝트의 첫 화면을 위해 home.html을 지정. 템플리 파일 디렉터리는 TEMPLATES_DIRS에 지정