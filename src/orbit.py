from src.constants import WINDOW_X, WINDOW_Y
import pygame
from src.orb import Orb
class Orbit():
    
    def __init__(self, radius, parent_orb=None):
        self.color = (255, 255, 255)
        self.radius = radius
        if parent_orb != None:
            self.has_parent = True
            self.parent_orb = parent_orb
            self.pos = self.parent_orb.pos
        else:
            self.parent_orb = None
            self.has_parent = False
            pos_x = round(WINDOW_X/2)
            pos_y = round(WINDOW_Y/2)
            self.pos = [pos_x, pos_y]
        #[100, 0, 90], #Radius, Rotation Speed, Spawn Angle

    def get_pos(self):
        if self.has_parent:
            return self.parent_orb.pos
        return self.pos
    
    def draw_self(self, window, render_trail=False):
        if self.has_parent:
            if render_trail:
                pygame.draw.circle(window, (93,93,93), self.pos, self.radius, 1)
            pass
        else:
            pygame.draw.circle(window, (93,93,93), self.pos, self.radius, 1)
            pass

    def update(self, window, render_trail=False):
        self.pos = self.get_pos()
        self.draw_self(window, render_trail)