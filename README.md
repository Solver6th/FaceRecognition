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
8. 장고 관리자 생성하기
    $ python manage.py createsuperuser
    
설문조사 앱 만들기(https://docs.djangoproject.com/ko/4.1/intro/tutorial01/)
1. pools/urls.py & mysite/urls.py
    어디에 위치한 urls인지 혼동하지 말기
2. 띄어쓰기 신경쓰기
    view.py에서 띄어쓰기 문제로 오류 발생
3. 이미지 추가하는 방법
    static\polls 폴더에 image 폴더를 추가 후 png 파일을 저장

1. 프로젝트 만들기
    $ django-admin startproject mysite
2. 서버가 정상 작동하는지 확인
    $ python manage.py runserver
3. 설문조사 앱 만들기
    $ python manage.py startapp polls (polls 라는 디렉토리가 생성된다.)
4. 데이터베이스 설치
    $ python manage.py migrate
5. 모델 만들기 (설문조사 앱에서 필요한 Question 과 Choice 라는 모델을 만든다.)
    from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

6. 모델 활성화 시키기 (mysite/settings.py 파일에 INSTALLE_APPS 추가)
    INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    ]
6. 장고 관리자 생성 


얼굴 인식 앱 만들기(https://learn.microsoft.com/ko-kr/training/modules/analyze-images-computer-vision/3-analyze-images)
1. Cognitive Services 리소스 만들기( https://portal.azure.com)
    리소스 만들기에서  Cognitive Services 리소스를 만든다.
2. 리소스 그룹에서 키 및 엔드포인트 확인 및 저장하기
3. Cloud Shell 실행
    *중요* Cloud Shell에서 셸 형식을 PowerShell로 바꾼다
4. 샘플 애플리케이션을 다운로드
    $ git clone https://github.com/MicrosoftLearning/AI-900-AIFundamentals ai-900
5. 키 및 엔드포인트 변경
    $code .     을 입력하여 analyze.image.ps1파일에 들어가서 자신의 키 및 엔드포인트 변경
6. 이미지 분석
    $cd ai-900
    ./analyze-image.ps1 store-camera-1.jpg