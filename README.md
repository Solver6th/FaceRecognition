작업 내용
1. venv 가상환경 만들기
    $ python -m venv venv
2. Scripts 폴더로 이동
    $ cd venv 
    $ cd Scripts
3. activate -> (venv) 생성됨
    $ . activate
4. "cd .." 두번 후 장고 설치
    $ cd ..
    $ cd ..
    $ pip install django
5. 장고 프로젝트 만들기 (주의 처음 실행시)
    $ django-admin startproject mysite
6.  mysite로 이동 후 runserver
    $ cd mysite
    $ python manage.py runserver
7. 데이터베이스 생성
    $ python manage.py migrate
    
설문조사 앱 만들기(https://docs.djangoproject.com/ko/4.1/intro/tutorial01/)
1. 첫번 째 뷰 작성하기
    pools/urls.py 와 mysite/urls.py에 코드 입력
    주의) polls/urls.py & mysite/urls.py -> 어디에 위치한 urls인지 혼동하지 말기
2. 데이터 베이스 설치
    $ python manage.py migrate
3. 모델 만들기
    polls/models.py 수정
4. 모델 활성화
    mysite/settings.py 파일을 편집하여 INSTALLED_APPS 설정에 추가
5. API 가지고 놀기
    polls/models.py 파일의 Question 모델을 수정하여, __str__() 메소드를 Question과 Choice에 추가
    polls/models.py에 커스텀 메소드 또한 추가
6. 관리자 생성
    $ python manage.py createsuperuser
    Username: admin
    Email address: admin@example.com
    Password: **********
    Password (again): *********
7. 개발 서버 시작
    $ python manage.py runserver
    http://127.0.0.1:8000/admin/
8. 관리 사이트에서 poll app 을 변경가능하도록 만들기
    polls/admin.py 파일을 열어 편집
9. 뷰 추가하기
    polls/views.py 에 뷰를 추가
    path() 호출을 추가하여 새로운 뷰를 polls.urls 모듈로 연결
10. 뷰가 실제로 뭔가를 하도록 만들기
    polls/views.py 수정 (띄어쓰기 신경쓰기 -> view.py에서 띄어쓰기 문제로 오류 발생)
    polls/templates/polls/index.html에 코드 입력
    polls/views.py에 index 뷰를 업데이트
11. 지름길: render()
    index() 뷰를 단축 기능으로 작성
12. 404 에러 일으키기
    polls/views.py에 새로운 내용이 추가(뷰는 요청된 질문의 ID 가 없을 경우 Http404 예외를 발생)
    polls/templates/polls/detail.html 작성
13. 지름길: get_object_or_404()
    polls/views.py에 detail() 뷰를 단축 기능으로 작성
14. 템플릿 시스템 사용하기
    polls/views.py에 detail()에 추가 작성
15. 템플릿에서 하드코딩된 URL 제거하기
    polls/templates/polls/index.html에 코드 수정
16. URL의 이름공간 정하기
    polls/urls.py 파일에 app_name을 추가
    polls/templates/polls/index.html에 코드 변경
17. 간단한 폼 쓰기
    polls/templates/polls/detail.html에 HTML <form> 요소를 포함
    polls/urls.py에 vote() 함수 추가
    polls/templates/polls/results.html 생성
18. 제너릭 뷰 사용하기
    polls/urls.py 변경
    polls/views.py 수정
19. 배경 이미지 추가
    이미지 추가하는 방법 -> static\polls 폴더에 image 폴더를 추가 후 images/background.png 파일을 저장
    polls/static/polls/style.css 생성 및 작성


얼굴 인식 앱 만들기