import pygame
import math
import sys

#pygame initilization first
pygame.init()

red = (200,0,0)
white = (255,255,255)
green = (0,200,0)
blue = (0,0,128)
black = (0,0,0)

#screen or window size
ScreenHeight = 400
ScreenWidth = 400
screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))

#loading an image
#carimp=pygame.image.load("RedCar.jpg")
#car1=pygame.transform.scale(carimp,(50,50))

#pygame window name
pygame.display.set_caption("Pygame Testing")

#pygame fonts
pygame.font.init
myfont = pygame.font.SysFont("monospace", 12)
hud = myfont.render("Speed: ", 1, red)
#blit the font on the screen at location 1, 1
screen.blit(hud, (1, 1))

pygame.display.update()

#set the clock
clock=pygame.time.Clock()
velX = 0
velY = 0
done = False
posx = ScreenWidth / 2
posy = ScreenHeight / 2
radius = 75


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
            if event.key == pygame.K_UP:
                velY = velY - .1
            if event.key == pygame.K_DOWN:
                velY = velY + .1
            if event.key == pygame.K_RIGHT:
                velX = velX + .1
            if event.key == pygame.K_LEFT:
                velX = velX - .1
            if event.key == pygame.K_q:
                done = True
    
    #fill the screen with a color
    screen.fill(white)
    posx = posx + velX
    posy = posy + velY
    pygame.draw.circle(screen, blue, (posx, posy), radius, 5)
    

    #rework what is on the screen blit, etc.
    #refresh the screen
    pygame.display.update()
    
sys.exit()