'''
Joseph DiMartino and Devin Mason
'''
# IMPORT MODULES
import pygame
import sys

# Initialze pygame
pygame.init()

# CONSTANTS
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = pygame.Color('grey12')
LIGHT_GREY = (200, 200, 200)

player_score = 0 # Initialize scores
opponent_score = 0

max_misses = 3 # Set the maximum number of misses before game over


# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

# Clock for controlling the frame rate
clock = pygame.time.Clock()

''' 
DEFINE THE BALL AND PADDLES USING PYGAMES RECT OBJECTS
'''
# Ball
ball = pygame.Rect(SCREEN_WIDTH // 2 - 15, SCREEN_HEIGHT // 2 - 15, 30, 30)
ball_speed_x = 7
ball_speed_y = 7

# Player Paddle
player = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2 - 70, 10, 140)
player_speed = 0

# Opponent Paddle
opponent = pygame.Rect(10, SCREEN_HEIGHT // 2 - 70, 10, 140)
opponent_speed = 7

'''
GAME FUNCTIONS TO HANDLE BALL MOVEMENT - COLLISIONS - PADDLE MOVEMENT
'''
def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with top or bottom
    if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
        ball_speed_y *= -1

    # Ball passes the player
    if ball.right >= SCREEN_WIDTH:
        opponent_score += 1
        ball_restart()
        if opponent_score >= max_misses:
            game_over("Opponent")

    # Ball passes the opponent
    if ball.left <= 0:
        player_score += 1
        ball_restart()
        if player_score >= max_misses:
            game_over("Player")

    # Ball collision with paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= SCREEN_HEIGHT:
        player.bottom = SCREEN_HEIGHT

def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= SCREEN_HEIGHT:
        opponent.bottom = SCREEN_HEIGHT

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    ball_speed_y *= -1
    ball_speed_x *= -1

def game_over(winner):
    # Display the winner
    font = pygame.font.Font(None, 74)
    text = font.render(f"{winner} Wins!", True, LIGHT_GREY)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)

    # Ask the player if they want to play again
    play_again = True
    while play_again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    reset_game()
                    play_again = False
                elif event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()

def reset_game():
    global player_score, opponent_score
    player_score = 0
    opponent_score = 0
    ball_restart()

## MAIN GAME LOOP ##
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 6
            if event.key == pygame.K_UP:
                player_speed -= 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 6
            if event.key == pygame.K_UP:
                player_speed += 6

    # Game logic
    ball_animation()
    player_animation()
    opponent_ai()

    # Drawing
    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, LIGHT_GREY, player)
    pygame.draw.rect(screen, LIGHT_GREY, opponent)
    pygame.draw.ellipse(screen, LIGHT_GREY, ball)
    pygame.draw.aaline(screen, LIGHT_GREY, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    # Display scores
    font = pygame.font.Font(None, 36)
    player_text = font.render(f"Player: {player_score}", True, LIGHT_GREY)
    screen.blit(player_text, (SCREEN_WIDTH - 150, 20))
    opponent_text = font.render(f"Opponent: {opponent_score}", True, LIGHT_GREY)
    screen.blit(opponent_text, (20, 20))

    # Update the display
    pygame.display.flip()
    clock.tick(60)