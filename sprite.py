import pygame
import random
from random import randint
pygame.display.init()
display_width = 1000
display_height = 800
surface = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tom And Jerry')
green = (0, 200,0 )
clock = pygame.time.Clock()

catImg = pygame.image.load('cat.png')
mouseImg = pygame.image.load('jerry1.png')

def Jerry(mx,my):
    surface.blit(mouseImg, (mx,my))

def tom(x,y):
    surface.blit(catImg, (x,y))

x = (display_width * 0.45)
y = (display_height * 0.45)
x_change = 0
y_change = 0
mx_change = 0
my_change = 0
mouse_width = 131
mouse_height = 110
new_mx = 0
new_my = 0
cat_startx = (display_width * 0.45)
cat_starty = (display_height * 0.45)
cat_width = 131
cat_height = 75
new_x = 0
new_y = 0
#code for jerry
mx = (random.randint(0,(1000-mouse_width)))
my = (random.randint(0,(800-mouse_height)))
mouse_startmx = (random.randint(0,(1000-mouse_width)))
mouse_startmy = (random.randint(0,(1000-mouse_width)))
#catrect
catrect = pygame.Rect(x,y, cat_width, cat_height)
mouserect = pygame.Rect(mx,my, mouse_width, mouse_height)


    
#game loop
game_over = False
while game_over == False:
    #catrect.pygame.rect
#set up quit when hit X
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

#set up key press diorections
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5


            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
                x += x_change
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = +5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

    new_x = x + x_change
    if new_x >=0 and new_x <= display_width - cat_width:
        x += x_change

    new_y = y + y_change
    if new_y >= 0 and new_y <= display_height - cat_height:
        y += y_change
#set up for box
        catRect = pygame.Rect(x, y, cat_width, cat_height)
        mouseRect = pygame.Rect(mx, my, mouse_width, mouse_height)

        if catRect.colliderect(mouseRect):
            x = cat_startx
            y = cat_starty
            mx = mouse_startmx
            my = mouse_startmy
            



        
    surface.fill(green)
    tom(x,y)
    Jerry(mx,my)
    pygame.display.flip()
#jerry
    clock.tick(60)

pygame.quit()

#this code makes it to where you can control the cat and moved it around and has it to where the mouse
# spawns at radnom location and you can contrl the cat with the arrow keys


