import cv2 as cv

img = cv.imread('Image/Lena.png', cv.IMREAD_GRAYSCALE)

if img is None:
    print("File couldn't be read!")
    
def do_nothing(x):
    pass

cv.namedWindow('Canny')
switch = '0 : OFF \n1 : ON'
cv.createTrackbar(switch, 'Canny', 0, 1, do_nothing)
cv.createTrackbar('thres1', 'Canny', 0, 255, do_nothing)
cv.createTrackbar('thres2', 'Canny', 0, 255, do_nothing)

thres1 = 80
thres2 = 200
while True:
    thres1 = cv.getTrackbarPos('thres1', 'Canny')
    thres2 = cv.getTrackbarPos('thres2', 'Canny')
    s = cv.getTrackbarPos(switch, 'Canny')
    # Canny edge detector uses a three-stage procedure to extract edges from an image.
    canny = cv.Canny(img, thres1, thres2)
    
    if s == 0:
        canny = img
    else:
        canny = cv.Canny(img, thres1, thres2)

    cv.imshow('Gray Image', img)
    cv.imshow('Canny Image', canny)
    
    if cv.waitKey(1) == 27 & 0xFF:
        break
    
cv.destroyAllWindows()