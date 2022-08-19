
import pygame

import random

pygame.init()

win = pygame.display.set_mode((500, 500))

x = 200
y = 200

ox = 100
oy = 100

width = 20
height = 20

vel = 2

running = True

while running:

    pygame.time.delay(10)

    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    keys = pygame.key.get_pressed()

    #Player keeps moving


    if keys[pygame.K_LEFT] and x > 0:

        x -= vel


    if keys[pygame.K_RIGHT] and x < 500 - width:

        x += vel


    if keys[pygame.K_UP] and y > 0:

        y -= vel


    if keys[pygame.K_DOWN] and y < 500 - height:

        y += vel


    win.fill((0, 0, 0))


    pla = pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    app = pygame.draw.rect(win, (55, 89, 255), (ox, oy, width, height))

    random_coord = (random.uniform(0,500), random.uniform(0,500))


    if pla.colliderect(app):
        print("collision!")



    pygame.display.update()


pygame.quit()



