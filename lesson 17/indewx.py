import cv2 
import time
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
from pynput.mouse import Controller
 
mouse = Controller()
base_options = python.BaseOptions(
    model_asset_path = "lesson 17/hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands = 1
)
detector = vision.HandLandmarker.create_from_options(options)
cap = cv2.VideoCapture(0)
last_scroll = 0
SCROLL_DELAY = 0.5
def count_fingers(hand):
    tips = [8,12,16,20]
    landmarks = hand
    count = 0
    for tip in  tips:
        if landmarks[tip].y < landmarks[tip - 2].y:
            count +=  1
    return count
while True :
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame,1)
    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format = mp.ImageFormat.SRGB,data=rgb )
    result =  detector.detect(mp_image)
    gesture = "None"
    if result.hand_landmarks:
        hand = result.hand_landmarks[0]

        fingers = count_fingers(hand)
        now = time.time()
        if fingers == 4 :
            gesture = "Scroll up"
            if now - last_scroll >SCROLL_DELAY:
                mouse.scroll(0,2)
                last_scroll=now
        elif fingers == 0 : 
            gesture = "Scroll down "
            if now - last_scroll >SCROLL_DELAY:
                mouse.scroll(0,-2)
                last_scroll=now
    
    cv2.putText(frame,f"Gesture:{gesture}",(10,40),
                cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    
    cv2.imshow("hand scroll control", frame)
    if cv2.waitKey(1)&0xFF  == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()






                   
