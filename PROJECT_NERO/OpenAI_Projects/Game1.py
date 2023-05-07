import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Blocks")

# Set up the player
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_X = WIDTH // 2 - PLAYER_WIDTH // 2
PLAYER_Y = HEIGHT - PLAYER_HEIGHT - 10
PLAYER_COLOR = (0, 255, 0)
PLAYER_SPEED = 5
player_rect = pygame.Rect(PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)

# Set up the blocks
BLOCK_WIDTH = 50
BLOCK_HEIGHT = 50
BLOCK_COLOR = (255, 0, 0)
blocks = []
for i in range(10):
    x = random.randint(0, WIDTH - BLOCK_WIDTH)
    y = random.randint(-500, 0)
    block_rect = pygame.Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
    blocks.append(block_rect)

# Set up the clock
clock = pygame.time.Clock()

# Set up the game loop
game_running = True
while game_running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_rect.right < WIDTH:
        player_rect.x += PLAYER_SPEED

    # Handle block movement
    for block_rect in blocks:
        block_rect.y += 5
        if block_rect.top > HEIGHT:
            block_rect.top = random.randint(-500, 0)
            block_rect.left = random.randint(0, WIDTH - BLOCK_WIDTH)

        # Check for collision with player
        if player_rect.colliderect(block_rect):
            print("Game over!")
            game_running = False

    # Draw everything
    WINDOW.fill((255, 255, 255))
    pygame.draw.rect(WINDOW, PLAYER_COLOR, player_rect)
    for block_rect in blocks:
        pygame.draw.rect(WINDOW, BLOCK_COLOR, block_rect)
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()