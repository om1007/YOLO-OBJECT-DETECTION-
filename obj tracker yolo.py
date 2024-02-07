import cv2
import ultralytics
from ultralytics import YOLO

# load yolov8 model 

model = YOLO(r'C:\Users\om\Desktop\CV\yolov8n.pt')

# load video 

cap = cv2.VideoCapture(r"C:\Users\om\Desktop\CV\test.mp4")

ret = True
#read frames 
while ret:
    ret, frame = cap.read()

    # detect objects & track objects
    
    results = model.track(frame, persist=True)
    

    # plot results

    frame_ = results[0].plot()


    # visualize 
    cv2.imshow('frame',frame_)
    if cv2.waitKey(25) & 0XFF == ord('q'):
            break
