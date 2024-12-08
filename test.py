import pygame
import sys

pygame.init()

# Create the window and what it's size will be (by pixels)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
circles = []
rects = []

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('First Game')


# --- Main Game Loop ---
run = True
while run:

    # --- Event Handler Loop ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            circles.append((x, y))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            x, y = event.pos
            rects.append((x, y, 20, 20))

    screen.fill((0, 0, 0))
    for circle in circles:
        # draw a red circle with a radius of 10 at whatever coordinate you clicked
        pygame.draw.circle(screen, (255, 0, 0), circle, 10)
    for rect in rects:
        pygame.draw.rect(screen, (0, 0, 255), rect, 1)

    pygame.display.flip()


pygame.quit()
sys.exit()
