import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

while(True):
    # Read image frame
    _, frame = video.read()
    
    # Convert from BGR to HSV colorspace
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # Extract red color from HSV frame
    l_red = np.array([161, 155, 84])
    u_red = np.array([179, 255, 255])
    
    # Threshold the HSV frame to get red value
    mask = cv.inRange(hsv, l_red, u_red)
    
    # Bitwise-and 
    result = cv.bitwise_and(frame, frame, mask=mask)
    
    cv.imshow('Frame', frame)
    cv.imshow('Mask', mask)
    cv.imshow('Result', result)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()