import numpy as np
import cv2 as cv

num_cameras = 0
cap = cv.VideoCapture(num_cameras)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    img = np.zeros(frame.shape, np.uint8)
    smaller_img = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
    img[:height//2, :width//2] = cv.rotate(smaller_img, cv.ROTATE_180)   # Top-left
    img[height//2:, :width//2] = smaller_img    # Bottom-left
    img[:height//2, width//2:] = cv.rotate(smaller_img, cv.ROTATE_180)   # Top-right
    img[height//2:, width//2:] = smaller_img     # Bottom-right
    
    cv.imshow("Camera", img)
    
    # Close window with q-button
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()