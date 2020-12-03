'''
    https://www.youtube.com/watch?v=-RtVZsCvXAQ
    In this video on OpenCV Python Tutorial For Beginners,
    I am going to show How to Read, Write, Show Videos from Camera in OpenCV.
    We will see How to read video, display video and save video,
    How to capture from Camera and display it, we will see these functions:
    cv.VideoCapture(), cv.VideoWriter().
    We will Capture Video from Camera using opencv.
    So let us see How to process images of a video, frame by frame in video streaming using Opencv python.
'''
import cv2
cap = cv2.VideoCapture(0) #can be 0 or -1, depends on your pc setting

while(True):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()