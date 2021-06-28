from sys import exit

import pygame
from pygame.locals import *
from pygame import Rect, Vector2, Color


# --- Globals ---

RUNNING = 1


# --- Configuration ---

WINDOW_FLAGS = DOUBLEBUF
WIDTH = 800
HEIGHT = 600
RESOLUTION = (WIDTH, HEIGHT)
FPS_LIMIT = 144
FILL_COLOR = Color (27, 27, 27)


# --- Functions ---

def handle_events():

    global RUNNING

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            RUNNING = 0



# --- Setup ---

pygame.init()
window = pygame.display.set_mode(RESOLUTION, WINDOW_FLAGS)
pygame.display.set_caption("Plat")
fps = pygame.time.Clock()

player_width = 25
player_height = 50
player_rect = Rect (0, 0, player_width, player_height)
player_color = Color (27, 97, 29)
player_x = 0
player_y = 0
player_speed = 0.5


# --- Run ---

while (RUNNING):

    # events
    handle_events()

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys [K_UP]:
        player_y -= player_speed
    
    if pressed_keys[K_DOWN]:
        player_y += player_speed

    if pressed_keys [K_LEFT]:
        player_x -= player_speed

    if pressed_keys [K_RIGHT]:
        player_x += player_speed

    # update
    player_rect.update(player_x, player_y, player_width, player_height)

    # clear
    window.fill (FILL_COLOR)
    
    # render
    pygame.draw.rect(window, player_color, player_rect)

    # swap the framebuffer
    pygame.display.update()


# --- Exit ---

pygame.quit()
exit()