import pygame as py
from random import randint
py.mixer.init()

"""
Player 
Obstacle 
move 
collision 
draw

"""

class Player:
    """
    rectangle object of pygame must take x, y, width and height
    """
    #static or class variable 
    speedX, speedY = randint(3, 6), randint(1, 4)
    sound = py.mixer.Sound("C:/Users/04Solec/PreDP2-MagdalenaK/Game/Creeper_death.oga")

    def __init__(self, x:int, y:int, width:int, height:int, img):
        #instance variables, specific to given object
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.rect = (self.x, self.y, self.w, self.h)
        self.collide = False
        self.img = img

    def draw(self, screen):
        # py.draw.rect(screen , "#ffffff", self.rect)
        screen.blit(self.img, (self.x, self.y))
        # return py.draw.rect(screen , "#FF90BC", self.rect)

    def move(self, screen, grid, event):
        r = self.y // 60
        c = self.x // 60
        if event.type == py.KEYDOWN:        #one action per key press 
            if event.key == py.K_LEFT and c - 1 >= 0 and grid[r][c-1] != 0:
                self.x -= 60
                Player.sound.play()
            if event.key == py.K_RIGHT and c + 1 < len(grid[0]) and grid[r][c+1] != 0:
                self.x += 60
                Player.sound.play()
            if event.key == py.K_UP and r - 1 >= 0 and grid[r-1][c] != 0:
                self.y -= 60
                Player.sound.play()
            if event.key == py.K_DOWN and r + 1 < len(grid) and grid[r+1][c] != 0:
                self.y += 60
                Player.sound.play()

        
    def collision(self, enemy):     #enemy player object 
            # |x1 - x2| <= w 
            # |y1 - y2| <= h 
            if abs(self.x - enemy.x) <= self.w and abs(self.y - enemy.y) <= self.h: 
                if self.collide == False:       #1st collision
                    print("collision")
                    self.collide = True     #value to true
                elif self.collide == True:
                    self.collide = False 

class Obstacle: 
    " fixed size, only store x,y coordinates"
    def __init__(self, x: int, y:int, img):
        self.x = x 
        self.y = y 
        self.img = img
                
    def draw(self, screen):
       screen.blit(self.img, (self.x, self.y))
    #    return py.draw.rect(screen, "#000000", (self.x, self.y, 60, 60))
    
        

    
        
        
        
        
        
        
        
        
        # if self.x < screen.get_width() :    #- self.w
        #     self.x += Player.speedX
        # else:
        #     self.x = -self.w
        # Player.speedX = randint(3, 6)
            # pi = Player(self.x - screen.get_width, self.y, self.w, self.h)

        # if self.y < screen.get_height() :   #- self.h
        # #     self.y += Player.speedY
        # else:
        #     self.y = - self.h 
        #     Player.speedY = randint(1,4)
        # self.rect = (self.x, self.y, self.w, self.h)
