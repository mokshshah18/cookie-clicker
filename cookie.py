# Importing pygame module
import pygame
 
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
 
# create the display surface object
# of specific dimension.
screen = pygame.display.set_mode((800, 800))
 
# Fill the scree with white color
screen.fill((255, 255, 255))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            bool_mokey_1 = True
            mouse_x, mouse_y = pygame.mouse.get_pos()
            msx,msy = mouse_x,mouse_y

    pygame.draw.circle(screen, (0,0,0), (400, 400), 100, 10)
    # Draws the surface object to the screen.
    pygame.display.update()