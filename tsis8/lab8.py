import pygame
import random

pygame.init()

SCREEN_WIDTH = 600 # Размеры экрана
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255) # белый цвет

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Инициализация экрана
pygame.display.set_caption("Moving Background")

background_layer1 = pygame.transform.scale(pygame.image.load("background_layer1.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
background_layer2 = pygame.transform.scale(pygame.image.load("background_layer2.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
background_layer3 = pygame.transform.scale(pygame.image.load("background_layer3.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))

background_layers = [
    {"image": pygame.image.load("background_layer1.png"), "speed": 1.5}, # Фоновые слои с разной скоростью прокрутки
    {"image": pygame.image.load("background_layer2.png"), "speed": 2},
    {"image": pygame.image.load("background_layer3.png"), "speed": 0.1}
]


class Star: # Динамичные фоновые элементы
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.size = random.randint(1, 3)
        self.color = (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)

stars = [Star() for _ in range(100)]

clock = pygame.time.Clock() # Прокручиваем цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE) #Очищаем экран от предыдущего кадра
    
   
    for layer in background_layers: # Обрисовываем фоновые слои с параллакс-прокруткой
        layer_x = -((layer["speed"] * pygame.time.get_ticks()) % layer["image"].get_width())
        screen.blit(layer["image"], (layer_x, 0))
    
    for star in stars: # Рисуем динамические фоновые элементы 
        star.draw()
    
    pygame.display.flip() #Обновляем экран

    clock.tick(60)  # Ставим ограничение частоты кадров

pygame.quit() #Выход с Pygame
