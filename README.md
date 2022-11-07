작업 내용
1. venv 가상환경 만들기
    $ python -m venv venv
2. Scripts 폴더로 이동
    $ cd venv 
    $ cd Scripts
3. activate -> (venv) 생성됨
    $ . activate
4. "cd .." 두번 후 장고 설치
    $ pip install django
5. 장고 프로젝트 만들기 (주의 처음 실행시)
    $ django-admin startproject mysite
6.  mysite로 이동 후 runserver
    $ cd mysite
    $ python manage.py runserver
7. 데이터베이스 생성
    $ python manage.py migrate
    
설문조사 앱 만들기(https://docs.djangoproject.com/ko/4.1/intro/tutorial01/)
1. pools/urls.py & mysite/urls.py
    어디에 위치한 urls인지 혼동하지 말기
2. 띄어쓰기 신경쓰기
    view.py에서 띄어쓰기 문제로 오류 발생
3. 이미지 추가하는 방법
    static\polls 폴더에 image 폴더를 추가 후 png 파일을 저장

얼굴 인식 앱 만들기