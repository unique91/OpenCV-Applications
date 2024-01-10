import cv2 as cv
from ultralytics import YOLO

# Load pretrained model
model = YOLO('yolov8n-pose.pt')

cap = cv.VideoCapture(0)
cap.set(3, 1270)
cap.set(4, 720)

while True:
    ret, frame = cap.read()
    
    if ret:
        results = model.track(frame, persist=True)
        plot_result = results[0].plot()
        
        cv.imshow('HandTracker', plot_result)
    
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
    
cap.release()
cv.destroyAllWindows()