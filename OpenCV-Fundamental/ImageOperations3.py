import cv2 as cv

img1 = cv.imread("Image/OpenCV-Logo.png")
img2 = cv.imread("Image/Python-Logo.png")
img1 = cv.resize(img1, (0,0), fx=0.5, fy=0.5)
img2 = cv.resize(img2, (0,0), fx=0.33, fy=0.33)

# Mask of logo and inverse
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 50, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

rows,cols,channels = img2.shape
roi =img1[0:rows, 0:cols]

img1_bg = cv.bitwise_and(roi, roi, mask = mask_inv)
img2_fg = cv.bitwise_and(img2, img2, mask = mask)

result = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = result

cv.imshow('Result', mask)
cv.imshow('Result2', mask_inv)
cv.imshow('Result3', img1_bg)
cv.imshow('Result4', img2_fg)
cv.imshow('img1', img1)
cv.waitKey(0)
cv.destroyAllWindows()