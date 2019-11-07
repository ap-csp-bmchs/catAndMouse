import pygame
import random
pygame.init()

display_width = 1000
display_height = 800
gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Cat N Mouse')
clock = pygame.time.Clock()

catImg = pygame.image.load('cat.png')
mouseImg = pygame.image.load('mouse.png')
cheeseImg = pygame.image.load('cheese.png')

white = (255, 255, 255)
black = (0, 0, 0)

cat_width = 131
cat_height = 75
mouse_width = 38
mouse_height = 25
cheese_width = 35
cheese_height = 34

#cat starting point info
x = (50)
y = (display_height - cat_height*2)
#mouse starting point info
mx = (display_width - mouse_width)
my = 0
#cheese starting point info
cx = 0
cy = display_height - cheese_height

#cat location change variables
x_change = 0
y_change = 0
new_x = 0
new_y = 0

#mouse location change variables
mx_change = 0
my_change = 0
new_mx = 0
new_my = 0

#image rectangles
catRect = catImg.get_rect()
mouseRect = mouseImg.get_rect()
cheeseRect = cheeseImg.get_rect()

def cat(x,y):
    gameDisplay.blit(catImg, (x,y))

def mouse(mx,my):
    gameDisplay.blit(mouseImg, (mx,my))

def cheese(cx,cy):
    gameDisplay.blit(cheeseImg, (cx,cy))

#game loop
game_over = False
while game_over == False:
    
#set up quit when user clicks the 'x'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

#set up key press definitions for controlling the cat
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
                    
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
                #x += x_change

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = +5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0


#set up key press definitions for controlling the mouse
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
        

#set up x & y change of cat to stay within window boundaries
    new_x = x + x_change
    if new_x >=0 and new_x <= display_width - cat_width:
        x += x_change

    new_y = y + y_change
    if new_y >= 0 and new_y <= display_height - cat_height:
        y += y_change

#set up x & y change of mouse to stay within window boundaries
    new_mx = mx + mx_change
    if new_mx >=0 and new_mx <= display_width - mouse_width:
        mx += mx_change

    new_my = my + my_change
    if new_my >= 0 and new_my <= display_height - mouse_height:
        my += my_change

#set up when cat touches mouse sensing
    #if catRect.colliderect(mouseRect):
        

    


        

#draw the frame
    gameDisplay.fill(white)
    cat(x,y)
    mouse(mx,my)
    cheese(cx,cy)
    pygame.display.flip()
#set up fps
    clock.tick(60)


pygame.quit()
        

            
