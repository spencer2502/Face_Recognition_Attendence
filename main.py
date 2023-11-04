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