
import pygame
import button
import random

pygame.init()

win = pygame.display.set_mode((500, 500))

x1 = 100
y1 = 150

x2 = 100
y2 = 100

mouse_pos = pygame.mouse.get_pressed()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (195, 231, 246)
red = (255, 0, 0)
width = 15
height = 15


x1_change = 0
y1_change = 0

game_over = False


snake_block = 15

game_over_font = pygame.font.Font('freesansbold.ttf', 60)
Score = 0

length_snake = 1
snake_List = []

def snake(snake_piece, snake_List):
     for x in snake_List:
        pygame.draw.rect(win, [255, 0, 0], [x[0], x[1], snake_block, snake_block])

def game_over():
    global gameover
    length_snake = 0
    x1 = 0
    y1 = 0
    x1_change = 0
    y1_change = 0
    win.fill(blue)
    display_gameover = game_over_font.render("GAME OVER!", True, red, black)
    win.blit(display_gameover, (50, 150))
    display_restart = font.render("Press space to restart", True, white, black)
    win.blit(display_restart, (150, 250))
    gameover = True


running = True

clock = pygame.time.Clock()


while running:

    win.fill(black)

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE and gameover:
                pygame.display.update()
                x1 = 100
                y1 = 150
                x1_change = 0
                y1_change = 0
                length_snake = 1
                Score = 0
                x2 = 100
                y2 = 100
                gameover = False






    x1 += x1_change
    y1 += y1_change
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

    for x in snake_List[:-1]:
        if x == snake_piece:
            game_over()

    snake(snake_block, snake_List)


    #Text
    win_surface.blit(scoretxt, textRect)

    #Rand apple move
    if player.colliderect(apple):
        x2 = random.randint(0,400)
        y2 = random.randint(0,400)

    #Score
    if player.colliderect(apple):
        Score += 1
        length_snake += 2

    # Border detection

    if x1 >= 470 and pygame.K_RIGHT:
            game_over()

    elif x1 <= 3 and pygame.K_LEFT:
            game_over()

    elif y1 >= 490 and pygame.K_DOWN:
            game_over()

    elif y1 <= 3 and pygame.K_UP:
            game_over()



    pygame.display.update()


    clock.tick(30)

pygame.quit()
quit()



