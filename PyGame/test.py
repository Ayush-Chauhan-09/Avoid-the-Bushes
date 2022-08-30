import pygame
import random
import math

from pygame import mixer
# initializing the pygame
pygame.init()
# screen
screen = pygame.display.set_mode((800,600)) 

#background sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Car Crash")
icon = pygame.image.load('car.png')
pygame.display.set_icon(icon)
back = pygame.image.load('back.png')

#score
ex = 0
score = 0
font = pygame.font.Font('freesansbold.ttf', 36)
fl = pygame.font.Font('freesansbold.ttf', 18)
game = pygame.font.Font('freesansbold.ttf', 64)
level = 'Level 1'

def show_score():
    t = font.render("CAR CRASH", True, (250, 91, 61))
    s=font.render("Score:" + str(score), True,(255,215,0))
    l = fl.render(level, True, (0, 100, 0))
    text_r = l.get_rect(center=(400, 125))
    text_rect = s.get_rect(center=(800/2, 75))
    text_rec = t.get_rect(center=(800/2, 20))
    screen.blit(s, text_rect)
    screen.blit(t, text_rec)
    screen.blit(l, text_r)

def game_over():
    
    g = game.render("Game Over", True, (250, 91, 61))
    text_end = g.get_rect(center=(400, 300))
    screen.blit(g, text_end)




# player
playerImg = pygame.image.load('car.png')
playerX = 100
playerY = 265
playerX_change = 0
playerY_change = 0
speed = 3
bushspeed = 3.5

bushImg = pygame.image.load('bush.png')
#bush1
bush1X = 785
bush1Y = random.randint(150,286)

#bush2
bush2X = 1085
bush2Y = random.randint(276,412)

#bush3
bush3X = 1385
bush3Y = random.randint(402,536)



def player(x,y):
    screen.blit(playerImg,(x,y))


def bush1(x, y):
    screen.blit(bushImg, (x,y))

def bush2(x, y):
    screen.blit(bushImg, (x,y))

def bush3(x, y):
    screen.blit(bushImg, (x,y))


def collision(bush1X,bush1Y,bush2X,bush2Y,bush3X,bush3Y,playerX,playerY):
    distance1 = math.sqrt((math.pow(bush1X-playerX,2) + math.pow(bush1Y-playerY,2)))
    distance2 = math.sqrt((math.pow(bush2X-playerX,2) + math.pow(bush2Y-playerY,2)))
    distance3 = math.sqrt((math.pow(bush3X-playerX,2) + math.pow(bush3Y-playerY,2)))

    if distance1 < 35 or distance2 < 35 or distance3 < 35:
        return True
    else:
        return False

# Game loop
running = True
while running:
    # Background
    screen.fill((128, 128, 128))
    screen.blit(back,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -(speed)

            if event.key == pygame.K_RIGHT:
                playerX_change = speed

            if event.key == pygame.K_UP:
                playerY_change = -(speed)

            if event.key == pygame.K_DOWN:
                playerY_change = speed
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
    
    #collision
    c = collision(bush1X,bush1Y,bush2X,bush2Y,bush3X,bush3Y,playerX,playerY)
    if c:
        crash = mixer.Sound('crash.wav')
        crash.play()
        #score = 0
        #running = False
        bush1X = 800000000
        bush2X = 800000000
        bush3X = 800000000
        playerX = 15
        playerY = 270
        ex = 1
        bushspeed = 0
        pygame.mixer.music.stop()


    if score <= 100:
        level = 'Level 1'
    elif score > 100 and score <= 250:
        bushspeed = 5
        level = 'Level 2'
    elif score > 250 and score <= 450:
        bushspeed = 7
        level = 'Level 3'
    elif score > 450 and score <= 600:
        bushspeed = 9
        level = 'Level 4'
    elif score > 600:
        bushspeed = 13
        level = 'Level 5'
    bush1X -= bushspeed
    bush2X -= bushspeed
    bush3X -= bushspeed

    playerX += playerX_change
    if playerX <=10:
        playerX = 10
    elif playerX >= 726:
        playerX = 726

    playerY += playerY_change
    if playerY <= 150:
        playerY = 150
    elif playerY >= 530:
        playerY = 530

    if bush1X < -35:
        score += 10
        bush1X = 785
        bush1Y = random.randint(150,276)        
    if bush2X < -35:
        score += 10
        bush2X = 785
        bush2Y = random.randint(276, 402)        
    if bush3X < -35:
        score += 10
        bush3X = 785
        bush3Y = random.randint(402, 536)       

    player(playerX,playerY)
    bush1(bush1X,bush1Y)
    bush2(bush2X, bush2Y)
    bush3(bush3X, bush3Y)


    show_score()
    if ex == 1:
        game_over()
    pygame.display.update() 