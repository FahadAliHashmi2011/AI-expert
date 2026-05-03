import cv2
import numpy as np
import mediapipe as mp

from mediapipe.tasks.python import vision
from mediapipe.tasks.python import BaseOptions
import screen_brightness_control as sbc

options = vision.HandLandmarkerOptions(
    base_options = BaseOptions(model_asset_path = "lesson 16/hand_landmarker.task"),
    num_hands = 1
)

detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)
last_brightness =  -1

while True :
    success,frame = cap.read()
    if not success:
        break
    
    frame = cv2.flip(frame,1)
    h,w, _ = frame.shape
     
    rgb =cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB,data = rgb)
    
    result = detector.detect(mp_image)

    if result.hand_landmarks :
        for hand in result.hand_landmarks:
    
          thumb = hand[4]
          index = hand[8]

          x1,y1 = int(thumb.x*w), int(thumb.y*h)
          x2,y2 = int(thumb.x*w), int(thumb.y*h)

          cv2.circle(frame,(x1,y1),10,(255,0,0),-1)
          cv2.circle(frame,(x2,y2),10,(255,0,0),-1)
          cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),3)

          distance = np.hypot(x2 -x1,y2-y1)

          brightness = int(np.interp(distance,[30,300],[0,100]))

          if brightness != last_brightness:
                try:
                  sbc.set_brightness(brightness)
                except:
                  pass
            
            
          cv2.putText(frame,f"brightness :{brightness}%",
                      (50,50),cv2.FONT_HERSHEY_SIMPLEX,
                      1,(0,255,0), 2)
    cv2.imshow("brightness control",frame) 
    if cv2.waitKey(1) &0xFF == ord("q"):
       break

cap.release()
cv2.destroyAllWindows()
                  

