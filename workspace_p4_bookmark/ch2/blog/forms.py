from django import forms	# 폼을 클래스로 표현할 수 있도록 하는 기능. django.forms 모듈에서 제공

class PostSearchForm(forms.Form):	# 그 모듈의 Form클래스를 상속받아 클래스를 정의
	search_word=forms.CharField(label='Search Word')	# CharField는 텍스트입력 위젯으로 표현됨. label인자인 Search Word는 폼 앞에 출력되는 레이블이 됨.
													# 변수 search_word는 필드에 대한 id로 각 필드를 구분하는 데 사용 됨