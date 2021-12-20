import pygame as pg
import sys

from pygame.version import PygameVersion

pg.init()

RED = (200,0,0)
GREEN = (0,200,0)
BLUE = (0,0,128)
BLACK = (0,0,0)
WHITE = (255,255,255)




#Initialization
mousex = 0
mousey = 0
#Instantiate Window
screenHeight = 800
screenWidth = 800
screen = pg.display.set_mode((screenWidth, screenHeight))
pg.display.set_caption("Tic Tac Toe")

pg.font.init

myfont = pg.font.SysFont("monospace", 12)
hud = myfont.render("Tic Tac Toe", 1, BLUE)
#blit the font on the screen at location 1, 1

board = [[0,0,0],[0,0,0],[0,0,0]]

#0's or 1's will determine x's or o's
#for loop for finding 0's and 1's within board
#if statement for each piece of information in board to print either x or o
#update screen

playing = True

while playing:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            mousex, mousey = pg.mouse.get_pos()
            print(mousex, mousey)
    
    screen.fill(WHITE)
    screen.blit(hud, ((screenWidth/2) - 20, 10))

    pg.draw.line(screen, RED, (0, screenHeight/3),(screenWidth, screenHeight/3), 5)
    pg.draw.line(screen, RED, (0, screenHeight*(2/3)),(screenWidth, screenHeight*(2/3)), 5)
    pg.draw.line(screen, RED, (screenWidth/3, 0),(screenWidth/3, screenHeight), 5)
    pg.draw.line(screen, RED, (screenWidth*(2/3), 0),(screenWidth*(2/3), screenHeight), 5)

    #if player 1 (not specified) clicks within certain area, two lines are drawn to form an X.


    if (mousex < screenWidth/3) and (mousey < screenHeight/3):
        
        #pg.draw.line(screen, BLUE, (screenWidth*(3/99), screenHeight*(3/99)), (screenWidth*(30/99), screenHeight*(30/99)), 5)
    #if player 2 (not specified) clicks within certain area, circle is drawn.
    #Sizes of lines and circles shouldn't intersect with board lines.

    pg.display.update()


#While loop for gameplay
#copy + paste mouseclicks from snake game
#

#Setup player 1 gameplay
#Setup player 2 gameplay
#evaluate "win"
#evaluate "loss"
#evaluate "tie"

"""---Ideas---
Player vs Player
Player vs AI
AI vs AI
Difficulty Levels (easy, normal, hard, impossible)
Player Profiles (logging wins, losses, ties, win%, win streak, total games played)
Customization between X or O"""
