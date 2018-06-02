import cv2
face_cascade = cv2.CascadeClassifier(".\\cascades\\haarcascade_frontalface_default.xml")
capture = cv2.VideoCapture(0)


while True:
    ss, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (w+x, y+h), (255, 0, 0), 2)
    cv2.namedWindow("Human Detected!")
    cv2.imshow("Human Detected!", frame)
    k = cv2.waitKey(30)
    if k == 27:
        break