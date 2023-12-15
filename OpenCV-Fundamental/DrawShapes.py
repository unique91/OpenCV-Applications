import cv2 as cv
import numpy as np

img = np.zeros((512, 512), np.uint8)

# Draw a diagonal line
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 3)