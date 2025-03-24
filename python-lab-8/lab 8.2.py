#Second task: Snake game!

import pygame
import random

pygame.init()  # Pygame-ді инициализациялау. 
WIDTH, HEIGHT = 600, 400  # Экранның өлшемдері. Биіктігі және ені 
CELL_SIZE = 20  # Жылан мен тамақтың өлшемі
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Экран құру. 
pygame.display.set_caption("Snake Game") # Экранның атауын беру. 

# Түстер
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


snake = [(100, 100)]  # Жыланның бастапқы орны
snake_dir = (CELL_SIZE, 0)  # Оңға қарай қозғалады
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
score = 0
level = 1
speed = 10

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE) #Экранды ақ түске боядық. 
    
    # Оқиғалармен жұмыс жасау. 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Егер экрандағы Х батырмасы басылса, код өз жұмысын тоқтатады. 
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                snake_dir = (0, -CELL_SIZE)
            if event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                snake_dir = (0, CELL_SIZE)
            if event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                snake_dir = (-CELL_SIZE, 0)
            if event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                snake_dir = (CELL_SIZE, 0)
    
    # Жыланды жылжыту
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    # Шекарадан шықпауын қамтамасыз ету керек. 
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake:
        running = False
        break
    
    snake.insert(0, new_head)
    
    # Тамақты жеу
    if new_head == food:
        score += 1
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        if score % 4 == 0:
            level += 1
            speed += 2  # Жылдамдықты арттыру
    else:
        snake.pop()
    
    # Тамақты экранға шығару
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))
    
    # Жыланды экранға шығару
    for part in snake:
        pygame.draw.rect(screen, GREEN, (part[0], part[1], CELL_SIZE, CELL_SIZE))
    
    font = pygame.font.Font(None, 30)
    text = font.render(f"Score: {score}  Level: {level}", True, BLACK)
    screen.blit(text, (10, 10))
    
    pygame.display.update() # Экранды жаңарту. 
    clock.tick(speed) 

pygame.quit() # Pygame операциясын аяқтау. 
