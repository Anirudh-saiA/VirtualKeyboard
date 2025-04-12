import cv2
from cvzone.HandTrackingModule import HandDetector
from time import time
import numpy as np
import cvzone
from pynput.keyboard import Controller

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
        ["<- Backspace"]]

finalText = ""
keyboard = Controller()

class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text
        self.hoverStart = 0  # When finger started hovering

def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (x, y, w, h), 20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 15, y + 60),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img

# Create the keyboard buttons
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

# Variables to store finger state
activeKey = None
hoverStartTime = None

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        lmList = hands[0]["lmList"]
        xFinger, yFinger = lmList[8][0], lmList[8][1]  # Index fingertip

        # Check all buttons
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            # Check if finger is hovering over the button
            if x < xFinger < x + w and y < yFinger < y + h:
                # If not already hovering, start timer
                if activeKey != button:
                    activeKey = button
                    hoverStartTime = time()

                # If hovered for more than 1 seconds, register input
                elif time() - hoverStartTime >= 1:
                    if button.text == "<- Backspace":
                        finalText = finalText[:-1]
                    else:
                        keyboard.press(button.text)
                        finalText += button.text
                    # Reset hover
                    hoverStartTime = None
                    activeKey = None
                    break  # Prevent multiple keys triggering at once

                # Show hover feedback
                cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, button.text, (x + 15, y + 60),
                            cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                break
        else:
            # Reset if finger not hovering on any key
            activeKey = None
            hoverStartTime = None

    # Draw buttons and text area
    img = drawAll(img, buttonList)

    overlay = img.copy()
    cv2.rectangle(overlay, (50, 350), (700, 450), (175, 0, 175), cv2.FILLED)
    img = cv2.addWeighted(overlay, 0.4, img, 0.6, 0)
    cv2.putText(img, finalText, (60, 430),
                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    cv2.imshow("Virtual Keyboard", img)
    cv2.waitKey(1)
