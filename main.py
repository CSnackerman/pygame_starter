from sys import exit

import pygame
from pygame.locals import *
from pygame import Rect, Vector2, Color

from platform import Platform

from gamesettings import RESOLUTION, WINDOW_FLAGS, CURSOR_VISIBLE
from gamesettings import WIDTH, HEIGHT, BG_COLOR

from player import Player


# --- Setup ---

# pygame
pygame.init()

# window
window = pygame.display.set_mode (RESOLUTION, WINDOW_FLAGS)
window_rect = window.get_rect()
pygame.display.set_caption("Plat")

# time & fps
clock = pygame.time.Clock()
frame_time = 0
frame_counter = 0



# miscellaneous
pygame.mouse.set_visible(CURSOR_VISIBLE)



# --- Game Objects ---

# player
player = Player()

# platforms
p1 = Platform (100, HEIGHT - 100, 200, 10, Color (255, 0, 0, 255))

# fps text
bold, antialias = True, True
fps_font = pygame.font.SysFont ('Verdana', 11, bold)
fps_font_color = Color (255, 255, 255)
fps_text_surface = fps_font.render ('1000 FPS', antialias, fps_font_color)
fps_text_position_x = WIDTH - fps_text_surface.get_rect().width



# --- Functions ---




# --- Game Loop ---

RUNNING = 1
while (RUNNING):

    # time & framerate
    pygame.time.delay(5)
    dt = clock.get_time() / 1000.0    # delta time (sec)
    clock.tick()
    frame_time += dt
    frame_counter += 1
    
    # keyboard events

    pressed_keys = pygame.key.get_pressed()

    player.move_horizontal(pressed_keys)
    
    # quit
    if pressed_keys [K_ESCAPE]:
        print ("pressed escape... quitting!")
        RUNNING = 0
        
    
    # events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print ("clicked the X... quitting!")
            RUNNING = 0
            break
        
        # keyboard events
        if event.type == pygame.KEYDOWN:

            key = event.key
            
            # jump
            if key == K_SPACE:
                player.jump (p1)




    # render average frame rate
    if ( frame_time > 0.5 ):

        fps = str ( int ( frame_counter / frame_time ) )
        # fps = str ( int ( clock.get_fps() ) )
        
        frame_time = 0
        frame_counter = 0
            
        pygame.display.set_caption ("Plat - " + fps + " fps" )

        fps_text_surface = fps_font.render (
            fps + ' FPS', 
            antialias,  
            fps_font_color
        )
    
    player.update(dt, p1)

    # clear
    window.fill (BG_COLOR)

    # render game objects
    p1.draw(window)

    player.draw (window)

    window.blit ( fps_text_surface, (fps_text_position_x, 0) )

    # swap the framebuffer
    pygame.display.update()





# --- Exit ---

pygame.quit()
exit()