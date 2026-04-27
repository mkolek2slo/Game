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
3. ... 

PROBLEMS 
1. printing queen in one place 
"""
import pygame as py 
from random import random as R
from random import randint 
from player import Player
from player import Obstacle
from characters import Human 
py.mixer.init()


cell_w, cell_h = 60, 60       #9 cells 
row, col = 9, 9 
screen_w, screen_h = col * cell_w, row * cell_h 
panel_w = 3*cell_w

grid = [[randint(0,4) for i in range(col)] for j in range(row)]
# 0,0 0,1, 1,0 


sound = py.mixer.Sound("C:/Users/04Solec/PreDP2-MagdalenaK/Game/Creeper_death.oga")
char = py.image.load("C:/Users/04Solec/PreDP2-MagdalenaK/Game/charheart.svg.svg")
char = py.transform.scale(char, (60, 60))
bg = py.image.load("C:/Users/04Solec/PreDP2-MagdalenaK/PygameProject/Game/background.png")
bg = py.transform.scale(bg, (screen_w, screen_h))
# soundEffect = py.mixer.music(" ADRES")
# coin_sound = py.mixer.Sound("C:/Users/04Solec/PreDP2-MagdalenaK/Game/Pig_death.oga") #CHANGE
queen = py.image.load("C:/Users/04Solec/PreDP2-MagdalenaK/PygameProject/Game/Question-Mark-Fractal.svg")
queen = py.transform.scale(queen, (60,60))


clock  = py.time.Clock()
py.init()
screen = py.display.set_mode((screen_w + panel_w, screen_h))
py.display.set_caption("Generating random grid")

p1 = Player(5, 5, 60, 60, char)       
p2 = Human(5, 5, 60, 60, queen)
# Player.speedX = cell_w
# Player.speedY = cell_h
 
       

def drawPanel():
    font = py.font.SysFont(None, 30)  
    py.draw.rect(screen, "#F891BB", (screen_w, 0, panel_w, screen_h))
    textSurface = font.render(f"BACKPACK", True,"#ffffff")
    screen.blit(textSurface, (screen_w + 20, 40))


#INFORMATION 

# Inicjalizacja
font = py.font.SysFont('Arial', 24)
active_message = None  # Tu przechowujemy tekst, gdy gracz coś aktywuje
info_tile = (2, 2)     # Pole z wiadomością

        
if event.type == py.KEYDOWN:
    # 1. Jeśli wiadomość jest wyświetlana, dowolny klawisz ją zamyka
    if active_message:
                active_message = None
    else:
        # 2. Jeśli nie ma wiadomości, pozwalamy na ruch
         # 3. Sprawdź czy po ruchu gracz wszedł na pole z informacją
        if (p1.x, p1.y) == info_tile:
            active_message = "Znalazles stara mape! [Nacisnij klawisz]"
    

# cell_w, cell_h = 60, 60       #9 cells 
# row, col = 9, 9 
# screen_w, screen_h = col * cell_w, row * cell_h 
# panel_w = 3*cell_w
    # Rysujemy siatkę i cel
    py.draw.rect(screen, (200, 255, 200), (info_tile[0]*cell_h, info_tile[1]*cell_h, 9, 9))

    # WYŚWIETLANIE OKNA WIADOMOŚCI
    if active_message:
        # Tło okienka (overlay)
        overlay = py.Surface((300, 100))
        overlay.fill((50, 50, 50))
        text_surf = font.render(active_message, True, (255, 255, 255))
        
        screen.blit(overlay, (180, 180))
        screen.blit(text_surf, (180, 180))


            

run = True 
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False 
        p1.move(screen, grid, event)
    clock.tick(10)              #frame rate 
    # screen.fill("#ffffff")      #clear history 
    screen.blit(bg, (0,0))
    drawPanel()
    p1.draw(screen)
    # p2.draw(screen)
    screen.blit(queen, (9,5)) #????

    py.display.flip()
py.quit()

