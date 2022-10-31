from cvzone.HandTrackingModule import HandDetector as hd
import mediapipe as mp
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = hd()


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    img2 = cv2.imread("Cat03.jpg")

    # img[0:1026, 0:1024] = img2

    if len(hands) == 2:
        print("tiene 2 manos en camara")
        if detector.fingersUp(hands[0][0]) and detector.fingersUp(hands[0][1]) and detector.fingersUp(hands[1][0]) and detector.fingersUp(hands[1][1]):
            print("gesto de zoom")


    cv2.imshow("camara", img)
    cv2.waitKey(1)


