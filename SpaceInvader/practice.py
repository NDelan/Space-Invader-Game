import pygame

# Initialize the pygame
pygame.init()

# create screen window
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('Images\spaceship.png')
pygame.display.set_icon(icon)

# Game Loop
# Close game window when close button is clicked
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False