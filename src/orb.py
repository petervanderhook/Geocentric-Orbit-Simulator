import math
from src.constants import RADIAN
import pygame
class Orb():

    def __init__(self, color, angle, radius, rotation_speed, orbit):
        #self.img
        #self.default rgb values
        #Tolerance of 15 for each R, G, and B
        #self.state
        self.color = color
        self.angle = angle
        self.radius = radius
        self.rotate_speed = rotation_speed
        self.orbit_trail = orbit
        if self.orbit_trail.parent_orb != None:
            self.orbit_center_x_axis = self.orbit_trail.parent_orb.pos[0]
            self.orbit_center_y_axis = self.orbit_trail.parent_orb.pos[1]
        else:
            self.orbit_center_x_axis = self.orbit_trail.pos[0]
            self.orbit_center_y_axis = self.orbit_trail.pos[1]
        self.get_pos()

    def get_pos(self):
        if self.orbit_trail.parent_orb != None:
            self.orbit_center_x_axis = self.orbit_trail.parent_orb.pos[0]
            self.orbit_center_y_axis = self.orbit_trail.parent_orb.pos[1]
        else:
            self.orbit_center_x_axis = self.orbit_trail.pos[0]
            self.orbit_center_y_axis = self.orbit_trail.pos[1]
        pos_valx = math.floor(self.orbit_center_x_axis + (math.sin(self.angle * RADIAN) * self.orbit_trail.radius))
        pos_valy = math.floor(self.orbit_center_y_axis + (math.cos(self.angle * RADIAN) * self.orbit_trail.radius))
        # Subtract angle - Rotation Speed
        self.pos = [pos_valx, pos_valy]
        self.angle -= self.rotate_speed


    def draw_self(self, window):
        pygame.draw.circle(window, self.color, self.pos, self.radius)

    def update(self, window):
        self.get_pos()
        self.draw_self(window)
