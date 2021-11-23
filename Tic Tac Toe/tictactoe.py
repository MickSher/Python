import pygame as pg
import sys

from pygame.version import PygameVersion

pg.init()

RED = (200,0,0)
GREEN = (0,200,0)
BLUE = (0,0,128)
BLACK = (0,0,0)
WHITE = (255,255,255)





#Instantiate Window
screenHeight = 800
screenWidth = 800
screen = pg.display.set_mode((screenWidth, screenHeight))
pg.display.set_caption("Tic Tac Toe")

pg.font.init

myfont = pg.font.SysFont("monospace", 12)
hud = myfont.render("Tic Tac Toe", 1, BLUE)
#blit the font on the screen at location 1, 1




playing = True

while playing:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            mousex, mousey = pg.mouse.get_pos()
        
        
    screen.fill(WHITE)
    screen.blit(hud, ((screenWidth/2) - 20, 10))
    pg.display.update()




#While loop for gameplay
#copy + paste mouseclicks from snake game
#

#Setup player 1 gameplay
#Setup player 2 gameplay
#evaluate "win"
#evaluate "loss"
#evaluate "tie"

"""---Order of Ideas---
Player vs Player
Player vs AI
AI vs AI
Difficulty Levels (easy, normal, hard, impossible)
Player Profiles (logging wins, losses, ties, win%, win streak, total games played)"""