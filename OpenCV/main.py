import cv2

#가중치 파일 경로
cascade_filename = 'haarcascade_frontalface_alt.xml'
#모델 불러오기
cascade = cv2.CascadeClassifier(cascade_filename)