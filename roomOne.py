"""
First room of game
opening image

1.  starting kingdom 
    a) introduction 
    b) meeting with the queen 
    c) message 
    d) pick outfit 
    e) TASK 1.1 saying farewell to ?

point: 
1. explain game
2. pick character 
3. 
"""

import pygame as py 
from random import random as R
from random import randint 
from player import Player
from player import Obstacle 
py.mixer.init()


cell_w, cell_h = 60, 60       #9 cells 
row, col = 9, 9 
screen_w, screen_h = col * cell_w, row * cell_h 
panel_w = 3*cell_w

grid = [[randint(0,4) for i in range(col)] for j in range(row)]
# 0,0 0,1, 1,0 

for r  in grid :
    print(r)

grid[0][0], grid[0][1], grid[1][0] = 1, 1, 1

sound = py.mixer.Sound("C:/Users/04Solec/PreDP2-MagdalenaK/Game/Creeper_death.oga")
char = py.image.load("C:/Users/04Solec/PreDP2-MagdalenaK/Game/charheart.svg.svg")
char = py.transform.scale(char, (60, 60))
bush = py.image.load("./Game/square.png")
bush = py.transform.scale(bush, (60, 60))
bg = py.image.load("./Game/background.png")
bg = py.transform.scale(bg, (screen_w, screen_h))
# soundEffect = py.mixer.music(" ADRES")
coin_sound = py.mixer.Sound("C:/Users/04Solec/PreDP2-MagdalenaK/Game/Pig_death.oga") #CHANGE

clock  = py.time.Clock()
py.init()
screen = py.display.set_mode((screen_w + panel_w, screen_h))
py.display.set_caption("Generating random grid")

p1 = Player(5, 5, 60, 60, char)       #moves by 60 (500 +5 +5)

# Player.speedX = cell_w
# Player.speedY = cell_h
 

       
coin = 0 
def drawPanel(coin):
    font = py.font.SysFont(None, 30)    #font
    py.draw.rect(screen, "#F891BB", (screen_w, 0, panel_w, screen_h))
    textSurface = font.render(f"BACKPACK", True,"#ffffff")
    screen.blit(textSurface, (screen_w + 20, 40))

            

run = True 
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False 
        p1.move(screen, grid, event)
    clock.tick(10)              #frame rate 
    # screen.fill("#ffffff")      #clear history 
    screen.blit(bg, (0,0))
    drawPanel(coin)
    p1.draw(screen)

    py.display.flip()
py.quit()

