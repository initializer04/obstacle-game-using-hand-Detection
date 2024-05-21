import cv2


class Paddle:
    def __init__(self, x, y,block_vel):
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.block_vel=block_vel

    def jumpButton(self,frame):
         self.circle=cv2.circle(frame,(900,100),50,(0,255,0),-1)
         cv2.putText(self.circle,"JUMP",(860,110),cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    def draw(self, frame):
        self.img=cv2.rectangle(frame,(self.x-25,self.y-25),(self.x+25,self.y+25),(0,0,255),-1,)
    
    def moveup(self, frame):
              self.y-=self.block_vel
    def reset(self,frame):
            self.y=self.original_y