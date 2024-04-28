import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Background")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Background layers
background_layers = [
    pygame.image.load("background_layer1.png"),  # Add your own background images
    pygame.image.load("background_layer2.png"),
    pygame.image.load("background_layer3.png"),
]

# Parallax scrolling speeds for each layer
scroll_speeds = [0.1, 0.3, 0.5]

# Clouds (procedurally generated)
clouds = []
for _ in range(20):
    cloud_x = random.randint(0, WIDTH)
    cloud_y = random.randint(50, 200)
    clouds.append((cloud_x, cloud_y))

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Scroll background layers
    for i, layer in enumerate(background_layers):
        layer_x = -scroll_speeds[i] * pygame.time.get_ticks() % layer.get_width()
        screen.blit(layer, (layer_x, 0))

    # Draw clouds
    for cloud in clouds:
        cloud_x, cloud_y = cloud
        cloud_x += 1  # Move clouds to the right
        if cloud_x > WIDTH:
            cloud_x = -50
        pygame.draw.circle(screen, WHITE, (cloud_x, cloud_y), 20)

    pygame.display.flip()

# Clean up
pygame.quit()
