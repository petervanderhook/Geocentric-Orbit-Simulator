from src.base_screen import Screen
from src.constants import WINDOW_Y, WINDOW_X
from src.orb import Orb
from src.orbit import Orbit
import pygame
from time import ctime, time

class GlowScreen(Screen):
    """Example class for a Pong game screen"""

    def __init__(self, *args, **kwargs):
        # Call the parent constructor
        super().__init__(*args, **kwargs)

        # Values to pass back/return

        # Create objects
        scale = 5
        orb_width = scale
        p = 72176400
        j = 1438500000
        self.time = time() - (time() - p)
        # 1/1440 = 1 minute, 1/48 = 30 minute, 1/24 = 1 hour, 1/2 = 12 hour, 1 = 24 hour
        # (1 / 0.5) = 48 hour, (1 / 0.1428571) = 7 days, (1 / 0.0333333333) = 30 days, ( 1 / 0.00273972602 ) = 365 days
        self.speed_index = [-0.00273972602, -0.0333333333, -0.1428571, -0.5, -1, -12, -24, -48, -1440, 1440, 48, 24, 12, 1, 0.5, 0.1428571, 0.0333333333, 0.00273972602]
        self.time_index = [-365, -30, -7, -2, -1, -.5, -0.0416666666, -0.0208333333333, -0.000694444444, 0.0006944444444, 0.0208333333333, 0.041666666666, 0.5, 1, 2, 7, 30, 365]
        self.legend_index = ["-1 Year per tick.", "-30 Days per tick", "-7 Days per tick", "-2 days per tick", "-1 day per tick", "-12 hours per tick", "-1 hour per tick", "-30 minutes per tick", "-1 minute per tick", "1 minute per tick", "30 minutes per tick", "1 hour per tick", "12 hours per tick", "24 hours per tick", "2 days per tick", "7 days per tick", "30 days per tick", "1 year per tick"]
        self.index_num = 13
        #vvvvvvvvvvvv 1/1 represents 1 day per tick.
        time_passing_per_tick = 1/self.speed_index[self.index_num]
        self.orbits = []
        self.orbs = []
        self.line = False
        self.candle = Orbit(16 * scale)
        self.white_orb = Orb((167, 167, 167), 180, orb_width, time_passing_per_tick, self.candle)
        self.center_orb = Orb((255, 255, 255), 0, 8, 0, Orbit(1))
        self.black_orbit = Orbit(24 * scale, self.white_orb)
        self.green_orbit = Orbit(32 * scale, self.white_orb)
        self.red_orbit = Orbit(40 * scale, self.white_orb)
        self.purple_orbit = Orbit(48 * scale, self.white_orb)
        self.yellow_orbit = Orbit(56 * scale, self.white_orb)
        self.cyan_orbit = Orbit(64 * scale, self.white_orb)
        self.blue_orbit = Orbit(72 * scale, self.white_orb)
        self.black_orb = Orb((93, 93, 93), 180, orb_width, time_passing_per_tick/.2, self.black_orbit)
        self.green_orb = Orb((70, 154, 70), 180, orb_width, time_passing_per_tick/.6, self.green_orbit)
        self.red_orb = Orb((182,117,117), 180, orb_width, time_passing_per_tick/1.9, self.red_orbit)
        self.purple_orb = Orb((150,109,173), 180, orb_width, time_passing_per_tick/11.9, self.purple_orbit)
        self.yellow_orb = Orb((169,155,96), 180, orb_width, time_passing_per_tick/29.5, self.yellow_orbit)
        self.cyan_orb = Orb((104,173,173), 180, orb_width, time_passing_per_tick/84, self.cyan_orbit)
        self.blue_orb = Orb((96,118,173), 180, orb_width, time_passing_per_tick/164.8, self.blue_orbit)
        self.orbs.append(self.white_orb)
        self.orbs.append(self.black_orb)
        self.orbs.append(self.green_orb)
        self.orbs.append(self.red_orb)
        self.orbs.append(self.purple_orb)
        self.orbs.append(self.yellow_orb)
        self.orbs.append(self.cyan_orb)
        self.orbs.append(self.blue_orb)
        self.orbits.append(self.candle)
        self.orbits.append(self.black_orbit)
        self.orbits.append(self.green_orbit)
        self.orbits.append(self.red_orbit)
        self.orbits.append(self.purple_orbit)
        self.orbits.append(self.yellow_orbit)
        self.orbits.append(self.cyan_orbit)
        self.orbits.append(self.blue_orbit)
        self.center_x = self.center_orb.pos[0]
        self.center_y = self.center_orb.pos[0]

        # Music and sounds
        #pygame.mixer.music.load("./sounds/music.wav")
        #pygame.mixer.music.play(-1)

        # Buttons, Background, Fonts


    def process_event(self, event):
        # In this screen, we don't have events to manage - pass
        pass
    def calc_line(self, orb):
        dx = orb.pos[0] - self.center_orb.pos[0] + 0.1
        dy = orb.pos[1] - self.center_orb.pos[1]

        rev_sign_x = 1 if dx < 0 else -1
        #rev_sign_y = 1 if dy < 0 else -1

        slope = dy/dx
        x_new = rev_sign_x * WINDOW_X
        y_new = orb.pos[1] + slope * (x_new - orb.pos[0])
        new_coord = [x_new, y_new]
        pygame.draw.line(self.window, (255, 255, 255), orb.pos, new_coord, 1)


    def update_orb_speed(self):
        time_passing_per_tick = 10/self.speed_index[self.index_num]
        self.white_orb.rotate_speed = time_passing_per_tick/1
        self.black_orb.rotate_speed = time_passing_per_tick/.2
        self.green_orb.rotate_speed = time_passing_per_tick/.6
        self.red_orb.rotate_speed = time_passing_per_tick/1.9
        self.purple_orb.rotate_speed = time_passing_per_tick/11.9
        self.yellow_orb.rotate_speed = time_passing_per_tick/29.5
        self.cyan_orb.rotate_speed =  time_passing_per_tick/84
        self.blue_orb.rotate_speed = time_passing_per_tick/164.8
        print(f"Remade orbs with 1 / {self.speed_index[self.index_num]}")
        
    def render_text(self):
        self.speedfont = pygame.font.Font('./src/roboto.ttf', int((WINDOW_X+WINDOW_Y)/40))
        self.tickfont = pygame.font.Font('./src/roboto.ttf', int((WINDOW_X+WINDOW_Y)/40))
        self.tick_text = self.tickfont.render(f"Ticks per second: {self.fps}", True, (255, 255, 255))
        self.speed_text = self.speedfont.render(self.legend_index[self.index_num], True, (255, 255, 255))
        self.time_text = self.speedfont.render(ctime(self.time), True, (255, 255, 255))
        self.window.blit(self.speed_text, (20, 100))
        self.window.blit(self.tick_text, (20, 50))
        self.window.blit(self.time_text, (20, 0))
    
    def update_time(self):
        self.time += (1440 * self.time_index[self.index_num])

    def process_loop(self):
        """Runs code every tick"""
        self.window.fill((0, 0, 0))
        self.update_time()
        print(ctime(self.time))
        # Update the positions
        self.render_text()
        if pygame.key.get_pressed()[pygame.K_o]:
            self.line = False
        if pygame.key.get_pressed()[pygame.K_l]:
            self.line = True
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            if (self.index_num > 0):
                self.index_num -= 1
                self.update_orb_speed()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            if (self.index_num < (len(self.speed_index) - 1)):
                self.index_num += 1
                self.update_orb_speed()
                
        # Draws images, buttons, and fonts
        for item in self.orbits:
            item.update(self.window)
        self.center_orb.update(self.window)
        for item in self.orbs:
            item.get_pos()
        if self.line:
            for item in self.orbs:
                self.calc_line(item)

        for item in self.orbs:
            item.draw_self(self.window)
        print(self.blue_orb.pos)

        



