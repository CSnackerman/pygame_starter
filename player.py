import pygame
from pygame.locals import *
from pygame import Rect, Vector2, Color
from gamesettings import WIDTH, HEIGHT
from gamesettings import window_center_x, window_center_y
from gamesettings import GRAVITY, ACCELERATION, DECELERATION, JUMP_POWER, MAX_SPEED

import pymunk


class Player:

    def __init__(self, space):

        self.width = WIDTH // 42
        self.height = HEIGHT // 15
        self.half_width = self.width // 2
        self.half_height = self.height // 2

        self.position = Vector2 ([
            window_center_x - self.half_width, 
            window_center_y - self.half_height
        ]) 

        self.velocity = Vector2 ( [0.0, 0.0] ) 

        self.accel = Vector2 ([0, GRAVITY])

        self.rect = Rect (
            self.position.x,
            self.position.y,
            self.width,
            self.height
        )

        self.player_color = Color (27, 97, 29)

        # pymunk stuff
        self.body = pymunk.Body(1, 0)
        self.body.position = (self.position.x, self.position.y)
        self.hitbox = pymunk.Poly.create_box (self.body, (self.width, self.height))
        space.add (self.body, self.hitbox)
    

    def update2(self, dt):
        x = self.hitbox.bb.left
        y = self.hitbox.bb.top
        self.rect.update (x, y, self.width, self.height)


    def touchingGround (self):

        global HEIGHT

        bottom = self.rect.y + self.height

        if bottom >= HEIGHT:
            return True
        
        return False


    def update (self, dt, platforms):

        # apply acceleration
        self.velocity += self.accel * dt

        # apply speed limit
        if self.velocity.x > MAX_SPEED:   # right
            self.velocity.x = MAX_SPEED

        elif self.velocity.x < -MAX_SPEED:    # left
            self.velocity.x = -MAX_SPEED

        if self.velocity.y > MAX_SPEED:   # down
            self.velocity.y = MAX_SPEED

        
        # move the player rect
        if self.velocity.x != 0 or self.velocity.y != 0:
            
            # calculate new position
            self.position.x += self.velocity.x * dt
            self.position.y += self.velocity.y * dt
            
            # update the rectangle
            self.rect.update (
                self.position.x, 
                self.position.y, 
                self.width, 
                self.height
            )

        # collide with floor
        floor = HEIGHT - self.height
        if self.position.y > floor:
            self.position.y = floor
            self.velocity.y = 0

        # collide with platforms
        if self.rect.colliderect (platforms.rectangle):
            self.velocity.y = 0
            self.accel.y = 0
        else:
            self.accel.y = GRAVITY


    def jump (self, platforms):
        if self.touchingGround () or self.rect.colliderect (platforms.rectangle):
            self.velocity.y = -JUMP_POWER

    def move_horizontal(self, keys):

        # accelerate left or right
        if keys [K_LEFT]:
            self.accel.x = -ACCELERATION

        elif keys [K_RIGHT]:
            self.accel.x = ACCELERATION

        # slow down / decelerate
        else:
        
            if self.velocity.x > 5:

                print ("\nacceleration\t velocity")
                print (self.accel, "\t", self.velocity)

                self.accel.x = -DECELERATION

            elif self.velocity.x < -5:

                print ("\nacceleration\t velocity")
                print (self.accel, "\t", self.velocity)

                self.accel.x = DECELERATION

            # stop when slow enough
            else:
                self.accel.x = 0
                self.velocity.x = 0

    
    def draw (self, w):
        pygame.draw.rect (w, self.player_color, self.rect)


    def __str__(self):
        return