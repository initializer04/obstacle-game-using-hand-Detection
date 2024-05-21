import cv2
import mediapipe as mp
import time
import pyautogui

class HandDetection():
    def __init__(self,mode=False,
               maxhands=2,
               model_complexity=1,
               min_detection_confidence=0.5,
               min_tracking_confidence=0.5):
        self.mode=mode
        self.maxhands=maxhands
        self.model_complexity=model_complexity
        self.min_detection_confidence=min_detection_confidence
        self.min_tracking_confidence=min_tracking_confidence

        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(self.mode,self.maxhands,self.model_complexity,self.min_detection_confidence,self.min_tracking_confidence)
    
        self.mpDraw = mp.solutions.drawing_utils

    def findHand(self,img):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)         
        self.result=self.hands.process(imgRGB)
        #print(result.multi_hand_landmarks)             
        #qprint(result.multi_handedness)
        if self.result.multi_hand_landmarks:

            for self.handLms in self.result.multi_hand_landmarks:
               
                    self.mpDraw.draw_landmarks(img,self.handLms,self.mpHands.HAND_CONNECTIONS)

    def findPosition(self,img):
         lmList=[]
         if self.result.multi_hand_landmarks:
              for id,lm in enumerate(self.handLms.landmark):
                   h,w,c=img.shape
                   cx,cy=int(lm.x*w),int(lm.y*h)
                   lmList.append([id, cx, cy])
                   cv2.circle(img,(cx,cy),5,(0,255,0),-1)

         return lmList       