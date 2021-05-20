import cv2

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    sucess, img = cap.read()
    cv2.imshow("Result", img)

    if cv2.waiKey(1) & 0xFF == ord('q'):
        break