import cv2
from sliding import Slider
from handDetectionmodule import HandDetection
from flyingblock import Paddle
from collison2 import jump
import random
import numpy as np

WIDTH=1000
HEIGHT=700
xc=125
yc=575
sc=10
score=0

cap=cv2.VideoCapture(0)

'''mpHands=mp.solutions.hands
hands=mpHands.Hands(False)
mpDraw = mp.solutions.drawing_utils'''
detector=HandDetection(False,1,1,0.5,0.5)
paddle=Paddle(xc,yc,20)
slider=Slider(1050,550,20)

while True:
    success,img1=cap.read()
    img=cv2.flip(img1,1)
    img = cv2.resize(img, (WIDTH, HEIGHT))
    detector.findHand(img)   
    x=detector.findPosition(img)  
    '''game over condition'''
    if(slider.x-50<=150  and paddle.y+25>=500 and slider.x+50>=100):
        cv2.putText(img,"Game over",(WIDTH//2-50,HEIGHT//2),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        slider.reset(img)
    cv2.rectangle(img,(0,600),(1000,700),(255,0,0),-1,)
    
    paddle.draw(img)
    paddle.jumpButton(img)
    if len(x)!=0:
        x1,y1=x[8][1:]
        if( (x1<950 and x1>850 and y1<150 and y1>50)):
             paddle.moveup(img)  
             jump(paddle)
        elif((paddle.y<575)):
           paddle.moveup(img)  
           jump(paddle)            
    elif((paddle.y<575)):
         paddle.moveup(img)  
         jump(paddle)
    i=random.randint(2,10)
    
    slider.drawslider(img)
    slider.slide(img)
    if(slider.x<0):
        slider.reset(img)
        score+=1
    '''game over condition'''
    if(slider.x-50<=150  and paddle.y+25>=500 and slider.x+50>=100):
        cv2.putText(img,"Game over",(WIDTH//2-50,HEIGHT//2),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        paddle.draw(img)
        slider.drawslider(img)
        slider.reset(img)
        score=0
    '''score'''
    cv2.putText(img,f"Score:{score}",(20,20),cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    cv2.imshow("IMAGE",img)
    if cv2.waitKey(100)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    