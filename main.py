from sys import exit

import pygame
from pygame.locals import *
from pygame import Rect, Vector2, Color


# --- Globals ---

RUNNING = 1
MAX_SPEED = 500


# --- Configuration ---

WINDOW_FLAGS = 0
CURSOR_VISIBLE = True

WINDOW_FLAGS = FULLSCREEN | HWSURFACE | NOFRAME | DOUBLEBUF
CURSOR_VISIBLE = False

WIDTH = 1920
HEIGHT = 1080
RESOLUTION = (WIDTH, HEIGHT)

FILL_COLOR = Color (27, 27, 27)


# --- Setup ---

# pygame
pygame.init()
window = pygame.display.set_mode(RESOLUTION, WINDOW_FLAGS)
pygame.display.set_caption("Plat")
pygame.mouse.set_visible(CURSOR_VISIBLE)

# time & fps
clock = pygame.time.Clock()
fps_list = []
fps_list_len = 0

# miscellaneous
window_center_x = WIDTH // 2
window_center_y = HEIGHT // 2


# --- Game Objects ---

# player
player_width = 25
player_height = 50
player_half_width = player_width // 2
player_half_height = player_height // 2
player_position = Vector2 ( [window_center_x - player_half_width, window_center_y - player_half_height] ) 
player_velocity = Vector2 ( [0.0, 0.0] ) 
player_rect = Rect (player_position.x, player_position.y, player_width, player_height)
player_color = Color (27, 97, 29)

# fps text
bold, antialias = True, True
fps_font = pygame.font.SysFont ('Verdana', 11, bold)
fps_text_surface = fps_font.render ('144 FPS', antialias, (255, 255, 255, 100))
fps_text_position_x = WIDTH - fps_text_surface.get_rect().width


# --- Run ---

while (RUNNING):

    # time & framerate
    # pygame.time.wait(2)
    clock.tick()
    dt = clock.get_time() / 1000.0    # delta time (sec)
    fps = int (clock.get_fps())
    fps_list.append (fps)
    fps_list_len += 1


    # quit event
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            RUNNING = 0
            break
    
    # keyboard events
    pressed_keys = pygame.key.get_pressed()

    player_velocity.update (0, 0)

    if pressed_keys [K_UP]:
        player_velocity.y -= 1
    
    if pressed_keys[K_DOWN]:
        player_velocity.y += 1
        
    if pressed_keys [K_LEFT]:
        player_velocity.x -= 1

    if pressed_keys [K_RIGHT]:
        player_velocity.x += 1
    
    if pressed_keys [K_ESCAPE]:
        RUNNING = 0
        break

    # display average frame rate every 100 frames

    if ( fps_list_len >= 100 ):
        
        total = 0
        for f in fps_list:
            total += f

        avg_fps = int (total / fps_list_len)
            
        pygame.display.set_caption ("Plat - " + str (avg_fps) + " fps" )
        fps_list.clear()
        fps_list_len = 0

        fps_text_surface = fps_font.render (str (avg_fps) + ' FPS', True, (255, 255, 255))
    
    # move the player rect
    if player_velocity.x != 0 or player_velocity.y != 0:
        player_position += player_velocity.normalize() * MAX_SPEED * dt
        player_rect.update (player_position.x, player_position.y, player_width, player_height)

    # clear
    window.fill (FILL_COLOR)

    # render game objects
    pygame.draw.rect (window, player_color, player_rect)

    window.blit ( fps_text_surface, (fps_text_position_x, 0) )

    # swap the framebuffer
    pygame.display.update()


# --- Exit ---

pygame.quit()
exit()