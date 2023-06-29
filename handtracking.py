import cv2
import mediapipe as mp
import serial
import time
tip, bottom = 1, 1
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
distance = 5
ard = serial.Serial('COM4', baudrate=9600)
time.sleep(2)
print(ard.name)

while True:
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)
    if results.multi_hand_landmarks:
        for id, lm in enumerate(results.multi_hand_landmarks[0].landmark):
            h, w, c = image.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            if id == 5:
                tip = cy
                cv2.circle(image, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
            if id == 8:
                bottom = cy
                cv2.circle(image, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
                distance = tip - bottom
                if distance <= 0:
                    distance = 0
                if distance >= 150:
                    distance = 150
        mpDraw.draw_landmarks(image, results.multi_hand_landmarks[0], mpHands.HAND_CONNECTIONS)   
        ard.write(bytes(str(distance) +'\n', 'utf-8'))
        print(bytes(str(distance), 'utf-8')) 
    cv2.imshow("Hand Scanner", image)
    cv2.waitKey(1)
    
