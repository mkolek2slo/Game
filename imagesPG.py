"""
Images in Pygame 

the way images work - they are drawn on a surface.
create rectangle of a given size and then we will simply draw the image 
at the coordinates of the rectangle.
All images used in project must be located withinh the same folder as the script 
Never load an image inside the loop. You can draw inside a loop 
"""
import pygame as py
py.init()

w, h = 600, 600 
screen = py.display.set_mode((w,h))
py.display.set_caption("working with images in pygame")
# img = py.image.load("./Game/charheart.svg")
img = py.image.load("C:/Users/04Solec/PreDP2-MagdalenaK/Game/charheart.svg.svg")
img = py.transform.scale(img, (60, 60))
x, y = 0, 0

clock = py.time.Clock()

run = True 
while run:
    clock.tick(25)
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False 
    screen.fill("#ffffff")
    screen.blit(img, (x, y))
    x, y = x+1, y+1


    py.display.flip()

py.quit

