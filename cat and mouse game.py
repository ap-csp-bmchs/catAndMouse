import pygame
import random
pygame.init()
from pygame.locals import *
from random import randint

display_width = 1000
display_heigth = 800
gameDisplay = pygame.display.set_mode((display_width, display_heigth))

pygame.display.set_caption('Cat & Mouse')
clock = pygame.time.Clock()

catImage = pygame.image.load('cat.png')

#define color RGB
white = (255, 255, 255)
black = (0, 0, 0)
olive_green = (79, 89, 55)
'''
cat
'''
#this put the cat in the middle of the screen
x = (display_width * 0.45) 
y = (display_heigth * 0.45)
cat_startx = (display_width * 0.45)
cat_starty = (display_heigth * 0.45)


#this will help move the cat
x_change = 0
y_change = 0

#this is how big the cat is
cat_width = 99
cat_height = 99

#this plus x_change or y_change move the cat
new_x = 0
new_y = 0

#this function appear the cat on the screen
def cat(x,y):#blith mean add to 
    gameDisplay.blit(catImage, (x,y)) 

'''
Make a mouse
'''
mouseImage = pygame.image.load('mouse.png')
#this put the mouse in the middle of the screen
a = (display_width * 0.5)
b = (display_heigth * 0.5)
mouse_startx = (display_width * 0.7)
mouse_starty = (display_heigth * 0.7)

#this will help move the mouse
ac = 0
bc = 0

#this is how big the cat is
mouse_width = 90
mouse_height = 85

#this plus x_change or y_change move the cat
na = 0
nb = 0
#this function appear the cat on the screen
def mouse(a,b):#blith mean add to 
    gameDisplay.blit(mouseImage, (a,b)) 
na = (random.randint(0,(1000-mouse_width)))
nb = (random.randint(0,(800-mouse_height)))


#game loop
game_over = False
while game_over == False:
    
#set up quit when user clicks the 'x'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

#set up key press definitions
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

        #this help mouse to move
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                ac = -5
                    
            elif event.key == pygame.K_d:
                ac = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                ac = 0
                

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                bc = -5
            elif event.key == pygame.K_s:
                bc = +5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                bc = 0

#set up x & y change to stay within window boundaries
    new_x = x + x_change
    if new_x >=0 and new_x <= display_width - cat_width:
        x += x_change

    new_y = y + y_change
    if new_y >= 0 and new_y <= display_heigth - cat_height:
        y += y_change
#set up a & b change to stay within window boundaries
    na = a + ac
    if na >=0 and na <= display_width - mouse_width:
        a += ac

    nb = b + bc
    if nb >= 0 and nb <= display_heigth - mouse_height:
        b += bc
#test cat touch mouse

    CatRect = pygame.Rect(x, y, cat_width, cat_height)
    MouseRect = pygame.Rect(a, b, mouse_width, mouse_height)

    if CatRect.colliderect(MouseRect):
        x = cat_startx
        y = cat_starty
        a = mouse_startx
        b = mouse_starty


    #draw the frame
    gameDisplay.fill(olive_green)
    cat(x,y)
    mouse(a,b)
    pygame.display.flip()
#set up fps
    clock.tick(60)






pygame.quit()


