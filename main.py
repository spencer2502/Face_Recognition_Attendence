import os
import pickle
import numpy as np
import  cv2
import face_recognition
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import  db
from datetime import  datetime


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

while True :
    success, img = cap.read()

    imgS = cv2.resize(img,(0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)

    imgBackground[162:162+480, 55:55+640] = img
    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

