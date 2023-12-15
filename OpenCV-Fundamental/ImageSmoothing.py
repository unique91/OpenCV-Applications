import cv2 as cv

img_path = "Image/Lena.png"
img = cv.imread(img_path, 1)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.blur(img, (5, 5))
gaussianBlur = cv.GaussianBlur(img, (5, 5), 0)

cv.imshow("Original Image", img)
cv.imshow("Grayscale Image", gray)
cv.imshow("Blurring Image", blur)
cv.imshow("Gaussian Blurring Image", gaussianBlur)

cv.waitKey(0)
cv.destroyAllWindows()