import pygame
import random
import math

# Initialize the pygame
pygame.init()

# create screen window
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('Images/background.png')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('Images/spaceship.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('Images/cade.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 30)

textX = 10
textY = 10

# Game Over text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def display_score(x, y):
    score = font.render("Score :" + str(score_value), True, (255,255, 255))
    screen.blit(score, (x,y))

def game_over_text():
    gama_over = over_font.render("GAME OVER", True, (255,255, 255))
    screen.blit(gama_over, (200,250))

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 7

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('Images/lien.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(20,60))
    enemyX_change.append(0.3)
    enemyY_change.append(30)

# Bullet
# Ready - Bullet loaded
# Fire - Bullet currently moving

bulletImg = pygame.image.load('Images/weapon.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = 'ready'

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Game Loop
# Close game window when close button is clicked
running = True
while running:

    # Set Screen Window background colour
    screen.fill((0, 0, 0))

    # Set Background Image
    screen.blit(background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key Stroke events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1
            if event.key == pygame.K_RIGHT:
                playerX_change = 1
            if event.key == pygame.K_UP:
                # Store the x_position of spaceship
                bulletX = playerX
                fire_bullet(bulletX, playerY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
                

    # Keeping spaceship within window boundaries
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    # Enemy movement
    # Keeping space invader within window boundaries
    for i in range(num_of_enemies):

        if enemyY[i] > 450:
            for j in range(num_of_enemies):
                enemyY[j] = 1000
            game_over_text()
            break 

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bullet_state = 'ready'
            bulletY = 480
            score_value += 1
            # print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    # Reset Bullet position for shooting
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    display_score(textX, textY)

    pygame.display.update()