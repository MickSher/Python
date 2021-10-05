import pygame
import math
import sys
import random

#pygame initilization first
pygame.init()

red = (200,0,0)
white = (255,255,255)
green = (0,200,0)
blue = (0,0,128)
black = (0,0,0)

#screen or window size
ScreenHeight = 800
ScreenWidth = 800
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

#loading an image
#carimp=pygame.image.load("RedCar.jpg")
#car1=pygame.transform.scale(carimp,(50,50))

#pygame window name
pygame.display.set_caption("Snake Game")

#pygame fonts
pygame.font.init
myfont = pygame.font.SysFont("monospace", 12)
hud = myfont.render("Speed: ", 1, red)
#blit the font on the screen at location 1, 1
screen.blit(hud, (1, 1))

pygame.display.update()
#set the clock
clock=pygame.time.Clock()
radius = 5
snakeSpeed = 1
velX = 1
velY = 0
done = False
posx = ScreenWidth / 2
posy = ScreenHeight / 2
x = ScreenWidth / 2
y = ScreenHeight / 2

#tail positioning
tailX = []
tailY = []

#functions
def show():
    pass
def sUpdate(x, y, appleX, appleY):
    snake = pygame.draw.rect(screen, blue, (x, y, 10, 5), 3)
    apple = pygame.draw.circle(screen, red, (appleX, appleY), radius, 0)
    return(x, y, appleX, appleY)

def death(tailX, tailY, x, y):
    if (x > ScreenWidth - 1) or (x < 1) or (y > ScreenHeight - 1) or (y < 1):
        tailX = []
        tailY = []
        x = ScreenWidth / 2
        y = ScreenHeight / 2
        print("Snake reset.")
    return(tailX, tailY, x, y)

def spawnapple():
    appleX = random.randint(20, 380)
    appleY = random.randint(20, 380)
    return appleX, appleY

appleX, appleY = spawnapple()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION:
            posx = event.pos[0]
            print("mouse pos x", posx)
            posy = event.pos[1]
            print("mouse pos x", posx)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("click")
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                velY = snakeSpeed*-1
                velX = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                velY = snakeSpeed
                velX = 0
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                velX = snakeSpeed*1
                velY = 0
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                velX = snakeSpeed*-1
                velY = 0
            if event.key == pygame.K_q:
                done = True
    
    #fill the screen with a color
    screen.fill(white)
    x = x + velX
    y = y + velY
    snake = pygame.draw.rect(screen, blue, (x, y, 10, 5), 3)
    snakeHead = pygame.draw.rect(screen, blue, (x, y, 10, 5), 3)
    apple = pygame.draw.circle(screen, red, (appleX, appleY), radius, 0)

    if (abs(x - appleX) < 10) and (abs(y - appleY) < 10):
        appleX = 0
        #Add a segment to the snake

    #snake interaction with apple
    if appleX == 0:
        appleX, appleY = spawnapple()
    tailX, tailY, x, y = death(tailX, tailY, x, y)
    x, y, appleX, appleY = sUpdate(x, y, appleX, appleY)

    #show(x, y)

    
    
    

    #rework what is on the screen blit, etc.
    #refresh the screen
    pygame.display.update()
    clock.tick(60)

sys.exit()