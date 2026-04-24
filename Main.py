import pygame as py 
from player import Player
from random import randint

py.init()
w, h = 600, 600 
screen = py.display.set_mode((w, h))
py.display.set_caption("creating player object")

print(screen.get_width())

p1 = Player(w/2, h/2, 50, 50)
p2 = Player(500, 500, 50, 50)

run = True 
clock = py.time.Clock()

while run:
    for event in py.event.get(): 
        if event.type == py.QUIT:
            run = False 
    clock.tick(60)
    screen.fill("#FFE5E5")
  
    p1.draw(screen)
    p2.draw(screen)
    p1.move(screen)
    
    p1.collision(p2)

    
    # p2.move(screen)
    py.display.flip()


