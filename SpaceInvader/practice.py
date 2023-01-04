import pygame
import random

# Initialize the pygame
pygame.init()

# create screen window
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('Images\spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Images\cade.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Enemy
enemyImg = pygame.image.load('Images\lien.png')
enemyX = random.randint(0,800)
enemyY = random.randint(20,60)
enemyX_change = 0
enemyY_change = 0

def player(x, y):
    screen.blit(playerImg, (playerX, playerY))

def enemy(x, y):
    screen.blit(enemyImg, (enemyX, enemyY))

# Game Loop
# Close game window when close button is clicked
running = True
while running:

    # Set Screen Window background colour
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key Stroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()