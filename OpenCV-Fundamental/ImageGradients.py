import cv2 as cv

img = cv.imread('Image/Lena.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Opencv provides several types of gradient filters.

# 1. Sobel Filter: The sobel operator is a gradiend based method based on the first order derivatives.
# It calculate two kernels one for horizontal direction and one for vertical direction.
ksize = 1
gx = cv.Sobel(gray, ddepth=cv.CV_32F, dx=1, dy=0, ksize=ksize)
gy = cv.Sobel(gray, ddepth=cv.CV_32F, dx=0, dy=1, ksize=ksize)
# Convert from floating point data type to unsigned 8-bit integer
# so other opencv functions can operate on them
gx = cv.convertScaleAbs(gx)
gy = cv.convertScaleAbs(gy)

# Combine the gradient into a single image
sobelXY = cv.addWeighted(gx, 0.5, gy, 0.5, 0)

# 2. Laplacian Filter: The Laplacian operator uses only one kernel.
# It calculates second order derivates in a single pass.
laplacian = cv.Laplacian(gray, ddepth=cv.CV_32F, ksize=ksize)

cv.imshow('Original Image', img)
cv.imshow('Gray Image', gray)
cv.imshow('Sobel Operator', sobelXY)
cv.imshow('Laplacian Operator', laplacian)
cv.waitKey(0)