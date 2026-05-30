import cv2
import time
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

base_options = python.BaseOptions(
    model_asset_path="lesson 18/hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)
SEPIA_MATRIX =np.array([
    [ 0.272, 0.534, 0.131]
    [ 0.349, 0.686, 0.168]
    [ 0.393, 0.769, 0.189]
    
])

FILTERS = ["SEPIA","NEGATIVE","BLUR","EDGE","CARTOON"]
current_filter = 0

last_gesture_time = 0
GETURE_COOLDOWN = 0.6


def dist (a,b):
    return np.hypot( a[0]-b[0],  a[1]-b[1])
    


def apply_filter(img,mode):
    if mode == "SEPIA":
        return np.clip(cv2.transform(img,SEPIA_MATRIX),0,255).astype(np.uint8)
    elif mode == "NEGATIVE":
        return cv2.bitwise_not(img)   
    elif mode == "BLUR":
        return cv2.GaussianBlur(img,(15,15),0)
    elif mode == "EDGE":
        e = cv2.canny(cv2.cvtColor(img,cv2.COLOR_BGR2GRAY),80,160)
        return cv2.cvtColor(e,cv2.COLOR_GRAY2BGR)
    elif mode == "CARTOON":
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        edges = cv2.adaptiveThreshold(
            cv2.medianBlur(gray,7),
            255,
            cv2.ADAPTIVE_THRESH_MEAN_C,
            cv2.THRESH_BINARY,
            9,
            2
        )
        color = cv2.bilateralFilter(img,9,75,75)
        return cv2.bitwise_and(color,color,mask=edges)
    return img
cap = cv2.VideoCapture(0)
while cap.isOpened():
    ok,frame = cap.read()
    if not ok:
        break

    frame = cv2.flip(frame,1)
    h,w = frame.shape[:2]

    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)