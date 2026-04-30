# Chapter 11: Animation and Movement (Pygame)

## Overview
This chapter focuses on how to create **movement and animation** in Pygame. You will learn how objects move, how smooth animation is achieved using frame rate control, how to use images (sprites), and how to prevent objects from going outside the game window.

---

## Intended Learning Outcomes
After completing this chapter, you should be able to:
- Develop motion logic to create smooth and time-based object animation.
- Implement boundary checking to keep objects within the game window.
- Utilize sprite sheets or image sequences for basic visual animation.

---

## 11.1 Updating Object Positions (Motion Logic)

### Discussion
Motion in games is created by continuously updating the position of an object inside the game loop.

Instead of keeping an object in one place, its position (x and y coordinates) is changed every frame. This creates the illusion of movement.

### Key Idea
- Movement = changing position over time.
- Position updates happen inside the game loop.
- Speed determines how fast the object moves.

---

## 11.2 Frame Rate and Smooth Animation

### Discussion
The **frame rate (FPS - Frames Per Second)** controls how often the screen updates.

- Higher FPS → smoother animation  
- Lower FPS → choppy or laggy movement  

To ensure smooth animation, the game must maintain a consistent frame rate using a timing mechanism (clock).

### Key Idea
- Frame rate keeps animation consistent.
- A fixed FPS ensures smooth and predictable movement.
- Motion should be tied to time, not just frame count.

---

## 11.3 Sprite Basics and Image Movement

### Discussion
A **sprite** is an image or visual representation of an object in a game (e.g., player, enemy, item).

Sprites can:
- Be static (single image)
- Be animated (multiple images or sprite sheets)

Animating a sprite involves switching between images quickly to create motion.

### Key Idea
- Sprites make the game visually interactive.
- Image position is updated the same way as basic shapes.
- Animation can be done using image sequences.

---

## 11.4 Implementing Boundary Detection

### Discussion
Boundary detection ensures that objects **stay inside the game window**.

Without boundary checking:
- Objects may move off-screen
- Gameplay becomes unpredictable

This is done by limiting the object's position within the screen dimensions.

### Key Idea
- Prevent object from going beyond screen limits.
- Check position before or after movement.
- Adjust position if it exceeds boundaries.

---

## Example: Basic Animation, Movement, and Boundary Detection

Below is an example demonstrating:
- Motion logic
- Frame rate control
- Sprite (rectangle placeholder)
- Boundary detection

```python
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