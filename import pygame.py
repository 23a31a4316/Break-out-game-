import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 150, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)

# Paddle
paddle = pygame.Rect(WIDTH//2 - 60, HEIGHT - 20, 120, 10)
paddle_speed = 7

# Ball
ball = pygame.Rect(WIDTH//2 - 10, HEIGHT//2 - 10, 15, 15)
ball_speed = [4, -4]

# Bricks
bricks = []
brick_rows = 5
brick_cols = 8
brick_width = WIDTH // brick_cols
brick_height = 25

for row in range(brick_rows):
    for col in range(brick_cols):
        brick = pygame.Rect(col * brick_width, row * brick_height, brick_width - 2, brick_height - 2)
        bricks.append(brick)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    for brick in bricks:
        pygame.draw.rect(screen, GREEN, brick)

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-paddle_speed, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(paddle_speed, 0)

    # Ball movement
    ball.move_ip(ball_speed)

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] *= -1
    if ball.top <= 0:
        ball_speed[1] *= -1
    if ball.bottom >= HEIGHT:
        print("Game Over!")
        running = False

    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_speed[1] *= -1

    # Ball collision with bricks
    hit_index = ball.collidelist(bricks)
    if hit_index != -1:
        del bricks[hit_index]
        ball_speed[1] *= -1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
