"""
here will be stored classes of different characters
"""

class Human:
    """
    rectangle object of pygame must take x, y, width and height
    """

    def __init__(self, x:int, y:int, width:int, height:int, img):
        #instance variables, specific to given object
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.rect = (self.x, self.y, self.w, self.h)
        self.img = img

    def draw(self, screen):
       screen.blit(self.img, (self.x * self.w, self.y * self.h))

    # def display(self):
            # \r wraca na początek aktualnej linii

