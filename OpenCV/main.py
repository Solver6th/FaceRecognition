import cv2

#가중치 파일 경로
cascade_filename = 'haarcascade_frontalface_alt.xml'
#모델 불러오기
cascade = cv2.CascadeClassifier(cascade_filename)

#사진 파일
img = cv2.imread('sample.jpg')
#사진 출력
def imgDetector(img,cascade):
    img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cascaed 얼굴 탐지 알고리즘
#(입력 이미지, 이미지 피라미드 스케일 factor, 인접 객체 최소 거리 픽셀, 탐지 객첵 최소 크기)
results = cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5, minSize(20,20)) 

#결과값 = 탐지된 객체의 경계상자 list
for box in results:
    #좌표 추출
    x, y, w, h =  box
    #경계 상자 그리기
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), thinckness=2)

