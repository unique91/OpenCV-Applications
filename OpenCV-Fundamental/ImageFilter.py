import cv2 as cv

def do_nothing(x):
    pass

cv.namedWindow('Image')
# Trackbars for color change
cv.createTrackbar('Red', 'Image', 0, 255, do_nothing)
cv.createTrackbar('Green', 'Image', 0, 255, do_nothing)
cv.createTrackbar('Blue', 'Image', 0, 255, do_nothing)

img_path = "Image/Lena.png"
img = cv.imread(img_path, 1)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.blur(img, (5, 5))
gaussianBlur = cv.GaussianBlur(img, (5, 5), 0)

cv.imshow("Original Image", img)
cv.imshow("Grayscale Image", gray)
cv.imshow("Blurring Image", blur)
cv.imshow("Gaussian Blurring Image", gaussianBlur)

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()
