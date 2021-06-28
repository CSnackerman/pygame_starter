from sys import exit

import pygame
from pygame.locals import *
from pygame import Rect, Vector2, Color


# --- Globals ---

RUNNING = 1
MAX_SPEED = 1000


# --- Configuration ---

WINDOW_FLAGS = 0
WINDOW_FLAGS = FULLSCREEN | HWSURFACE | NOFRAME | DOUBLEBUF
WIDTH = 1280
HEIGHT = 720
RESOLUTION = (WIDTH, HEIGHT)
FILL_COLOR = Color (27, 27, 27)


# --- Setup ---

pygame.init()
window = pygame.display.set_mode(RESOLUTION, WINDOW_FLAGS)
pygame.display.set_caption("Plat")
clock = pygame.time.Clock()
fps_list = []


# --- Game Objects ---

player_width = 25
player_height = 50
player_rect = Rect (0, 0, player_width, player_height)
player_color = Color (27, 97, 29)
player_x = 0
player_y = 0
player_position = Vector2 ( [0, 0] ) # TODO fix diagonal movement speedup
player_velocity = Vector2 ( [0, 0] ) # TODO


bold, antialias = True, True
fps_font = pygame.font.SysFont ('Verdana', 11, bold)
fps_text_surface = fps_font.render ('144 FPS', antialias, (255, 255, 255, 100))
fps_text_position_x = WIDTH - fps_text_surface.get_rect().width


# --- Run ---

while (RUNNING):

    # time & framerate
    pygame.time.wait(1)
    clock.tick()
    dt = clock.get_time() / 1000.0    # delta time (sec)
    fps = int (clock.get_fps())
    fps_list.append (fps)

    # quit event
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            RUNNING = 0
            break
    
    # keyboard events
    pressed_keys = pygame.key.get_pressed()

    if pressed_keys [K_UP]:
        player_y -= MAX_SPEED * dt
    
    if pressed_keys[K_DOWN]:
        player_y += MAX_SPEED * dt

    if pressed_keys [K_LEFT]:
        player_x -= MAX_SPEED * dt

    if pressed_keys [K_RIGHT]:
        player_x += MAX_SPEED * dt

    if pressed_keys [K_ESCAPE]:
        RUNNING = 0
        break

    # display average frame rate every 100 frames
    fps_list_length = len (fps_list)

    if ( fps_list_length >= 100 ):
        
        total = 0
        for f in fps_list:
            total += f

        avg_fps = int (total / fps_list_length)
            
        pygame.display.set_caption ("Plat - " + str (avg_fps) + " fps" )
        fps_list.clear()

        fps_text_surface = fps_font.render (str (avg_fps) + ' FPS', True, (255, 255, 255))
    
    # move the player rect
    player_rect.update (player_x, player_y, player_width, player_height)

    # clear
    window.fill (FILL_COLOR)

    # render game objects
    pygame.draw.rect (window, player_color, player_rect)

    window.blit ( fps_text_surface, (fps_text_position_x, 0) )

    # swap the framebuffer
    pygame.display.flip()


# --- Exit ---

pygame.quit()
exit()