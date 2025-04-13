import pygame
import random

pygame.init()  # Инициализация Pygame


WIDTH, HEIGHT = 800, 600  # Ширина и высота окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Создание окна
pygame.display.set_caption("Racer Game")  # Установка названия окна

# Цвета
WHITE = (255, 255, 255)  # Цвет фона (белый)
GREEN = (0, 200, 0)  # Цвет машины игрока
RED = (200, 0, 0)  # Цвет машины-противника
GOLD = (255, 215, 0)  # Цвет маленькой монеты
BIG_GOLD = (255, 223, 0)  # Цвет большой монеты

clock = pygame.time.Clock()  # Настройка таймера
FPS = 60  # Количество кадров в секунду

# Параметры машины игрока
car_width, car_height = 50, 80
car_x = WIDTH // 2
car_y = HEIGHT - car_height - 20
car_speed = 5

# Параметры машины-противника
enemy_width, enemy_height = 50, 80
enemy_x = random.randint(100, WIDTH - 100)
enemy_y = -enemy_height
enemy_speed = 3  # Начальная скорость врага

# Параметры монет
coin_width, coin_height = 30, 30  # Маленькая монета
big_coin_width, big_coin_height = 50, 50  # Большая монета

coin_x = random.randint(100, WIDTH - 100)
coin_y = -coin_height
big_coin_x = random.randint(100, WIDTH - 100)
big_coin_y = -big_coin_height

coin_speed = 3
big_coin_speed = 3

coin_value = random.randint(1, 5)  # Случайная "стоимость" маленькой монеты
big_coin_value = 10  # Фиксированная "стоимость" большой монеты

# Показатели игры
score = 0  # Количество очков
level = 1  # Уровень

# Главный игровой цикл
running = True
while running:
    screen.fill(WHITE)  # Отрисовка фона

    # Обработка событий (например, выход из игры)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление машиной игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    # Движение машины-противника
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -enemy_height
        enemy_x = random.randint(100, WIDTH - 100)

    # Движение маленькой монеты
    coin_y += coin_speed
    if coin_y > HEIGHT:
        coin_y = -coin_height
        coin_x = random.randint(100, WIDTH - 100)
        coin_value = random.randint(1, 5)  # Случайное значение при повторном появлении

    # Движение большой монеты
    big_coin_y += big_coin_speed
    if big_coin_y > HEIGHT:
        big_coin_y = -big_coin_height
        big_coin_x = random.randint(100, WIDTH - 100)

    # Сбор маленькой монеты
    if (car_x < coin_x + coin_width and car_x + car_width > coin_x and
            car_y < coin_y + coin_height and car_y + car_height > coin_y):
        score += coin_value
        coin_y = -coin_height
        coin_x = random.randint(100, WIDTH - 100)

    # Сбор большой монеты
    if (car_x < big_coin_x + big_coin_width and car_x + car_width > big_coin_x and
            car_y < big_coin_y + big_coin_height and car_y + car_height > big_coin_y):
        score += big_coin_value
        big_coin_y = -big_coin_height
        big_coin_x = random.randint(100, WIDTH - 100)

    # Столкновение с машиной-противником — игра заканчивается
    if (car_x < enemy_x + enemy_width and car_x + car_width > enemy_x and
            car_y < enemy_y + enemy_height and car_y + car_height > enemy_y):
        running = False

    # Повышение уровня и увеличение скорости врага
    if score >= level * 10:
        level += 1
        enemy_speed += 1

    # Отрисовка машины игрока
    pygame.draw.rect(screen, GREEN, (car_x, car_y, car_width, car_height))

    # Отрисовка машины-противника
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))

    # Отрисовка маленькой монеты
    pygame.draw.circle(screen, GOLD, (coin_x + coin_width // 2, coin_y + coin_height // 2), coin_width // 2)

    # Отрисовка большой монеты
    pygame.draw.circle(screen, BIG_GOLD, (big_coin_x + big_coin_width // 2, big_coin_y + big_coin_height // 2),
                       big_coin_width // 2)

    # Отображение счёта и уровня на экране
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Очки: {score}", True, (0, 0, 0))
    level_text = font.render(f"Уровень: {level}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.update()  # Обновление экрана
    clock.tick(FPS)  # Контроль скорости игры

pygame.quit()  # Завершение игры