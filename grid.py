import pygame as py 
from random import random as R
from random import randint 
from player import Player
from player import Obstacle 
py.mixer.init()

"""
GAME PLAN 

Lore: 
journey of a traveler from one kingdom to another to deliver a massege 

Elements:
- night/day 
- water fall sounds 
- vivaldi 
- backpack 
- optional tasks: picking flowers, pet animals 
- lanterns / light overall 
- time tracker 
- coins 

Characters: 
- Queen 
- Guard
- King 
- Goodbye Person ? 
- cat 
- bat 


Room ideas: 
1.  starting kingdom 
    a) introduction 
    b) meeting with the queen 
    c) message 
    d) pick outfit 
    e) TASK 1.1 saying farewell to ?
2.  outside city    (fields, sun)
    a) get out of tall grass 
    b) OPT 2.1 pet cat 
3.  forest I (sunset colour, few trees)
    a) TASK 3.1 find good tree to rest 
    b) TASK 3.2 water streem 
    c) OPT 3.1 
4.  forest II (night time, świetliki, darker music)
    a) more unsettling vibe 
    b) OPT 4.1 touching smt? and bats flying out 
5.  foreign city 
    a) exploring 
    b) stopped by guards 
    c) play game - ?? 
        if win = 
        1. if have flower   = can choose to give flower
        2. if no flower     = thank for game 
        if lose = pay with coins 
    d) deliver message 


"""

#generates for 0 to 1 floating point num 
#generate n X n grid on the screen 
#player only move within thse cells in the grid 
#https://minecraft.fandom.com/wiki/Category:Sound_effects

cell_w, cell_h = 60, 60       #9 cells 
row, col = 9, 9 
screen_w, screen_h = col * cell_w, row * cell_h 
panel_w = 3*cell_w

#generating random value of 0 & 1 in the grind list
#decides where we draw obstacles 
# probablilities to be 70 - 30 for obstacle 
# grid = [[1 if R()> 0.8 else 0 for i in range(col)] for j in range(row)]

grid = [[randint(0,4) for i in range(col)] for j in range(row)]
# 0,0 0,1, 1,0 

for r  in grid :
    print(r)

grid[0][0], grid[0][1], grid[1][0] = 1, 1, 1

sound = py.mixer.Sound("C:/Users/04Solec/PreDP2-MagdalenaK/Game/Creeper_death.oga")
char = py.image.load("C:/Users/04Solec/PreDP2-MagdalenaK/Game/charheart.svg.svg")
char = py.transform.scale(char, (60, 60))
bush = py.image.load("C:/Users/04Solec/PreDP2-MagdalenaK/PygameProject/Game/square.png")
bush = py.transform.scale(bush, (60, 60))
bg = py.image.load("C:\\Users\\04Solec\\PreDP2-MagdalenaK\\PygameProject\\Game\\background.png")
bg = py.transform.scale(bg, (screen_w, screen_h))
# soundEffect = py.mixer.music(" ADRES")
coin_sound = py.mixer.Sound("C:/Users/04Solec/PreDP2-MagdalenaK/Game/Pig_death.oga") #CHANGE

clock  = py.time.Clock()
py.init()
screen = py.display.set_mode((screen_w + panel_w, screen_h))
py.display.set_caption("Generating random grid")

p1 = Player(5, 5, 60, 60, char)       #moves by 60 (500 +5 +5)
obstacleList = []
for r in range(row):
    for c in range(col): 
        if grid[r][c] == 0:
            obstacleList.append(Obstacle(c*cell_w, r*cell_h, bush))     #add obstacle based on grid 

# Player.speedX = cell_w
# Player.speedY = cell_h
 

def drawGrid(grid: list[list]):
    index = 0   #num of obsticles
    for r in range(row):
         for c  in range(col):
            if grid[r][c] == 0: 
                # py.draw.rect(screen, "#000000", (cell_w*c, cell_h*r, cell_w, cell_h))
                obstacleList[index].draw(screen)
                index += 1
            elif grid[r][c] == 6:
                screen.blit("CHANGE") 
        
coin = 0 
def drawPanel(coin):
    font = py.font.SysFont(None, 30)    #font
    py.draw.rect(screen, "#F891BB", (screen_w, 0, panel_w, screen_h))
    textSurface = font.render(f"Coins: {coin}", True,"#ffffff")
    screen.blit(textSurface, (screen_w + 20, 40))

def find(coin):     #action based on value in grid when key pressed 
    r = p1.y // 60
    c = p1.x // 60
    if event.type == py.KEYDOWN: 
        if event.key == py.K_SPACE and grid[r][c] == 3:
            coin += 1   
            grid[r][c] = 6
            coin_sound.play()
    return coin
            

run = True 
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False 
        p1.move(screen, grid, event)
        coin = find(coin)
        sound.play()
    clock.tick(10)              #frame rate 
    # screen.fill("#ffffff")      #clear history 
    screen.blit(bg, (0,0))
    drawGrid(grid) 
    drawPanel(coin)
    p1.draw(screen)

    py.display.flip()
py.quit()