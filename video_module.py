import socket
import cv2 as opencv

video_stream = opencv.VideoCapture('udp://@0.0.0.0:11111')

while True:
    try:
        ret, frame = video_stream.read()
        if ret:
            opencv.imshow('Tello', frame)
        if opencv.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as err:
        video_stream.release()
        opencv.destroyAllWindows()
        print(err)

video_stream.release()
opencv.destroyAllWindows()
