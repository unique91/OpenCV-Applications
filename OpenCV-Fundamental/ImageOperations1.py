import cv2 as cv
import numpy as np

img_path = "Image/Lena.png"
img = cv.imread(img_path)

if img is None:
    print("Image not found!")
else:
    print("Image found!")

# Accessing and Modifying pixel values    
px_value = img[55, 55]
print(f"Old value = {px_value}")

img[55, 55] = [255, 255, 255]
print(f"New value = {img[55, 55]}")

# Iterate through width and height 
for h in range(0, img.shape[0]):
    for w in range(0, img.shape[1]):
        img[h//2, w//2] = [255, 255, 255]

# Image ROI
roi = img[20:30, 50:80]
img[120:130, 100:130] = roi

# Splitting and Merging Image Channels
# b, g, r = cv.split(img)
# b = img[:,:,0]
# Numpy indexing is faster!
img[:,:,2] = 0

# Border for Image
const = cv.copyMakeBorder(img, 5, 5, 5, 5, cv.BORDER_CONSTANT, value=[0, 255, 0])

cv.imshow("Image", const)
cv.waitKey(0)
cv.destroyAllWindows()