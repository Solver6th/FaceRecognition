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