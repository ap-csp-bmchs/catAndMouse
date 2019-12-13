import pygame 
import random
from random import randint
pygame.init()

display_width = 800
display_height = 600
surface = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Cat N Mouse')
white = (255, 255, 255)
black = (0, 0, 0)
clock = pygame.time.Clock()

ImgTom = pygame.image.load('Tomcat.png')
ImgJerry = pygame.image.load('jerry.png')

x = (display_width * 0)
y = (display_height * 0)
cat_startx = (display_width * 0)
cat_starty = (display_height * 0)
x_change = 0
y_change = 0
cat_width = 131
cat_height = 110
new_x = 0
new_y = 0

mouse_width = 131
mouse_height = 110
mx = (random.randint(0,(800-mouse_width)))
my = (random.randint(0,(600-mouse_height)))
mouse_startmx = (random.randint(0,(800-mouse_width)))
mouse_startmy = (random.randint(0,(600-mouse_height)))
mx_change = 0
my_change = 0
new_mx = 0
new_my = 0



def Tom(x,y):
    surface.blit(ImgTom, (x,y))
def Jerry(mx,my):
    surface.blit(ImgJerry, (mx,my))

game_over = False
while game_over == False:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
                    
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
                

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = +5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

#This is to help Jerry move
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mx_change = -5
                    
            elif event.key == pygame.K_d:
                mx_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                mx_change = 0
                

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                my_change = -5
            elif event.key == pygame.K_s:
                my_change = +5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                my_change = 0
#get new cat coordinates if within window
    new_x = x + x_change
    if new_x >=0 and new_x <= display_width - cat_width:
        x += x_change

    new_y = y + y_change
    if new_y >= 0 and new_y <= display_height - cat_height:
        y += y_change
#get new mouse coordinates if within window
    new_mx = mx + mx_change
    if new_mx >=0 and new_mx <= display_width - mouse_width:
        mx += mx_change

    new_my = my + my_change
    if new_my >= 0 and new_my <= display_height - mouse_height:
        my += my_change
# checks position of the top left corner of Tom
    catRect = pygame.Rect(x, y, cat_width, cat_height)
    mouseRect = pygame.Rect(mx, my, mouse_width, cat_height)
    if catRect.colliderect(mouseRect):
       x = cat_startx
       y = cat_starty
       mx = mouse_startmx
       my = mouse_startmy

#Draws the new screen 
    surface.fill(white)
    Tom(x,y)
    Jerry(mx, my)
    pygame.display.flip()

    clock.tick(60)
    

    
    
    
pygame.quit()







