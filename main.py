
import pygame
import time
import random

pygame.init()

win = pygame.display.set_mode((500, 500))

x1 = 100
y1 = 150

x2 = 100
y2 = 100

white = (255, 255, 255)
black = (0, 0, 0)
width = 15
height = 15

x1_change = 0
y1_change = 0

snake_block = 15

Score = 0

length_snake = 1
snake_List = []

def snake(snake_piece, snake_List):
     for x in snake_List:
        pygame.draw.rect(win, [255, 0, 0], [x[0], x[1], snake_block, snake_block])


running = True
game_over = False
game_close = False

clock = pygame.time.Clock()


while running:

    '''while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_close = True
                    game_over = False
                    '''

    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -5
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 5
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -5
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 5
                x1_change = 0

    x1 += x1_change
    y1 += y1_change
    win.fill(black)
    win_surface = pygame.display.set_mode((500, 500))
    font = pygame.font.Font('freesansbold.ttf', 20)
    scoretxt = font.render("Score: " + str(Score), True, white)

    textRect = scoretxt.get_rect()
    textRect.center = (50, 30)

    player = pygame.draw.rect(win, (255, 0 ,0), [x1, y1, width, height])
    apple = pygame.draw.rect(win, (55, 89, 255), [x2, y2, width + 10, height + 10])
    snake_piece = []
    snake_piece.append(x1)
    snake_piece.append(y1)
    snake_List.append(snake_piece)

    if len(snake_List) > length_snake:
        del snake_List[0]

    snake(snake_block, snake_List)


    #Text
    win_surface.blit(scoretxt, textRect)

    #Rand apple move
    if player.colliderect(apple):
        x2 = random.randint(0,400)
        y2 = random.randint(0,400)

    # Score
    if player.colliderect(apple):
        Score += 1
        length_snake += 5


    #Border detection
    if x1 >= 470 and pygame.K_RIGHT:
        pygame.QUIT()
        quit()
    elif x1 <= 3 and pygame.K_LEFT:
        pygame.QUIT()
        quit()
    elif y1 >= 490 and pygame.K_DOWN:
        pygame.QUIT()
        quit()
    elif y1 <= 3 and pygame.K_UP:
        pygame.QUIT()
        quit()

    pygame.display.update()


    clock.tick(30)

pygame.quit()
quit()



