import cv2 as cv
from matplotlib import pyplot as plt

img_path = "Image/Lena.png"
img = cv.imread(img_path, cv.IMREAD_GRAYSCALE)

def do_nothing(x):
    pass

cv.namedWindow('Image')
cv.createTrackbar("Max", "Image", 0, 255, do_nothing)
cv.createTrackbar("Min", "Image", 0, 255, do_nothing)

while(1):
    hul=cv.getTrackbarPos("Max", "Image")
    huh=cv.getTrackbarPos("Min", "Image")
    ret,thresh1 = cv.threshold(img,hul,huh,cv.THRESH_BINARY)
    ret,thresh2 = cv.threshold(img,hul,huh,cv.THRESH_BINARY_INV)
    ret,thresh3 = cv.threshold(img,hul,huh,cv.THRESH_TRUNC)
    ret,thresh4 = cv.threshold(img,hul,huh,cv.THRESH_TOZERO)
    ret,thresh5 = cv.threshold(img,hul,huh,cv.THRESH_TOZERO_INV)
    # cv2.imshow(wnd)
    cv.imshow("thresh1",thresh1)
    cv.imshow("thresh2",thresh2)
    cv.imshow("thresh3",thresh3)
    cv.imshow("thresh4",thresh4)
    cv.imshow("thresh5",thresh5)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv.destroyAllWindows()


