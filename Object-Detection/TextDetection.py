import cv2 as cv
import pytesseract

# *** Hint: In this example I use the tesseract lib for recognize character from images. ***

img = cv.imread("Image/text.png")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# print(pytesseract.image_to_string(img))
hImg, wImg, _ = img.shape

# Choose your operation.
print(f"Following options can you choose:")
print(f"(1) Printing boxes around the characters")
print(f"(2) Detect the words in image")
print(f"(3) Detect only digits in image")
number = int(input("Enter your choice: "))
# Add Bounding box arround the character and detect them
if number == 1:
    boxes = pytesseract.image_to_boxes(img)
    for b in boxes.splitlines():
        b = b.split(' ')
        # List: [Sign, X, Y, Width, Heigh]
        X, Y, W, H = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv.rectangle(img, (X, hImg-Y), (W, hImg-H), (255, 0, 0), 1)
        cv.putText(img, b[0], (X, hImg-Y-20), cv.FONT_HERSHEY_COMPLEX, 1, (25, 25, 25), 1)
if number == 2:  
    # Detect the correct words
    boxes = pytesseract.image_to_data(img)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                X, Y, W, H = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv.rectangle(img, (X, Y), (W+X, H+Y), (255, 0, 0), 1)
                cv.putText(img, b[11], (X, Y), cv.FONT_HERSHEY_COMPLEX, 1, (25, 25, 25), 1)
if number == 3:
    custom_oem_psm_config = r" --oem 3 --psm 6 outputbase digits"    
    boxes = pytesseract.image_to_data(img, config=custom_oem_psm_config)
    for x, b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split()
            if len(b) == 12:
                X, Y, W, H = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv.rectangle(img, (X, Y), (W+X, H+Y), (255, 0, 0), 1)
                cv.putText(img, b[11], (X, Y), cv.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 1)

cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()