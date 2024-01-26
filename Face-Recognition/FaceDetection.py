import cv2

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

def detect_bbx(img):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_classifier.detectMultiScale(gray_img, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
    return face

while True:
    ret, frame = cap.read()
    
    if ret is False:
        break
    
    face = detect_bbx(frame)
    cv2.imshow("Frame", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()