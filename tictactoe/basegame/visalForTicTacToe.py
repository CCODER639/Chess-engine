# Importing pygame module
import pygame
from pygame.locals import *

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((750, 750))

# Fill the scree with white color
window.fill((255, 255, 255))

# Using draw.rect module of
# pygame to draw the solid rectangle
pygame.draw.rect(window, (0,   0, 255),
                 [0, 0, 250, 250], 0)

pygame.draw.rect(window, (0,   0, 0),
                 [250, 0, 250, 250], 0)

pygame.draw.rect(window, (0,   0, 255),
                 [500, 0, 250, 250], 0)

pygame.draw.rect(window, (0,   0, 0),
                 [0, 250, 250, 250], 0)

pygame.draw.rect(window, (0,   0, 255),
                 [250, 250, 250, 250], 0)
pygame.draw.rect(window, (0,   0, 0),
                 [500, 250, 250, 250], 0)
pygame.draw.rect(window, (0,   0, 255),
                 [0, 500, 250, 250], 0)
pygame.draw.rect(window, (0,   0, 0),
                 [250, 500, 250, 250], 0)
pygame.draw.rect(window, (0,   0, 255),
                 [500, 500, 250, 250], 0)

# Draws the surface object to the screen.
pygame.display.update()


running = True
while running:
    
    # Check for event if user has pushed
    # any event in queue
    for event in pygame.event.get():
        
        # if event is of type quit then 
        # set running bool to false
        if event.type == pygame.QUIT:
            running = False