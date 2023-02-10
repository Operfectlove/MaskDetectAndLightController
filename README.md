# MaskDetectAndLightController

we used "WEMOS D1 mini ESP8266 board"

# 제작자 김지원, 김성윤

#사용법

1. 아두이노ide에 "WEMOS D1 mini ESP8266 board" 설정을 추가하고 .ino파일을 열어 와이파이를 설정한 후 업로드 한다.
2. 메인기기에 파이썬과 opencv, HaarCascades분류기를 다운로드하여 경로를 설정한다.
3. 파이썬 코드를 열고 esp모듈의 내부ip주소를 입력하여 수정한다.
4. esp와 메인기기 모두 같은 네트워크에 연결되어 있다면 동작을 한다.
5. 메인기기의 카메라에서 마스크가 쓰여있지 않음이 인식되면 http request를 esp모듈로 보내게 되고, esp가 request를 수신하면 조명이 꺼진 후 깜빡이게 된다.
