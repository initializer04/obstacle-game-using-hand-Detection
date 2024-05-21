import cv2
import random
class Slider:
   
    def __init__(self,x,y,m_vel):
        self.x=self.orig=x
        self.y=y
        self.m_vel=m_vel
    def drawslider(self,frame):
        cv2.rectangle(frame,(self.x-50,self.y-50),(self.x+50,self.y+50),(255,0,255),-1)

    def slide(self,frame):
        self.x-=self.m_vel
    def reset(self,frame):
        self.x=random.randint(1000,2000)


