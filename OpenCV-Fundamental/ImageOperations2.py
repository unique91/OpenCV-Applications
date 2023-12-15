import cv2 as cv

# Image Blending
# dst = alpha * img1 + beta * img2 + gamma

alpha = 0.5
beta = 0.7
gamma = 2.0

dim = (400, 400)

img1 = cv.imread("Image/OpenCV-Logo.png")
img2 = cv.imread("Image/Python-Logo.png")

# Both images need the same size
img1 = cv.resize(img1, dim)
img2 = cv.resize(img2, dim)

# add (or blend) the images
result = cv.addWeighted(img1, alpha, img2, beta, gamma)

cv.namedWindow('Result', cv.WINDOW_AUTOSIZE)
cv.imshow('Result', result)
cv.waitKey(0)
cv.destroyAllWindows()

