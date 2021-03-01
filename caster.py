import utils.entity as e
from pygame.math import Vector2
import math
from ray import Ray
from functools import reduce



class Caster(e.Entity):
    def __init__(self, position, ray_count, mass=5):
        super().__init__(position, mass=mass)
        self.ray_count = ray_count
        self.rays = []

    def set_position(self,new_position):
        self.position = new_position
    
    def update_position(self,x,y):
        self.position.x = self.position.x+x
        self.position.y = self.position.y+y
        
    def edges(self, s_width, s_height):
        return super().edges(s_width, s_height)

    def draw(self, screen, color,walls):
        self.__create_rays()

        '''
        for wall in walls:
            for ray in self.rays:
                p = ray.intersects(wall)
                if(p!=None):
                    ray.set_head(p)
                    ray.draw(screen,color)

                wall.draw(screen,color)
        #print(len(self.rays))
        '''
        for ray in self.rays:
            p = self.__get_closest_intersection(ray,walls)
            for wall in walls:
                wall.draw(screen,color)
            if(p!= None):
                ray.set_head(p)
            ray.draw(screen,color)
    

    def __get_closest_intersection(self,ray,walls):

        def calculate(wall):
            res = None
            point = ray.intersects(wall)
            if(point!=None):
                temp = point - ray.p1
                res = (point,temp.magnitude())
            return res

        def get_closest(a,b):
            if a==None and b == None:
                return None
            elif a == None:
                return b
            elif b == None:
                return a
            elif(a[1]<=b[1]):
                return a
            else:
                return b


        points = map(calculate,walls)
        closest = reduce(get_closest,points)

        return closest[0] if closest!= None else None

    def __create_rays(self):
        rays = []
        origin = Vector2(self.position.x,self.position.y)
        increment = 360/self.ray_count
        angle = 0
        while angle<360:
            radians = math.radians(angle)
            head = Vector2(math.cos(radians)*10,math.sin(radians)*10) + self.position
            ray = Ray(origin,head,1)
            rays.append(ray)
            angle = angle + increment
        self.rays = rays

    
 
