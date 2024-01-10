import cv2 as cv
import numpy as np

# Required for Trackbar
def do_nothing():
    pass

# Init Webcam video
video = cv.VideoCapture(0)
video.set(3, 1280)
video.set(4, 720)
cv.namedWindow('HSV Tracker')

# Define H-S-V Range 
# HSV stands for Hue, Saturation and Value
cv.createTrackbar('Min Hue', 'HSV Tracker', 0, 179, do_nothing)
cv.createTrackbar('Max Hue', 'HSV Tracker', 179, 179, do_nothing)
cv.createTrackbar('Min Saturation', 'HSV Tracker', 0, 255, do_nothing)
cv.createTrackbar('Max Saturation', 'HSV Tracker', 255, 255, do_nothing)
cv.createTrackbar('Min Value', 'HSV Tracker', 0, 255, do_nothing)
cv.createTrackbar('Max Value', 'HSV Tracker', 255, 255, do_nothing)

while True:
    _, frame = video.read()
    
    # Flip image frame horizontally
    frame = cv.flip(frame, 1)
    
    # Convert BGR to HSV
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    
    # Get values from user input
    min_h = cv.getTrackbarPos('Min Hue', 'HSV Tracker')
    max_h = cv.getTrackbarPos('Max Hue', 'HSV Tracker')
    min_s = cv.getTrackbarPos('Min Saturation', 'HSV Tracker')
    max_s = cv.getTrackbarPos('Max Saturation', 'HSV Tracker')
    min_v = cv.getTrackbarPos('Min Value', 'HSV Tracker')
    max_v = cv.getTrackbarPos('Max Value', 'HSV Tracker')
    
    # Set lower and upper range for hsv
    lower_range = np.array([min_h, min_s, min_v])
    upper_range = np.array([max_h, max_s, max_v])
    
    # Compute the binary mask, where white represents
    mask = cv.inRange(hsv_frame, lower_range, upper_range)
    
    result = cv.bitwise_and(frame, frame, mask=mask)
    
    channel3 = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    
    # Convert to horizontally stack
    hstack = np.hstack((channel3, frame, result))
    
    cv.imshow('HSV Tracker', cv.resize(hstack, None, fx=0.5, fy=0.5))
    
    # Close condition
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv.destroyAllWindows()
