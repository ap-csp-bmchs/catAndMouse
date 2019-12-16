import pygame
import random
pygame.init()

display_width = 1000
display_height = 800
gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Cat and Mouse')
clock = pygame.time.Clock()

catImg = pygame.image.load('black_cat.png')

mouseImg = pygame.image.load('jerry.png')

white = (255, 255, 255)
black = (0, 0, 0)


def cat(x,y):
    gameDisplay.blit(catImg, (x,y))

def mouse(mx,my):
    gameDisplay.blit(mouseImg, (mx,my))

x_change = 0
y_change = 0
mx_change = 0
my_change = 0
mouse_width = 76
mouse_height = 76
new_mx = 0
new_my = 0

cat_width = 140
cat_height = 55
new_x = 0
new_y = 0

cat_startx = (display_width * 0.45)
cat_starty = (display_width * 0.45)
mouse_startmx = (display_width * 0.6)
mouse_startmy = (display_width * 0.6)
x = (display_width * 0.45)
y = (display_height * 0.45)
mx = (random.randint(0, (mouse_width-76)))
my = (random.randint(0, (mouse_height-76)))

def mouse(mx,my):
    gameDisplay.blit(mouseImg, (mx,my))



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

    new_mx = mx+ mx_change
    if new_mx >=0 and new_mx <= display_width - mouse_width:
        mx += mx_change

    new_my = my + my_change
    if new_my >=0 and new_my <= display_height - mouse_height:
        my += my_change

    catRect = pygame.Rect(x, y, cat_width, cat_height)
    mouseRect = pygame.Rect(mx, my, mouse_width, mouse_height)
    if catRect.colliderect(mouseRect):
        x = cat_startx
        y = cat_starty
        mx = mouse_startmx
        my = mouse_startmy
        
    gameDisplay.fill(white)
    cat(x,y)
    mouse(mx,my)
    pygame.display.flip()

    clock.tick(60)


pygame.quit()
        

            

