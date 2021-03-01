from pygame.math import Vector2
import pygame as pg

class Entity:
    def __init__(self,position,mass=5):
        self.mass = mass
        self.position = Vector2(position)
        self.acceleration = Vector2(0,0)
        self.velocity = Vector2(0,0)
    
    def draw(self,screen,color):
        pg.draw.circle(screen,color,self.position,10)

    def update(self):
        self.velocity = self.velocity + self.acceleration
        self.position = self.velocity + self.position
        self.acceleration = self.acceleration*0
        
    
    def apply_force(self,force):
        res = force/self.mass
        self.acceleration = self.acceleration + res
    
    def edges(self,s_width,s_height):
        if(self.position.x > s_width):
            self.position.x = 0
        elif(self.position.x < 0):
            self.position.x= s_width
        
        if(self.position.y > s_height):
            self.position.y = 0
        elif(self.position.y < 0):
            self.position.y= s_height
    
    
