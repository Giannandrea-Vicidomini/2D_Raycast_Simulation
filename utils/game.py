import abc
import pygame
import datetime

class GameFramework(abc.ABC):
    def __init__(self,size,title):
        self.screen_width = size[0]
        self.screen_height = size[1]
        self.screen = pygame.display.set_mode(size)
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.t_elapsed = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.title = title
    
    def start(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        self.on_create()

        start = self.__get_time_milliseconds()
        
        while self.running:
            mouse_pos = pygame.mouse.get_pos()
            self.mouse_x = mouse_pos[0]
            self.mouse_y = mouse_pos[1]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    self.on_mouse_down(self.mouse_x,self.mouse_y)
                if event.type == pygame.MOUSEBUTTONUP:
                    
                    self.on_mouse_up(self.mouse_x,self.mouse_y)

                if pygame.mouse.get_pressed()[0]:

                    self.on_mouse_hold(self.mouse_x,self.mouse_y)

                self.on_event(event)

            self.t_elapsed = self.__get_time_milliseconds() - start
            delta_time = self.clock.tick(self.fps)/1000.0
            self.on_update(self.screen,delta_time,self.t_elapsed)

            
            pygame.display.update()
        
        pygame.quit()

    def on_create(self):
        pass

   
    def on_event(self,event):
        pass

    def on_mouse_down(self,pos_x,pos_y):
        pass
    def on_mouse_up(self,pos_x,pos_y):
        pass

    def on_mouse_hold(self,pos_x,pos_y):
        pass

    @abc.abstractmethod
    def on_update(self,screen,delta_time,time):
        raise NotImplementedError

    def __get_time_milliseconds(self):
        return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000)
