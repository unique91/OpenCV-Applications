import sys
import cv2
print(f"Python: {sys.version}")
print(f"OpenCV: {cv2.__version__}")

img_path = "Image/OpenCV-Logo.png"
img = cv2.imread(img_path, cv2.IMREAD_COLOR)
img = cv2.resize(img, (600, 600))
img_ccw = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

crop = img[200:300, 400:500]
img[50:150, 100:200] = crop

# print(type(img))
# print(img.shape)

cv2.imshow("Original image", img)
cv2.imshow("Image 90 CCW", img_ccw)
cv2.waitKey(0)
cv2.destroyAllWindows()