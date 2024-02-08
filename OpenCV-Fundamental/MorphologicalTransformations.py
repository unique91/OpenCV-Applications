import cv2 as cv
import numpy as np

img = cv.imread('Image/binary.jpg', cv.IMREAD_GRAYSCALE)

if img is None:
    print("File couldn't be read!")
    
# 1. Erosion: Erodes away the boundaries of the foreground object.
# Benefit: Useful for removing small white noises
kernel = np.ones((5, 5), np.uint8)
erosion = cv.erode(img, kernel, iterations=1)

# 2. Dilation: Dilation increases the object area.
# Benefit: Useful in combination of erosion because while erosion remoces white noises
# and shrinks our object, the dilation increases the object area and joined broken parts.
dilation = cv.dilate(img, kernel, iterations=1)

# 3. Opening: Combines erosion and dilation in one step.
# First come erosion then dilation
# Benefit: Useful in removing noise
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)

# 4. Closing: Reverse of Opening, dilation followed by erosion
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

cv.imshow('Original Image', img)
cv.imshow('Erosion Image', erosion)
cv.imshow('Dilation Image', dilation)
cv.imshow('Morphology Opening', opening)
cv.waitKey(0)
cv.destroyAllWindows()

