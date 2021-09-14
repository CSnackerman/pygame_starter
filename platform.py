import pygame
from pygame import Rect, Color

import pymunk

class Platform:

    # constructor
    def __init__ (self, x, y, w, h, c, space):
        
        self.width = w
        self.height = h
        self.rectangle = Rect (x, y, w, h)
        self.color = Color (c)

        # pymunk stuff
        self.body = pymunk.Body(1, 0, pymunk.Body.KINEMATIC)
        self.body.position = (x, y)
        self.hitbox = pymunk.Poly.create_box (self.body, (self.width, self.height))
        space.add (self.body, self.hitbox)

    
    # to string
    def __str__ (self):

        output = "\n--- Platform ---"
        output += "\nx\t" + str (self.rectangle.x)
        output += "\ny\t" + str (self.rectangle.y)
        output += "\nw\t" + str (self.width)
        output += "\nh\t" + str (self.height)
        output += "\nc\t" + str (self.color)
        
        return output

    def draw(self, window):
        pygame.draw.rect (window, self.color, self.rectangle)


#  testing
if __name__ == "__main__":  # only runs if the file is directly run (not imported)

    p = Platform (10, 10, 20, 25, Color (0, 0, 0))

    print (p)