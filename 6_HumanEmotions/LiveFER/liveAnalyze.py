from fer import FER
import os
import sys
import pandas as pd
import cv2

capture = cv2.VideoCapture(0)
detector = FER()

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        print("Error")
        break
    if cv2.waitKey(1) == ord('q'):
        break

    data = detector.detect_emotions(frame)

    for point in data:
        box = point['box']
        cv2.rectangle(frame, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (255, 255, 0), 2)
        i = 1
        separation = 15
        for emotion, amount in point['emotions'].items():
            cv2.putText(frame, f"{emotion}: {amount}", (box[0], box[1] + box[3] + i * separation), cv2.FONT_HERSHEY_SIMPLEX, .3, (0, 255, 0))
            i += 1
    cv2.imshow('Live FER', frame)

    
capture.release()
cv2.destroyAllWindows()