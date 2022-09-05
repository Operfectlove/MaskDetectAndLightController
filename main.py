import numpy as np
import cv2
import requests
from time import sleep
offMask = True
# 찾고자하는 것의 cascade classifier 를 등록
# 경로는 상대경로로 바뀔 수 있음
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
noseCascade = cv2.CascadeClassifier('haarcascade_mcs_nose.xml')

""" 2022.09.03 ~ 2022.09.04 """
""" 
    def = haar를 이용 얼굴과 코을 찾는 함수
    input = 그레이 스케일 이미지
    output = 얼굴과 코에 사각형이 그려진 이미지 프레임
"""


def detect(gray, frame):
    # 등록한 Cascade classifier 를 이용 얼굴을 찾음
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(100, 100),
                                         flags=cv2.CASCADE_SCALE_IMAGE)

    # 얼굴에 사각형을 그리고 코를 찾자
    for (x, y, w, h) in faces:
        # 얼굴: 이미지 프레임에 (x,y)에서 시작, (x+넓이, y+길이)까지의 사각형을 그림(색 255 0 0 , 굵기 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # 이미지를 얼굴 크기 만큼 잘라서 그레이스케일 이미지와 컬러이미지를 만듬
        face_gray = gray[y:y + h, x:x + w]
        face_color = frame[y:y + h, x:x + w]

        # 등록한 Cascade classifier 를 이용 코를 찾음(얼굴 영역에서만)
        nose = noseCascade.detectMultiScale(face_gray, 1.1, 3)

        # 코: 이미지 프레임에 (x,y)에서 시작, (x+넓이, y+길이)까지의 사각형을 그림(색 0 255 0 , 굵기 2)
        for (ex, ey, ew, eh) in nose:
            cv2.rectangle(face_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            dd = requests.get("http://172.20.10.4")
            sleep(1)
            continue

    return frame


# 웹캠에서 이미지 가져오기
video_capture = cv2.VideoCapture(1)

while True:
    # 웹캠 이미지를 프레임으로 자름
    _, frame = video_capture.read()
    # 그리고 이미지를 그레이스케일로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 만들어준 얼굴 코 찾기
    canvas = detect(gray, frame)

    # 찾은 이미지 보여주기
    cv2.imshow("haha", canvas)

    # q를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# 끝
video_capture.release()
cv2.destroyAllWindows()