import pygame as pg
from pygame.math import Vector2
import pygame.gfxdraw as gfx
import random

class Ray:
    def __init__(self, p1, p2, width=1):
        self.p1 = p1
        self.p2 = p2
        self.width = width

    def set_head(self,new_head):
        self.p2 = new_head

    def draw(self,screen, color):
        #pg.draw.line(screen,color ,self.p1, self.p2,self.width)
        gfx.line(screen,int(self.p1.x),int(self.p1.y),int(self.p2.x),int(self.p2.y),color)
    
    def normalize(self):
        dir = (self.p2 - self.p1)
        self.p2 = self.p1+(dir.normalize()*10)

    def set_magnitude(self,mag):
        dir = (self.p2 - self.p1)
        self.p2 = self.p1+(dir.normalize()*mag)
    
    def intersects(self,other):
        return cramer(self.p1,self.p2,other.p1,other.p2)
    
    @staticmethod
    def lerp(val1,val2,scalar):
        return (1-scalar)*val1 + scalar*val2

    @staticmethod
    def random(screen_x,screen_y, max_len):
        x1 = random.randint(0,screen_x)
        y1 = random.randint(0,screen_y)

        x2 = random.randint(0,screen_x)
        y2 = random.randint(0,screen_y)

        p1 = Vector2(x1,y1)
        p2 = Vector2(x2,y2)
        magnitude = Ray.lerp(max_len*0.5,max_len,random.random())
        ray = Ray(p1,p2)
        ray.set_magnitude(magnitude)
        return ray
        
    



def cramer(p1, p2, q1, q2):
    '''
        Cramer's method

        #first line parametric equation
        r1: p1.x + dirP.x *(t)  p1+dirP*(t) t€R, t>0
            p1.y + dirP.y *(t)

        #second line parametric equation
        r2: q1.x + dirQ.x *(s)  q1 +dirQ*(s) s€R, 0 <= s <= 1
            q1.y + dirQ.y *(s)
        
        
        system:
        p1.x + dirP.x *t = q1.x + dirQ.x *s
        p1.y + dirP.y *t = q1.y + dirQ.y *s
        -----------------------------------
        #Incomplete matrix determinant
        dirP.x*t - dirQ.x*s = q1.x - p1.x
        dirP.y*t - dirQ.y*s = q1.y - p1.y

        D = (dirP.x * -dirQ.y) - (-dirQ.x * dirP.y)
        -------------------------------------------
        #t variable matrix determinant
        (q1.x -p1.x) - dirQ.x
        (q1.y -p1.y) - dirQ.y

        Dt = ((q1.x -p1.x) * (-dirQ.y)) -  ((-dirQ.x)*((q1.y -p1.y)))
        -------------------------------------------------------------

        #s variable matrix  determinant
        dirP.x + (q1.x - p1.x)
        dirP.y + (q1.y - p1.y)

        Ds = (dirP.x *(q1.y - p1.y)) - ((q1.x - p1.x) * dirP.y)

    '''

    dirP = p2-p1
    dirQ = q2-q1

    D = (dirP.x *(-dirQ.y)) - (-dirQ.x *dirP.y)
    Dt = ((q1.x -p1.x) * (-dirQ.y)) -  ((-dirQ.x)*((q1.y -p1.y)))
    Ds = (dirP.x *(q1.y - p1.y)) - ((q1.x - p1.x) * dirP.y)

    if(D==0):
        #raise Exception("Divide by 0 exception")
        return None

    t = Dt/D
    s = Ds/D

    #(p1.x + dirP.x *t) == (q1.x + dirQ.x *s) and (p1.y + dirP.y *t)== (q1.y + dirQ.y *s) 
    if(0<= s <= 1 and t > 0):
        #x = p1.x + dirP.x *(t)
        #y = p1.y + dirP.y *(t)
        x = q1.x + dirQ.x *(s)
        y = q1.y + dirQ.y *(s)
        return Vector2(x,y)
    else:
        return None


    

