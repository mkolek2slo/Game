import pygame as py 
from random import random as R
from random import randint 
from player import Player
from player import Obstacle
from characters import Human 

import os                                                       #???
os.chdir(os.path.dirname(os.path.abspath(__file__)))            #???

"""
ROOM 1
1. I want the window to pop up when player is next to queen 
2. After the queens message is told, I want the player to have to choose one of the outfit choices by clicking a or b or c
3. Each of the letters should change the image of the player to one linked to the letter ( so ex. outfit a would have a dress, outfit b pants etc.)
4. After outfit is picked, I want the an envelope to be added to the backpack to symbolize the message from the queen  

ROOM 2 
1. character spawns in tall grass (the whole grid filled with separate grass images which the player can be seen behind)
2. one of the positions there is a cat - if player is on a spot next to the cat, a window appears at the bottom saying : " pet the cat " with yes (press Y) or no (press N) at the bottom 
    - if y pressed the cat meows, if n pressed the cat hisses 
3. to get to a new room the player has to find an exit in the tall grass, the exit door appears after interaction with cat (both y or n)
4. once player steps on the door, the scene changes to next room 

PROBLEMS: 
1. outfit 1 not working (can be fixed later)
2. comments (ignore for now)
3. SOUND (final touch)

"""

py.init()                       #??
py.mixer.init()                 #?? 

cell_w, cell_h = 60, 60                                              # the size of one ?
row, col = 9, 9                                                      # the amount of ? 
screen_w, screen_h = col * cell_w, row * cell_h                      # screen height and width 
panel_w = 3 * cell_w                                                 # with of the panel on the side 

grid = [[randint(0,4) for i in range(col)] for j in range(row)]      #?? 


"""
SCHOOL
"""
# sound = py.mixer.Sound("C:/Users/04Solec/PreDP2-MagdalenaK/Game/Creeper_death.oga")

char = py.image.load("C:/Users/04Solec/PreDP2-MagdalenaK/Game/charheart.svg.svg")
char = py.transform.scale(char, (60, 60))

bg = py.image.load("C:\\Users\\04Solec\\PreDP2-MagdalenaK\\PygameProject\\Game\\white_bg.jpg")
bg = py.transform.scale(bg, (screen_w, screen_h))

queen = py.image.load("C:/Users/04Solec/PreDP2-MagdalenaK/PygameProject/Game/Question-Mark-Fractal.svg")
queen = py.transform.scale(queen, (60,60))

# outfit_a = py.image.load("C/Users/04Solec/PreDP2-MagdalenaK/PygameProject/Game/fitone.svg" )
# outfit_a = py.transform.scale(outfit_a, (60,60))

outfit_b = py.image.load( "C:/Users/04Solec/PreDP2-MagdalenaK/PygameProject/Game/fittwo.svg" )
outfit_b = py.transform.scale(outfit_b, (60,60))

outfit_c = py.image.load( "C:/Users/04Solec/PreDP2-MagdalenaK/PygameProject/Game/fitthree.svg")
outfit_c = py.transform.scale(outfit_c, (60,60))

envelope = py.image.load( "C:/Users/04Solec/PreDP2-MagdalenaK/PygameProject/Game/zero.svg" )
envelope = py.transform.scale(envelope, (40,40))

door_img = py.image.load( "C:/Users/04Solec/PreDP2-MagdalenaK/PygameProject/Game/x.png" )
door_img = py.transform.scale(door_img, (60,60))

grass_img = py.image.load( "C:/Users/04Solec/PreDP2-MagdalenaK/PygameProject/Game/grass.png" )
grass_img = py.transform.scale(grass_img,(60,60))

"""
HOME 

# sound = py.mixer.Sound("C:/Users/04Solec/PreDP2-MagdalenaK/Game/Creeper_death.oga")

char = py.image.load("C:/Users/me/OneDrive/Obrazy/Dokumenty/python 2IB/charheart.svg.svg")
char = py.transform.scale(char, (60, 60))

bg = py.image.load("C:/Users/me/OneDrive/Obrazy/Dokumenty/python 2IB/white_bg.jpg")
bg = py.transform.scale(bg, (screen_w, screen_h))

queen = py.image.load("C:/Users/me/OneDrive/Obrazy/Dokumenty/python 2IB/Question-Mark-Fractal.svg")
queen = py.transform.scale(queen, (60,60))

outfit_a = py.image.load("C:/Users/me/OneDrive/Obrazy/Dokumenty/python 2IB/outfitone.svg")
outfit_a = py.transform.scale(outfit_a, (60,60))

outfit_b = py.image.load("C:/Users/me/OneDrive/Obrazy/Dokumenty/python 2IB/outfittwo.svg")
outfit_b = py.transform.scale(outfit_b, (60,60))

outfit_c = py.image.load("C:/Users/me/OneDrive/Obrazy/Dokumenty/python 2IB/outfitthree.svg")
outfit_c = py.transform.scale(outfit_c, (60,60))

envelope = py.image.load("C:/Users/me/OneDrive/Obrazy/Dokumenty/python 2IB/zero.svg")
envelope = py.transform.scale(envelope, (40,40))

door_img = py.image.load("C:/Users/me/OneDrive/Obrazy/Dokumenty/python 2IB/x.png")
door_img = py.transform.scale(door_img, (60,60))

grass_img = py.image.load(  )
grass_img = py.transform.scale(grass_img,(60,60))
"""


current_skin = char                                                  #???

clock  = py.time.Clock()                                             #clock object to control game speed (frames per sec)
screen = py.display.set_mode((screen_w + panel_w, screen_h))         #creates game window and sets width and height
py.display.set_caption("Generating random grid")                     #the window title NEEDS TO BE CHANGED 

p1 = Player(0, 0, 60, 60, char)                                     #creates player object with starting position, player size and image                
p2 = Human(8, 4, cell_w, cell_h, queen)                             #creates NPC with grid position, size and image 

def is_next_to(p1, target):                                         #function which checks if player is directly beside target 
    return abs(p1.x - target[0]) + abs(p1.y - target[1]) == 1       #distance between p1 and target ( horizontal, vertical) abs(...) makes distance positive - if distance is 1 p1 and target are touching veritcally or horizontally 


def drawPanel():                                                                                #function which draws inventory 
    font = py.font.SysFont(None, 30)                                                            #font object for text (none = defoult font NEEDS TO BE CHANGED, 30 = font size)
    py.draw.rect(screen, "#F891BB", (screen_w, 0, panel_w, screen_h))                           # draws rectangle on screen ( with coulour, rectangle position and size)

    screen.blit(font.render("BACKPACK", True, "#ffffff"), (screen_w + 20, 40))                  # draws text onto the panel (text, smooth edges, colour)(position near to of side panel)

    if has_letter:                                                                              #checks if player have letter item??
        screen.blit(envelope, (screen_w + 70, 250))                                             # draws envelope (position)

    if outfit_state == "choosing":                                                              #checks if outfit is being selected
        options = ["A", "B", "C"]                                                               # list of outfit choices
        y = 100                                                                                 # vertical position of options

        for i, opt in enumerate(options):                                                       #loops through options ( index numb, value )??
            if selected_outfit == i:                                                            #selected text is green     
                color = (0,255,0)
            else:
                color = (255,255,255)                                                           #not selected white 
            screen.blit(font.render(f"Outfit {opt}", True, color), (screen_w + 20, y))          #draws coloumn with outfit options 
            y += 40                                                                             #moves next option down by 40 pixels     


font = py.font.SysFont('Arial', 24)             #object for font 

game_state = "kingdom"                          #stores the current room of the game, starts in kingdom 

cat_pos = (6, 6)                                #cats grid position
grass_zone = (3, 2, 3, 4)                       #rectangular grass area DELETE
door_pos = (8, 8)                               #dorrs grid position 

active_message = None                           #dialogue variable

messages = [                                    #list of dialogue items 
    "Queen: Welcome, traveler.",
    "Our kingdom is in danger.",
    "You must begin your journey."
]

message_index = 0                               #the message currently shown

outfit_state = "locked"                         #outfit selection status 
selected_outfit = None                          #the outift pick 
has_letter = False                              #player has or doesnt have the letter 

run = True                              #main game loop 
while run:
    for event in py.event.get():        #event queue

        if event.type == py.QUIT:       #if x buttom pressed game close
            run = False 

        if event.type == py.KEYDOWN:    #key pressed 

            # ---------------- OUTFIT SELECTION ----------------
            if outfit_state == "choosing":                  #when game in outfit selection
                                                            # if pressed key a = outfit a
                                                            #                b = outfit b
                                                            #                c = outfit c 
                if event.key == py.K_a:
                    selected_outfit = 0
                    current_skin = outfit_a

                elif event.key == py.K_b:
                    selected_outfit = 1
                    current_skin = outfit_b

                elif event.key == py.K_c:
                    selected_outfit = 2
                    current_skin = outfit_c

                elif event.key == py.K_RETURN and selected_outfit is not None:          #when return pressed outfit selection over
                    outfit_state = "done"
                    has_letter = True

            # ---------------- KINGDOM ----------------
            if game_state == "kingdom":

                if event.key == py.K_SPACE:

                    if active_message is None and is_next_to(p1, (p2.x, p2.y)):     #no dialogue
                        active_message = messages[0]
                        message_index = 0

                    elif active_message is not None:                                #moves to next line of dialogue     
                        message_index += 1

                        if message_index < len(messages):                           #show next message 
                            active_message = messages[message_index]

                        else:
                            active_message = None                                   #end dialogue 
                            message_index = 0                                       #reset dialogue
                            outfit_state = "choosing"                               #trigget outift selection 

                # ---------------- MOVEMENT ----------------
                elif active_message is None and outfit_state != "choosing":         #when no dialogue and no outfit selection 
                                                                                    #movement in 4 directions based on arrows

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
            elif game_state == "fields": # IDK DELETE THIS LATER

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
            if game_state == "kingdom":

                #when outfit selection done and player on door
                if (
                    outfit_state == "done"
                    and (p1.x, p1.y) == door_pos
                ):

                    game_state = "fields"

                    # spawn location in fields
                    p1.x = 1
                    p1.y = 1


            if game_state == "fields":          #check if player on top edge of field map 
                if p1.y == 0:
                    game_state = "forest1"      #spawn in forest1
                    p1.x, p1.y = 4, 8           #spawn at bottom 

            elif game_state == "forest1":      #??? LATER 
                if p1.y == 0:
                    game_state = "forest2"
                    p1.x, p1.y = 4, 8

            elif game_state == "forest2":
                if p1.y == 0:
                    game_state = "city"
                    p1.x, p1.y = 4, 8

            #NPC dialogue if player next to character and  if no message or outtfit selection 
            if (        
                is_next_to(p1, (p2.x, p2.y))
                and active_message is None
                and outfit_state == "locked"
            ):
                active_message = messages[0]
                message_index = 0


        # ---------------- DRAW ----------------
        clock.tick(10)                      #game loop 10 times per sec 

        screen.blit(bg, (0,0))              #draw background image on screen

        drawPanel()                         #draw inventory 

        # outfit instructions
        if outfit_state == "choosing":

            #text surface 
            choose_text = font.render(
                "Choose outfit: A / B / C",       #display
                True,                             #smooth edges
                (255,255,0)                       #colour CHANGE
            )

            enter_text = font.render(
                "Press ENTER to confirm",   #display
                True,                       #smooth edges
                (255,255,255)               #colour CHANGE
            )

            #draws text at given position 
            screen.blit(choose_text, (80, 500))
            screen.blit(enter_text, (80, 530))


        # ---------------- MAP DRAWING ----------------
        if game_state == "kingdom":
            # draw transition door AFTER outfit selection
            if outfit_state == "done":
                screen.blit(door_img, (door_pos[0] * cell_w, door_pos[1] * cell_h))

            screen.blit(current_skin, (p1.x * cell_w, p1.y * cell_h))       #draw player
            screen.blit(queen, (p2.x * cell_w, p2.y * cell_h))              #draw NPC


        elif game_state == "fields":

            screen.fill((120, 200, 120))        #background CHANGE

            gx, gy, gw, gh = grass_zone         #DELETE LATER 

            py.draw.rect(
                screen,
                (80, 180, 80),
                (gx*cell_w, gy*cell_h, gw*cell_w, gh*cell_h)
            )

            #cat CHANGE LATER 
            py.draw.rect(
                screen,
                (200, 200, 200),
                (cat_pos[0]*cell_w, cat_pos[1]*cell_h, cell_w, cell_h)
            )

            screen.blit(current_skin, (p1.x * cell_w, p1.y * cell_h))   #draw player

        #other rooms PROBLEM FOR LATER  
        elif game_state == "forest1":

            screen.fill((70, 140, 70))
            screen.blit(current_skin, (p1.x * cell_w, p1.y * cell_h))


        elif game_state == "forest2":

            screen.fill((40, 70, 40))
            screen.blit(current_skin, (p1.x * cell_w, p1.y * cell_h))


        elif game_state == "city":

            screen.fill((180, 180, 200))
            screen.blit(current_skin, (p1.x * cell_w, p1.y * cell_h))


        # ---------------- POPUP ----------------
        if active_message:

            popup_w = 400
            popup_h = 120

            popup_x = (screen_w - popup_w) // 2
            popup_y = (screen_h - popup_h) // 2

            overlay = py.Surface((popup_w, popup_h))
            overlay.fill((40, 40, 40))

            py.draw.rect(
                overlay,
                (255,255,255),
                (0,0,popup_w,popup_h),
                3
            )

            text_surf = font.render(
                active_message,
                True,
                (255,255,255)
            )

            screen.blit(overlay, (popup_x, popup_y))
            screen.blit(text_surf, (popup_x + 20, popup_y + 45))


        py.display.flip()