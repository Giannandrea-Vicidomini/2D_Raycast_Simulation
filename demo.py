from utils.game import GameFramework
import pygame as pg
from pygame.math import Vector2
from utils.entity import Entity
import math
from ray import Ray
from caster import Caster
import vnoise



class Demo(GameFramework):

    def __init__(self,size,title):
        super(Demo,self).__init__(size,title)
        self.circle = Entity((self.screen_width/2,self.screen_height/2))
        self.start_pos = None
        self.end_pos = None
        self.walls = []
        self.caster = None
        self.ray_number = 500
        self. wall_number = 9
        self.noise = vnoise.Noise()
        
    #INITIALISATION CALLBACK
    def on_create(self):

        self.caster = Caster((self.screen_width/2,self.screen_height/2),self.ray_number)

        for i in range(self.wall_number):
            w = Ray.random(self.screen_width,self.screen_height,200)
            self.walls.append(w)

        #boundaries
        left = Ray(Vector2(0,0),Vector2(0,self.screen_height),4)
        right = Ray(Vector2(self.screen_width-1,0),Vector2(self.screen_width-1,self.screen_height),4)
        top = Ray(Vector2(0,0),Vector2(self.screen_width,0),4)
        bottom = Ray(Vector2(0,self.screen_height-1),Vector2(self.screen_width,self.screen_height-1),4)

        
        self.walls.append(left)
        self.walls.append(right)
        self.walls.append(top)
        self.walls.append(bottom)

    '''
    def on_mouse_down(self, pos_x, pos_y):
        self.start_pos = Vector2(pos_x,pos_y)
        
    '''

    def on_mouse_up(self, pos_x, pos_y):
        
        self.walls = self.__recreate_walls()
    
    #DRAWING CALLBACK
    def on_update(self, screen, delta_time,time):
        screen.fill((22,22,22))
        '''
        offsetx = math.sin(time)*0.25 +0.25
        x = self.noise.noise1(offsetx)
        x = self.map_range(x,0,5,0,self.screen_width)

        print(x,offsetx)
        '''
        self.caster.draw(screen,(255,255,255),self.walls)
        self.caster.set_position(Vector2(self.mouse_x,self.mouse_y))
        #self.caster.set_position(Vector2(x,self.mouse_y))
    
    def __recreate_walls(self):
        walls = []
        for i in range(self.wall_number):
            w = Ray.random(self.screen_width,self.screen_height,200)
            walls.append(w)

        
        left = Ray(Vector2(0,0),Vector2(0,self.screen_height),4)
        right = Ray(Vector2(self.screen_width-1,0),Vector2(self.screen_width-1,self.screen_height),4)
        top = Ray(Vector2(0,0),Vector2(self.screen_width,0),4)
        bottom = Ray(Vector2(0,self.screen_height-1),Vector2(self.screen_width,self.screen_height-1),4)

        
        walls.append(left)
        walls.append(right)
        walls.append(top)
        walls.append(bottom)

        return walls

        
    def map_range(self,value, start1, stop1, start2, stop2):
        return (value - start1) / (stop1 - start1) * (stop2 - start2) + start2
  