import cv2
import torch
import yt_dlp as ytdlp

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Define YouTube video URL
youtube_url = 'https://www.youtube.com/watch?v=JfCE2MRFEGA'  # 유튜브 URL을 넣어주세요.

# Set up yt-dlp options to extract the video stream URL
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # 최적의 비디오 및 오디오 스트림을 선택
    'outtmpl': 'temp_video.%(ext)s',  # 임시 저장 파일 이름
    'quiet': True,
    'noplaylist': True  # 플레이리스트가 아니라 하나의 동영상만 처리
}

# Use yt-dlp to get the video stream URL
with ytdlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(youtube_url, download=False)

    # Retrieve the best available video URL from the 'formats' list
    video_url = None
    for fmt in info_dict['formats']:
        if fmt.get('vcodec') != 'none' and fmt.get('acodec') != 'none':
            video_url = fmt['url']
            break

    if not video_url:
        print("Error: No suitable video stream found.")
        exit()

# Open video stream from YouTube using OpenCV
cap = cv2.VideoCapture(video_url)

if not cap.isOpened():
    print(f"Error: Unable to access video stream from {youtube_url}.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read frame from video or end of video reached.")
        break

    # Perform detection
    results = model(frame)
    detections = results.xyxy[0].cpu().numpy()  # Get detections

    # Draw bounding boxes and labels
    for *xyxy, conf, cls in detections:
        x1, y1, x2, y2 = map(int, xyxy)
        label = f"{model.names[int(cls)]} {conf:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("YOLOv5 Object Detection", frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
