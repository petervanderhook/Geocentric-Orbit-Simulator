import pygame, math
pygame.init()

bg = (0, 0, 0)
self_color = (240, 240, 240)

orbit_start_pos = [500, 500]

orbits= [ 
    [100, 0, 0], #Radius, Rotation Speed, Spawn Angle
    [50, 1, 180], #Radius, Rotation Speed, Spawn Angle
    [10, 1, 90]  #Radius, Rotation Speed, Spawn Angle
]
position = [0, 0]
positions = []


size = [1000, 1000]

screen = pygame.display.set_mode(size)
screen.fill(bg)
pygame.display.set_caption("Aberoth Glows")

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    screen.fill(bg)
    for i in range(0, len(orbits)):
        if i > 0:
            radian = 0.0174532925
            self_orbit_radius = orbits[i - 1][0]
            self_angle = orbits[i][2]
            orbit_center_x_axis = positions[len(positions) - 1][0]
            orbit_center_y_axis = positions[len(positions) - 1][1]
            pos_valx = math.floor(orbit_center_x_axis + (math.sin(self_angle * radian) * self_orbit_radius))
            pos_valy = math.floor(orbit_center_y_axis + (math.cos(self_angle * radian) * self_orbit_radius))
            self_position = [pos_valx, pos_valy]
            print(self_position)
        
        else:
            self_position = orbit_start_pos
        self_radius = orbits[i][0]
        pygame.draw.circle(screen, self_color, self_position, self_radius, 1)  # width of line in px, no parameter = filled circle
        # Subtract to move CW, Add to move CCW
        # Subtract angle - Rotation Speed
        orbits[i][2] -= orbits[i][1]

        positions.append(self_position)
    
    positions = []
    pygame.display.update()
    clock.tick(30)
