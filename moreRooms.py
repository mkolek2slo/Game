import pygame as py 
from random import random as R
from random import randint 
from player import Player
from player import Obstacle
from characters import Human 

import pygame as py 
from random import random as R
from random import randint 
from player import Player
from player import Obstacle
from characters import Human 

py.init()
py.mixer.init()

cell_w, cell_h = 60, 60
row, col = 9, 9 
screen_w, screen_h = col * cell_w, row * cell_h 
panel_w = 3 * cell_w

grid = [[randint(0,4) for i in range(col)] for j in range(row)]

sound = py.mixer.Sound("C:/Users/04Solec/PreDP2-MagdalenaK/Game/Creeper_death.oga")

char = py.image.load("C:/Users/04Solec/PreDP2-MagdalenaK/Game/charheart.svg.svg")
char = py.transform.scale(char, (60, 60))

bg = py.image.load("C:\\Users\\04Solec\\PreDP2-MagdalenaK\\PygameProject\\Game\\white_bg.jpg")
bg = py.transform.scale(bg, (screen_w, screen_h))

queen = py.image.load("C:/Users/04Solec/PreDP2-MagdalenaK/PygameProject/Game/Question-Mark-Fractal.svg")
queen = py.transform.scale(queen, (60,60))

clock  = py.time.Clock()
screen = py.display.set_mode((screen_w + panel_w, screen_h))
py.display.set_caption("Generating random grid")

p1 = Player(0, 0, 60, 60, char)       
p2 = Human(8, 4, cell_w, cell_h, queen)

def is_next_to(p1, target):
    return abs(p1.x - target[0]) + abs(p1.y - target[1]) == 1


def drawPanel():
    font = py.font.SysFont(None, 30)  
    py.draw.rect(screen, "#F891BB", (screen_w, 0, panel_w, screen_h))

    screen.blit(font.render("BACKPACK", True, "#ffffff"), (screen_w + 20, 40))

    if outfit_state == "choosing":
        options = ["A", "B", "C"]
        y = 100

        for i, opt in enumerate(options):
            color = (0,255,0) if selected_outfit == i else (255,255,255)
            screen.blit(font.render(f"Outfit {opt}", True, color), (screen_w + 20, y))
            y += 40


font = py.font.SysFont('Arial', 24)

game_state = "kingdom"

cat_pos = (6, 6)
grass_zone = (3, 2, 3, 4)

active_message = None

messages = [
    "Queen: Welcome, traveler.",
    "Our kingdom is in danger.",
    "You must begin your journey."
]

message_index = 0

outfit_state = "locked"
selected_outfit = None

run = True 
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False 

        if event.type == py.KEYDOWN:

            # ---------------- OUTFIT SELECTION ----------------
            if outfit_state == "choosing":

                if event.key == py.K_a:
                    selected_outfit = 0
                elif event.key == py.K_b:
                    selected_outfit = 1
                elif event.key == py.K_c:
                    selected_outfit = 2
                elif event.key == py.K_RETURN and selected_outfit is not None:
                    outfit_state = "done"

            # ---------------- KINGDOM ----------------
            if game_state == "kingdom":

                if event.key == py.K_SPACE:

                    if active_message is None and is_next_to(p1, (p2.x, p2.y)):
                        active_message = messages[0]
                        message_index = 0

                    elif active_message is not None:
                        message_index += 1

                        if message_index < len(messages):
                            active_message = messages[message_index]
                        else:
                            active_message = None
                            message_index = 0
                            outfit_state = "choosing"

                # MOVEMENT (FIXED)
                elif active_message is None and outfit_state != "choosing":

                    next_x, next_y = p1.x, p1.y

                    if event.key == py.K_UP:
                        next_y -= 1
                    elif event.key == py.K_DOWN:
                        next_y += 1
                    elif event.key == py.K_LEFT:
                        next_x -= 1
                    elif event.key == py.K_RIGHT:
                        next_x += 1

                    if 0 <= next_x < col and 0 <= next_y < row:
                        if (next_x, next_y) != (p2.x, p2.y):
                            p1.x, p1.y = next_x, next_y

            # ---------------- FIELDS ----------------
            elif game_state == "fields":

                next_x, next_y = p1.x, p1.y

                if event.key == py.K_UP:
                    next_y -= 1
                elif event.key == py.K_DOWN:
                    next_y += 1
                elif event.key == py.K_LEFT:
                    next_x -= 1
                elif event.key == py.K_RIGHT:
                    next_x += 1

                if 0 <= next_x < col and 0 <= next_y < row:

                    gx, gy, gw, gh = grass_zone

                    if not (gx <= next_x < gx+gw and gy <= next_y < gy+gh):
                        p1.x, p1.y = next_x, next_y


    # ---------------- TRANSITIONS ----------------
    if game_state == "fields":
        if p1.y == 0:
            game_state = "forest1"
            p1.x, p1.y = 4, 8

    elif game_state == "forest1":
        if p1.y == 0:
            game_state = "forest2"
            p1.x, p1.y = 4, 8

    elif game_state == "forest2":
        if p1.y == 0:
            game_state = "city"
            p1.x, p1.y = 4, 8


    # ---------------- DRAW ----------------
    clock.tick(10)
    screen.blit(bg, (0,0))
    drawPanel()

    if game_state == "kingdom":
        screen.blit(char, (p1.x * cell_w, p1.y * cell_h))
        screen.blit(queen, (p2.x * cell_w, p2.y * cell_h))

    elif game_state == "fields":
        screen.fill((120, 200, 120))

        gx, gy, gw, gh = grass_zone
        py.draw.rect(screen, (80, 180, 80),
                     (gx*cell_w, gy*cell_h, gw*cell_w, gh*cell_h))

        py.draw.rect(screen, (200, 200, 200),
                     (cat_pos[0]*cell_w, cat_pos[1]*cell_h, cell_w, cell_h))

        screen.blit(char, (p1.x * cell_w, p1.y * cell_h))

    elif game_state == "forest1":
        screen.fill((70, 140, 70))
        screen.blit(char, (p1.x * cell_w, p1.y * cell_h))

    elif game_state == "forest2":
        screen.fill((40, 70, 40))
        screen.blit(char, (p1.x * cell_w, p1.y * cell_h))

    elif game_state == "city":
        screen.fill((180, 180, 200))
        screen.blit(char, (p1.x * cell_w, p1.y * cell_h))


    # ---------------- POPUP ----------------
    if active_message:
        popup_w = 400
        popup_h = 120

        popup_x = (screen_w - popup_w) // 2
        popup_y = (screen_h - popup_h) // 2

        overlay = py.Surface((popup_w, popup_h))
        overlay.fill((40, 40, 40))

        py.draw.rect(overlay, (255,255,255), (0,0,popup_w,popup_h), 3)

        text_surf = font.render(active_message, True, (255,255,255))

        screen.blit(overlay, (popup_x, popup_y))
        screen.blit(text_surf, (popup_x + 20, popup_y + 45))

    py.display.flip()

py.quit()