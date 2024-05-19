import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

# Colors
BLUE = (50, 10, 255)
qq=0
# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("HELLinCopter")

# Load background layers and resize them
background_layer1 = pygame.transform.scale(pygame.image.load("background_layer1.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
background_layer2 = pygame.transform.scale(pygame.image.load("background_layer2.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
background_layer3 = pygame.transform.scale(pygame.image.load("plane.png"), (SCREEN_WIDTH/3.5, SCREEN_HEIGHT/6))

# Background layers with speeds
background_layers = [
    {"image": background_layer1, "speed": 0.3},
    {"image": background_layer2, "speed": 0.4}
]
pp = {"image": background_layer3, "speed": 0.2}

# Helicopter settings
HELICOPTER_WIDTH = 200
HELICOPTER_HEIGHT = 130
helicopter_img = pygame.image.load("heli.png")  # Replace with your helicopter image
helicopter_img = pygame.transform.scale(helicopter_img, (HELICOPTER_WIDTH, HELICOPTER_HEIGHT))

class Helicopter:
    def __init__(self):
        self.x = 100
        self.y = SCREEN_HEIGHT // 2
        self.speed = 10
        self.image = helicopter_img.get_rect(topleft=(self.x, self.y))

    def move(self, dx, dy):
        self.image.x += dx
        self.image.y += dy

    def draw(self):
        screen.blit(helicopter_img, self.image.topleft)

# Star class for dynamic background elements
class Star:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.size = random.randint(1, 3)
        self.color = (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

# Load sound effect for stars
sound = pygame.mixer.Sound("sound1.wav") 

# Create stars
stars = [Star() for _ in range(100)]

# Game loop
clock = pygame.time.Clock()
running = True
helicopter = Helicopter()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle WASD input for helicopter movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        helicopter.move(0, -helicopter.speed)
        helicopter.y-=helicopter.speed
    if keys[pygame.K_s]:
        helicopter.move(0, helicopter.speed)
        helicopter.y+=helicopter.speed
    if keys[pygame.K_a]:
        helicopter.move(-helicopter.speed, 0)
        helicopter.x-=helicopter.speed
    if keys[pygame.K_d]:
        helicopter.move(helicopter.speed, 0)
        helicopter.x+=helicopter.speed

    # Clear the screen
    screen.fill(BLUE)

    # Draw background layers with parallax scrolling
    for layer in background_layers:
        layer_x = -((layer["speed"] * pygame.time.get_ticks()) % SCREEN_WIDTH)
        screen.blit(layer["image"], (layer_x, 0))
        if layer_x < 0:
            screen.blit(layer["image"], (layer_x + SCREEN_WIDTH, 0))

    layer_y = -((-pp["speed"] * pygame.time.get_ticks()) % (SCREEN_WIDTH/3-2000))
    sound.play()
    if layer_y >1500:
        qq=random.randint(0,500)
    screen.blit(pp["image"], (layer_y-500, qq))
    
    # Draw stars
    for star in stars:
        star.draw()
        
    #pygame.draw.rect(screen,(250,21,34),(helicopter.x,helicopter.y,200,100))
    if helicopter.x+200>=layer_y-500 and helicopter.x<=layer_y-200 and helicopter.y+100>=qq+100 and helicopter.y+40<=qq+150:
        running=False
    # Draw helicopter
    helicopter.draw()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
