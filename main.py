from sys import exit

import pygame
from pygame.locals import *
from pygame import Rect, Vector2, Color


# --- Configuration ---

WINDOW_FLAGS = 0
CURSOR_VISIBLE = True

# WINDOW_FLAGS = FULLSCREEN | HWSURFACE | NOFRAME | DOUBLEBUF
# CURSOR_VISIBLE = False

WIDTH = 1024
HEIGHT = 768
RESOLUTION = (WIDTH, HEIGHT)
ASPECT_RATIO = WIDTH / HEIGHT

BG_COLOR = Color (27, 27, 27)

# --- Setup ---

# pygame
pygame.init()

# window
window = pygame.display.set_mode (RESOLUTION, WINDOW_FLAGS)
window_rect = window.get_rect()
window_center_x = WIDTH // 2
window_center_y = HEIGHT // 2
window_side_diff = WIDTH - HEIGHT
pygame.display.set_caption("Plat")

# time & fps
clock = pygame.time.Clock()
frame_time = 0
frame_counter = 0

# game settings
MAX_SPEED = 500

# miscellaneous
pygame.mouse.set_visible(CURSOR_VISIBLE)


# --- Game Objects ---

# player
player_width = WIDTH // 42
player_height = HEIGHT // 15
player_half_width = player_width // 2
player_half_height = player_height // 2

player_position = Vector2 ([
    window_center_x - player_half_width, 
    window_center_y - player_half_height
]) 

player_velocity = Vector2 ( [0.0, 0.0] ) 

player_rect = Rect (
    player_position.x,
    player_position.y,
    player_width,
    player_height
)

player_color = Color (27, 97, 29)

# fps text
bold, antialias = True, True
fps_font = pygame.font.SysFont ('Verdana', 11, bold)
fps_font_color = Color (255, 255, 255)
fps_text_surface = fps_font.render ('1000 FPS', antialias, fps_font_color)
fps_text_position_x = WIDTH - fps_text_surface.get_rect().width


# --- Game Loop ---

RUNNING = 1
while (RUNNING):

    # time & framerate
    clock.tick()
    dt = clock.get_time() / 1000.0    # delta time (sec)
    frame_time += dt
    frame_counter += 1
    
    # keyboard events
    pressed_keys = pygame.key.get_pressed()

    player_velocity.update (0, 0)

    if pressed_keys [K_UP]:
        player_velocity.y -= 1
    
    if pressed_keys [K_DOWN]:
        player_velocity.y += 1
        
    if pressed_keys [K_LEFT]:
        player_velocity.x -= 1

    if pressed_keys [K_RIGHT]:
        player_velocity.x += 1
    
    if pressed_keys [K_ESCAPE]:
        print ("pressed escape... quitting!")
        RUNNING = 0
        
    # quit event
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print ("clicked the X... quitting!")
            RUNNING = 0
            break

    # render average frame rate
    if ( frame_time > 0.5 ):

        fps = str ( int ( frame_counter / frame_time ) )
        
        frame_time = 0
        frame_counter = 0
            
        pygame.display.set_caption ("Plat - " + fps + " fps" )

        fps_text_surface = fps_font.render (fps + ' FPS', antialias, fps_font_color)
    
    # move the player rect
    if player_velocity.x != 0 or player_velocity.y != 0:

        player_position += player_velocity.normalize() * MAX_SPEED * dt

        new_x = player_position.x
        new_y = player_position.y
        
        player_rect.update (new_x, new_y, player_width, player_height)

    # clear
    window.fill (BG_COLOR)

    # render game objects
    pygame.draw.rect (window, player_color, player_rect)

    window.blit ( fps_text_surface, (fps_text_position_x, 0) )

    # swap the framebuffer
    pygame.display.update()


# --- Exit ---

pygame.quit()
exit()