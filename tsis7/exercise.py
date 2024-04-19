import pygame

pygame.init() #инициализируем pygame

SCREEN_WIDTH = 700 #Настраиваем ширину и высоту экрана
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Scrolling Background")

background_image = pygame.image.load("background.jpg") #Загружаем фоновое изображение
background_rect = background_image.get_rect()

background_y = 0 #Устанавливаем начальную позицию фона

scroll_speed = 2 #Здесь устанавливаем скорость прокрутки

running = True #Этот код является основным циклом игры, который работает до тех пор, пока переменная running остается True
while running: # Внутри цикла происходит обработка всех событий, которые происходят в игре, таких как нажатия клавиш, движения мыши и т.д.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    background_y += scroll_speed #Прокручиваем фон

    if background_y >= background_rect.height: # Если фон доходит до нижней части экрана, сбрасываем его положение
        background_y = 0

    screen.blit(background_image, (0, background_y - background_rect.height))     # Рисуем фон
    screen.blit(background_image, (0, background_y))

    pygame.display.flip()   # Обновляем дисплей
    
    pygame.time.Clock().tick(60) # Устанавливаем частоту кадров

pygame.quit() #Выход с Pygame
exit()
