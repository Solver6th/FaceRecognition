작업 내용

1. venv 가상환경 만들기 
    $ python -m venv venv
2. Scripts 폴더로 이동 
    $ cd venv $ cd Scripts
3. activate -> (venv) 생성됨 
    $ . activate
4. "cd .." 두번 후 장고 설치 
    $ cd .. 
    $ cd .. 
    $ pip install django ->   장고패키지 설치 
    <<중요 pip이란 Python 패키지 관리자 중 하나로 지정한 패키지를  다은로드하고 설치해줌(이때 추가로 필요한 다른패키지도 자동으로 같이 설치해줌)>>
5. 장고 프로젝트 만들기 (주의 처음 실행시) 
    $ django-admin startproject mysite
6. mysite로 이동 후 runserver 
    $ cd mysite 
    $ python manage.py runserver
7. 데이터베이스 생성 
    $ python manage.py migrate


설문조사 앱 만들기(https://docs.djangoproject.com/ko/4.1/intro/tutorial01/)

1. 첫번 째 뷰 작성하기 (pools/urls.py 와 mysite/urls.py에 코드 입력 주의)   
    polls/urls.py & mysite/urls.py -> 어디에 위치한 urls인지 혼동하지 말기
2. 데이터 베이스 설치 
    $ python manage.py migrate
3. 모델 만들기 
    polls/models.py 수정
4. 모델 활성화 
    mysite/settings.py 파일을 편집하여 INSTALLED_APPS 설정에 추가
5. API 가지고 놀기 
    polls/models.py 파일의 Question 모델을 수정하여, str() 메소드를 Question과 Choice에 추가 polls/models.py에 커스텀 메소드 또한 추가
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
    polls/templates/polls/detail.html에 HTML 요소를 포함 
    polls/urls.py에 vote() 함수 추가 
    polls/templates/polls/results.html 생성
18. 제너릭 뷰 사용하기 
    polls/urls.py 변경 
    polls/views.py 수정
19. 배경 이미지 추가 
    이미지 추가하는 방법 -> static\polls 폴더에 image 폴더를 추가 후 images/background.png 파일을 저장 
    polls/static/polls/style.css 생성 및 작성


얼굴 인식 앱 만들기(https://learn.microsoft.com/ko-kr/training/modules/analyze-images-computer-vision/3-analyze-images) 

1. 아주르 홈페이지 가서 리소스 만들기 (스카이프 채팅창에 있는 사진 참고) 
    리소스 만들기에서 Cognitive Services 리소스 생성( https://portal.azure.com)
2. 리소스 그룹에서 키 및 엔드포인트 확인 및 저장하기 
3. Cloud Shell 실행
     <<중요 Cloud Shell에서 셸 형식을 PowerShell로 바꾼다>>
      아주르에서 파워쉘연 후 https://learn.microsoft.com/ko-kr/training/modules/analyze-images-computer-vision/2-image-analysis-azure 들어가기 
4. 샘플 애플리케이션을 다운로드 
    $ git clone https://github.com/MicrosoftLearning/AI-900-AIFundamentals ai-900 입력 
5. 키 및 엔드포인트 변경 
    $code . 입력 
    analyze.image.ps1 들어가서 자신의 키포인트 및 엔드포인트 변경 
6. 이미지 분석 
    $cd ai-900 ./analyze-image.ps1 store-camera-1.jpg 입력

Python 용 Azure Cognitive service 모듈 (https://learn.microsoft.com/ko-kr/python/api/overview/azure/cognitive-services?view=azure-python)
-Face API(비전모듈)
1. venv가 있는지 확인
    결과창에 venv 폴더가있는지 확인하기
    $ls -a
2. (venv가있을경우) 가상환경으로 들어가기
    $cd venv
    $cd Scripts
    $. activate
3. Face python 패키지 설치
    $cd ..
    $cd ..
    $pip install cognitive-face
4. Azure 계정에 Cognitive Services 기여자 역할이 할당되어있지 않을 경우 할당하기
5. 얼굴식별 클라이언트 라이브러리 설치
    $pip install --upgrade azure-cognitiveservices-vision-face
6. 새 Python 애플리케이션 만들기
    faceapi 폴더 생성후 안에 quickstart-file.py 생성 gn 코드 붙여넣기

[Python] 파이썬 OpenCV를 이용한 얼굴 인식(https://deep-eye.tistory.com/m/18)
1. 가상환경 들어가기
2. OpenCV 폴더 생성
    $pip install opencv-python
    main.py 생성
3. Haar Cascade 분류기 불러오기
    haarcascade_frontalface_alt.xml 다운로드 및 OpenCV 폴더로 이동
4. 사진 불러오기
    사진 파일과 사진 출력만 main.py에 코딩
5. 얼굴 탐지 알고리즘 적용
    오타 주의
6. 최종 응용 코딩
    imgDetector(cam,cascade)이 아닌 imgDetector(img, cascade)로 작성
7. 실행
    $python main.py


Facerecognition 

1. 가상환경들어가기
2. models.py 안에 코드추가
3. mysite안에 media\images 폴더 생성
4. mysite\mysite\setting.py 안에 MEDIA_URL,MEDIA_ROOT 생성
5. mysite\facerecognition\admin.py 안에 Face model 추가
6. 가상환경안에서 mysite 안에서 다음 커맨드 실행
    $python manage.py makemigrations
7. 6번이후 다음 커맨드실행
    $python manage.py migrate
8. mysite\facerecognition\forms.py 생성후 FaceForm 클래스 추가
9. mysite\facerecognition\templates\facerecognition\face_image.html 생성
10. mysite\facerecognition\views.py 안에 FaceImage 클래스 추가
11. mysite\facerecognition\templates\facerecognition\face_image_display.html 생성
12. mysite\facerecognition\views.py 안에 FaceImageDisplay 클래스 추가
13. mysite\facerecognition\views.py 안 arg 앞에 *추가