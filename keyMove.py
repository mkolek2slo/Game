import pygame as py

py.init()
sWidth, sHeight = 600, 600
screen = py.display.set_mode((sWidth, sHeight))
py.display.set_caption("Keyboard movement")






x, y, r = sWidth/2, sHeight/2, 20
speedX, speedY = 5, 5 

def Coll(x, y, r):
    if y+r >= 200 and y+r <= 300:    
        if x+r >= 400 and x-r <= 405:
            print("COLLISION")
            return True 
        return False
    
# object of clock 
"""
efficient way of coding games - doesnt use CPU or battery a lot 
will halt the processing for this program depending on the clock speed 
"""   
clock = py.time.Clock() 

running = True 
while running:
    for event in py.event.get():
        if event.type == py.QUIT: 
            running = False
        clock.tick(10)      # max framerate 60 

    screen.fill("#AAAAAA")    
    py.draw.circle(screen, "#8100D1", (x, y), r) 
    py.draw.line(screen, "#FF52A0", (400, 200), (400, 300), 5)

    keys = py.key.get_pressed()     #checks if key pressed 
    if keys[py.K_LEFT] and not Coll(x, y, r):        #_a        dictionary [index by key]
        if x > r:
            x -= speedX
    if keys[py.K_RIGHT] :
        if x < 600 - r:
          x += speedX

    if keys[py.K_UP]:
        if y > r:
            y -= speedY
    if keys[py.K_DOWN]:
        if y < 600 - r: 
            y += speedY

    py.display.flip()  
    # py.time.delay(20)

py.quit()