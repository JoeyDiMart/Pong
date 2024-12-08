import pygame
import sys
import random

pygame.init()

# Create the window and what it's size will be (by pixels)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


circles = []
rects = []

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('First Game')

BG_COLOR = pygame.Color('grey12')
hue = 0
def get_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

clock = pygame.time.Clock()


# --- Main Game Loop ---
run = True
while run:

    # --- Event Handler Loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            random_color = get_random_color()
            circles.append({'position': (x, y), 'random_color': random_color})
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            x, y = event.pos
            box_color = pygame.Color(0)
            box_color.hsva = (hue, 100, 100, 100)
            hue = (hue + 30) % 360
            rects.append({'position': (x, y, 20, 20), 'color': box_color})

    screen.fill(BG_COLOR)
    for circle in circles:
        pygame.draw.circle(screen, circle["random_color"], circle['position'], 10)
    for rect in rects:
        pygame.draw.rect(screen, rect['color'], rect['position'], 2)

    pygame.display.flip()
    clock.tick(60)



pygame.quit()
sys.exit()
