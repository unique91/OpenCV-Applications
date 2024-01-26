import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_file = cv.imread("Image/foto.jpg", cv.IMREAD_GRAYSCALE)
rows, cols = img_file.shape

if img_file is None:
    print("File couldn't read.")

# Scaling
scal = cv.resize(img_file, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)

# Translation
M = np.float32([[1,0,100],[0,1,50]])  # 2x3 transformation matrix
trans = cv.warpAffine(img_file, M, (cols,rows))

# Rotation
# (cols-1) and (rows-1) represent the coordinate limits.
M2 = cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 180, 1)
rot = cv.warpAffine(img_file, M2, (cols, rows))

# Affine Transformation
p1 = np.float32([[50,50],[200,50],[50,200]])
p2 = np.float32([[10,100],[200,50],[100,250]])

M3 = cv.getAffineTransform(p1, p2)  #2x3 transformation matrix
aff_trans = cv.warpAffine(img_file, M3, (cols, rows))

# Perspective Transformation
p1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
p2 = np.float32([[0,0],[300,0],[0,300],[300,300]])

M4 = cv.getPerspectiveTransform(p1, p2)
pers_trans = cv.warpPerspective(img_file, M4, (400, 750))

plt.subplot(231), plt.imshow(img_file), plt.title('Original')
plt.subplot(232), plt.imshow(scal), plt.title('Scaling')
plt.subplot(233), plt.imshow(trans), plt.title('Translation')
plt.subplot(234), plt.imshow(rot), plt.title('Rotation')
plt.subplot(235), plt.imshow(aff_trans), plt.title('Affine Transformation')
plt.subplot(236), plt.imshow(pers_trans), plt.title('Perspective Transformation')
plt.show()

if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()