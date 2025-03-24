#Third task: Painter

import pygame
pygame.init() #Pygame-діинициализациялау. 

WIDTH, HEIGHT = 800, 600 #Экран, дисплейдің өлшемдері. Ені: 800, Биіктігі: 600
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Терезені құру. 
pygame.display.set_caption("Simple Paint in Pygame") #Терезенің атауы. 

# Түстер
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Бастапқы түс - қара
current_color = BLACK

# Экранды ақ түске келтіру. 
screen.fill(WHITE)

running = True
shape = "circle"  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  #Егер экрандағы Х батырмасын басса, экран жабылады. 
            running = False
        
        elif event.type == pygame.KEYDOWN:  #Клавиатураның батырмасын басу шарты. 
            if event.key == pygame.K_r:  # Егер 'R' басса - төртбұрыш
                shape = "rect"
            elif event.key == pygame.K_c:  # Егер 'C' басса - шеңбер
                shape = "circle"
            elif event.key == pygame.K_e:  # Егер 'E' басса - өшіргіш
                shape = "eraser"
            elif event.key == pygame.K_1:  #Қара түс
                current_color = BLACK
            elif event.key == pygame.K_2:  #Қызыл түс
                current_color = RED
            elif event.key == pygame.K_3:  #Көк түс
                current_color = BLUE
            elif event.key == pygame.K_4:  #Жасыл түс
                current_color = GREEN

        elif event.type == pygame.MOUSEBUTTONDOWN:  # Егер тінтуір басылса
            x, y = event.pos  # Тінтуірдің координатасын аламыз
            if shape == "circle":  # Егер фигура - шеңбер болса
                pygame.draw.circle(screen, current_color, (x, y), 20)
            elif shape == "rect":  # Егер фигура - төртбұрыш болса
                pygame.draw.rect(screen, current_color, (x, y, 40, 40))
            elif shape == "eraser":  # Егер өшіргіш қосылса
                pygame.draw.circle(screen, WHITE, (x, y), 20)
    
    pygame.display.update()  # Экранды жаңарту.

pygame.quit()  # Pygame-ді жабу.
