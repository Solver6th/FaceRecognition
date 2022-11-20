import cv2
import timeit

#사진 검출기
def imgDetector(img,cascade):
    #영상 압축
    img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)
    #그레이 스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), thickness=2)
    #사진 출력
    cv2.imshow('facenet', img)
    cv2.waitKey(10000)

#가중치 파일 경로
cascade_filename = 'haarcascade_frontalface_alt.xml'
#모델 불러오기
cascade = cv2.CascadeClassifier(cascade_filename)

#이미지 파일
img = cv2.imread('sample.jpg')

#사진 탐지기
imgDetector(img, cascade)