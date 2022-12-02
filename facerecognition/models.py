from django.db import models
import cv2
from PIL import Image
import numpy as np
from io import BytesIO
from django.core.files import File

def make_image(image_input, cascade):
    """Makes thumbnails of given size from given image"""
    image = Image.open(image_input)

    image = np.array(image)
    #영상 압축
    image = cv2.resize(image, dsize=None, fx=1.0, fy=1.0)
    #그레이 스케일 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #cascaed 얼굴 탐지 알고리즘
    results = cascade.detectMultiScale(gray,               #입력 이미지
                                        scaleFactor = 1.5, #이미지 피라미드 스케일 factor
                                        minNeighbors = 5, #인접 객체 최소 거리 픽셀
                                        minSize = (20,20)   #탐지 객첵 최소 크기
                                        ) 

    #결과값 = 탐지된 객체의 경계상자 list
    for box in results:
        #좌표 추출
        x, y, w, h =  box
        #경계 상자 그리기
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 255), thickness=2)

    image = Image.fromarray(image)
    image = image.convert("RGB")
    image_io = BytesIO()
    image.save(image_io, "JPEG", quality=85)
    img = File(image_io, name = image_input.name)
    return img

class Face(models.Model):
    #이미지 이름
    name = models.CharField(max_length=50)
    #media 폴더 안에 images 폴더 생성
    image = models.ImageField(upload_to = "images/")

    def save(self, *args, **kwargs):
      
        #가중치 파일 경로
        cascade_filename = 'haarcascade_frontalface_alt.xml'
        #모델 불러오기
        cascade = cv2.CascadeClassifier(cascade_filename)

        self.image = make_image(self.image, cascade)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name