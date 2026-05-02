import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
base_options = python.BaseOptions(model_asset_path="lesson 15/hand_landmarker.task")
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands = 2,
    min_hand_detection_confindence = 0.7,
    min_tracking_confindence = 0.7
)

detetctor = vision.HandLandmarker.create_from_options(options)
cap =cv2.VideoCapture(0)

def detect_getsure(lm):
    tips = [4,8,12,16,20]
    pips = [2,6,10,14,18]
    count = 0
    if abs(lm[tips[0]].x -lm[pips[0]].x)>0.04:
        count+=1
    for i in range(1,5):
        if lm[tips[i]].y<lm[pips[i]].y:
            count+=1
    
    if count >= 4:
        return "Open"
    elif count <= 1:
        return "Fist"
    return "Partial"
print("press q to quit")

while True :
    ret,frame = cap.read()
    if  not ret :
        break
    frame=cv2.flip(frame,1)
    h,w, _ =frame.shape

    rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format = mp.ImageFormat.SRGB, data=rgb)
    result = detetctor  .detect(mp_image)
    gesture = "No hand"
    if result.hand_landmarks:
        for i, hand in enumerate(result.hand_landmarks):
            label = result.handedness[i][0].category_name
            label = "Right" if label =="Left" else "Left"

            gesture = detect_getsure(hand)
            
            for id, lm  in enumerate(hand):
                x,y = int(lm.x*w), int(lm.y*h)
                size = 8 if id in [4,8,12,16,20] else 3
                cv2.circle(frame, (x,y),size,(0,255,0),-1)
            
            wx,wy = int(hand[0].x*w),int(hand[0].y*h)
            cv2.putText(fraem,)

    
