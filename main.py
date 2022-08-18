#Importing pygame module
import pygame

#importing sys module
import sys

#Initalizing pygame
pygame.init()

#Creating window
window = pygame.display.set_mode((800,600))

#Var
color = [255, 0, 0]
x = 100
y =100

#sdsasadas
player = pygame.draw.rect(window, color, pygame.Rect(x, y, 25, 25))
pygame.display.flip()

#Active loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.K_ESCAPE:
            pygame.quit()
            sys.exist()



        if event.type == pygame.KEYDOWN:


            if event.key == pygame.K_a:
                print("Key a has been press")


            if event.key == pygame.K_j:
                print("Key j has been press")


            if event.key == pygame.K_p:
                print("Key p has been press")

            if event.key == pygame.K_b:
                print("Key b has bveen press")




