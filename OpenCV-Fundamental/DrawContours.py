import cv2 as cv
import numpy as np

img = cv.imread('Image/Shapes.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 200)

contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
print("Number of Contours found = " + str(len(contours))) 
#cv.drawContours(img, contours, -1, (255, 0, 0), 3)
#cv.imshow('Contours', img)
cnt = contours[4]
cv.drawContours(img, [cnt], 0, (0, 0, 255), 3)

# Moments
cnt2 = contours[1]
M = cv.moments(cnt2)
# print(M)

# Contour Area
area = cv.contourArea(cnt2)  # M['m00']
# print(area)

# Contour Approximation
epsilon = 0.1 * cv.arcLength(cnt2, True)
approx = cv.approxPolyDP(cnt2, epsilon, True)

# Bounding Rectangle
x, y, w, h = cv.boundingRect(cnt2)
cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Rotated Rectangle
rect = cv.minAreaRect(cnt2)
box = cv.boxPoints(rect)
box = np.int0(box)
cv.drawContours(img, [box], 0, (0, 0, 255), 2)

# Aspect Ratio
aspect_ratio = float(w) / h
print('Aspect Ratio = ', aspect_ratio)

# Extent
rect_area = w * h
extent = float(area) / rect_area
print('Extent = ', extent)

# Mask and Pixel Points
mask = np.zeros(gray.shape, np.uint8)  # row = y and column = x
cv.drawContours(mask, [cnt], 0, 255, -1)
pixelpoints = np.transpose(np.nonzero(mask))
print('Pixelpoints = ', pixelpoints)

# Maximum value, minimum value and their locations
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(gray, mask = mask)

# Mean Color or Mean Intensity
mean_val = cv.mean(img, mask = mask)

# Output
cv.imshow('Contours', img)  
cv.waitKey(0)
cv.destroyAllWindows()