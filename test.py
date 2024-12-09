import pygame
import sys
import random

# initialize pygame modules
pygame.init()

# Create the window and what it's size will be (by pixels)
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h

circles = []
rects = []

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption('First Game')

BG_COLOR = pygame.Color('grey12') # dark grey
hue = 0 # hue 0 = red
def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

# create clock object
clock = pygame.time.Clock()


# --- Main Game Loop ---
run = True
while run:

    # --- Event Handler Loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # check for X out of game
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: # left-click
            x, y = event.pos
            random_color = get_random_color()
            circles.append({'position': (x, y), 'random_color': random_color})
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3: # right-click
            x, y = event.pos
            box_color = pygame.Color(0)
            box_color.hsva = (hue, 100, 100, 100)
            hue = (hue + 30) % 360
            rects.append({'position': (x, y, 20, 20), 'color': box_color})

    screen.fill(BG_COLOR) # set background color to gray12

    # loop through circle/rects list to place on screens / place new onto screen
    for circle in circles:
        pygame.draw.circle(screen, circle["random_color"], circle['position'], 10)
    for rect in rects:
        pygame.draw.rect(screen, rect['color'], rect['position'], 2)

    pygame.display.flip() # update window
    clock.tick(60) # 60 fps



pygame.quit()
sys.exit()
