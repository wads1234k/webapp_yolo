# YOLOv5 Object Detection using Webcam and YouTube Video

이 프로젝트는 chatGPT를 이용하여 **YOLOv5** 모델을 사용하여 웹캠과 YouTube 비디오에서 실시간 객체 인식을 수행하는 파이썬 스크립트입니다. 두 개의 주요 스크립트가 포함되어 있으며, 각각은 다른 데이터 소스를 처리합니다. 

## 파일 목록

- `video_yolo.py`: YouTube 비디오 URL에서 객체 인식을 수행하는 스크립트
- `webcam_yolo_gui.py`: 웹캠에서 실시간 객체 인식을 수행하는 스크립트
- `index.html`: `webcam_yolo_gui.py`를 웹에서 실행하도록 수정한 파일일

## 요구 사항

- Python 3.x
- PyTorch
- OpenCV
- YOLOv5 모델
- yt-dlp (YouTube 비디오 스트리밍을 위한 라이브러리)

## 사용 방법
### 1. `video_yolo.py`: YouTube 비디오에서 객체 인식

1. **YouTube URL**을 지정합니다.
2. **YOLOv5 모델**을 사용하여 해당 비디오에서 객체를 실시간으로 인식합니다.
3. **인식된 객체**는 화면에 표시됩니다.


### 2. `webcam_yolo_gui.py`: 웹캠에서 실시간 객체 인식

1. **웹캠을 연결**하고 스크립트를 실행합니다.
2. 웹캠 화면이 캡처되어 실시간으로 객체 인식이 이루어집니다.
3. **YOLOv5 모델**을 사용하여 웹캠에서 캡처한 비디오 스트림을 처리하고, 인식된 객체를 화면에 표시합니다.


