import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400  # THE WIDTH AND HEIGHT OF THE DISPLAY
CELL_SIZE = 20  # THE CIZE OF THE FOOD
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Created the display
pygame.display.set_caption("Snake Game")  # The name of the display

WHITE = (255, 255, 255)  # WHITE background color
GREEN = (0, 255, 0)  # Green color of the snake
RED = (255, 0, 0)  # Red color of the food
BLACK = (0, 0, 0)  # The parameter of the indicator

snake = [(100, 100)]
snake_dir = (CELL_SIZE, 0)
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
food_size = random.choice([CELL_SIZE, CELL_SIZE * 2])  # Random cize of the food.
food_timer = 100  # Timer of losing food.
score = 0  # The score of the gamer
level = 1  # The level of the gamer
speed = 10  # The speed of the game

running = True
clock = pygame.time.Clock()  #

while running:
    screen.fill(WHITE)  # Background color of the screen

    for event in pygame.event.get():  # If user will push button X,
        if event.type == pygame.QUIT:  # then game will be over.
            running = False

        elif event.type == pygame.KEYDOWN:  # If user push button KEYDOWN,
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):  # Up
                snake_dir = (0, -CELL_SIZE)
            if event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):  # Down
                snake_dir = (0, CELL_SIZE)
            if event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):  # Left
                snake_dir = (-CELL_SIZE, 0)
            if event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):  # Right
                snake_dir = (CELL_SIZE, 0)

    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])

    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake:
        running = False  # If snake hits the screen, then game will stop.
        break

    snake.insert(0, new_head)

    if new_head[0] < food[0] + food_size and new_head[0] + CELL_SIZE > food[0] and \
            new_head[1] < food[1] + food_size and new_head[1] + CELL_SIZE > food[1]:
        score += food_size // CELL_SIZE  # Adding points because of the cize of foods.
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        food_size = random.choice([CELL_SIZE, CELL_SIZE * 2])
        food_timer = 100  # Update of the timer
        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    food_timer -= 1
    if food_timer <= 0:
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        food_size = random.choice([CELL_SIZE, CELL_SIZE * 2])
        food_timer = 100

    pygame.draw.rect(screen, RED, (food[0], food[1], food_size, food_size))

    for part in snake:
        pygame.draw.rect(screen, GREEN, (part[0], part[1], CELL_SIZE, CELL_SIZE))

    font = pygame.font.Font(None, 30)
    text = font.render(f"Score: {score}  Level: {level}", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(speed)

pygame.quit()