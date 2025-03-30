# First task: Extend example project from Lab 8 and add following tasks: Extra tasks to the given tutorial: 1. Randomly generating coins with different weights on the road 2.
# Increase the speed of Enemy when the player earns N coins 3. Comment your code

import pygame
import random

pygame.init()  # Initialize PyGame

WIDTH, HEIGHT = 800, 600  # The width and height of the display.
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Creating the display
pygame.display.set_caption("Racer Game")  # The name of the display

WHITE = (255, 255, 255)  # Background color
GREEN = (0, 200, 0)  # Color of the my car
RED = (200, 0, 0)  # Color of the enemy's car
GOLD = (255, 215, 0)  # Color of the small coin.
BIG_GOLD = (255, 223, 0)  # Color of the big coin

clock = pygame.time.Clock()  # FPS parameter.
FPS = 60

car_width, car_height = 50, 80  # The parametrs of the car
car_x, car_y = WIDTH // 2, HEIGHT - car_height - 20
car_speed = 5

# Қарсылас (Enemy) параметрлері
enemy_width, enemy_height = 50, 80  # The parametrs of the enemy's car.
enemy_x = random.randint(100, WIDTH - 100)
enemy_y = -enemy_height
enemy_speed = 3  # The speed of the enemy's car

# Parameters of the coins
coin_width, coin_height = 30, 30  # Width and Height of the small coin
big_coin_width, big_coin_height = 50, 50  # Width and Height of the big coin
coin_x = random.randint(100, WIDTH - 100)
coin_y = -coin_height
big_coin_x = random.randint(100, WIDTH - 100)
big_coin_y = -big_coin_height
coin_speed = 3
big_coin_speed = 3
coin_value = random.randint(1, 5)
big_coin_value = 10

# Indicator of the game
score = 0
level = 1

# Loop of the Game
running = True
while running:
    screen.fill(WHITE)  # Background color

    for event in pygame.event.get():  # If user push button X, then game is over.
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()  # Pushing the button for a long time
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    # Actions of the enemy's car
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -enemy_height
        enemy_x = random.randint(100, WIDTH - 100)

    # Actions of the coin
    coin_y += coin_speed
    if coin_y > HEIGHT:
        coin_y = -coin_height
        coin_x = random.randint(100, WIDTH - 100)
        coin_value = random.randint(1, 5)

    # Action of the big coin.
    big_coin_y += big_coin_speed
    if big_coin_y > HEIGHT:
        big_coin_y = -big_coin_height
        big_coin_x = random.randint(100, WIDTH - 100)

    # C ollecting the coin
    if (car_x < coin_x + coin_width and car_x + car_width > coin_x and
            car_y < coin_y + coin_height and car_y + car_height > coin_y):
        score += coin_value
        coin_y = -coin_height
        coin_x = random.randint(100, WIDTH - 100)

    # Collecting the big coin
    if (car_x < big_coin_x + big_coin_width and car_x + car_width > big_coin_x and
            car_y < big_coin_y + big_coin_height and car_y + car_height > big_coin_y):
        score += big_coin_value
        big_coin_y = -big_coin_height
        big_coin_x = random.randint(100, WIDTH - 100)

    # If my car will collision with enemy's car, then game is over
    if (car_x < enemy_x + enemy_width and car_x + car_width > enemy_x and
            car_y < enemy_y + enemy_height and car_y + car_height > enemy_y):
        running = False

    # If score is greater than level, then enemy will be faster
    if score >= level * 10:
        level += 1
        enemy_speed += 1

    # Drawing the car (rectangle)
    pygame.draw.rect(screen, GREEN, (car_x, car_y, car_width, car_height))

    # Drawing the enemy's car (rectangle)
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))

    # Drawing the coin (circle)
    pygame.draw.circle(screen, GOLD, (coin_x + coin_width // 2, coin_y + coin_height // 2), coin_width // 2)

    # Drawing the big coin (circle)
    pygame.draw.circle(screen, BIG_GOLD, (big_coin_x + big_coin_width // 2, big_coin_y + big_coin_height // 2),
                       big_coin_width // 2)

    # Printing the results of the game on screen.
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    level_text = font.render(f"Level: {level}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()