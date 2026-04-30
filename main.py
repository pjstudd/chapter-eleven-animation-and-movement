import pygame
import sys

pygame.init()

# Window setup
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animation and Movement")

# Clock for frame rate
clock = pygame.time.Clock()
fps = 60

# Player setup
player = pygame.Rect(100, 100, 50, 50)
speed = 5

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= speed
    if keys[pygame.K_RIGHT]:
        player.x += speed
    if keys[pygame.K_UP]:
        player.y -= speed
    if keys[pygame.K_DOWN]:
        player.y += speed

    # Boundary detection
    if player.left < 0:
        player.left = 0
    if player.right > width:
        player.right = width
    if player.top < 0:
        player.top = 0
    if player.bottom > height:
        player.bottom = height

    # Drawing
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player)

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
sys.exit()