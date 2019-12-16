import pygame
import random
pygame.init()

display_width = 900
display_height = 800
Surface = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Cat & Ice cream')
clock = pygame.time.Clock()

catImg = pygame.image.load('cat.png')
ice_cream = pygame.image.load('food.png')

lavender = (230, 230, 250)




x = (display_width * 0.4)
y = (display_height * 0.4)
startx = (display_width * 0.4)
starty = (display_height * 0.4)
x_change = 0
y_change = 0
cat_width = 50
cat_height = 50
new_x = 0
new_y = 0



icecream_width = 10
icecream_height = 10
nx = (random.randint(0,(1000-icecream_width)))
ny = (random.randint(0,(800-icecream_height)))
startnx = 0
startny = 0
nx_change = 0
ny_change = 0
new_nx = 0
new_ny = 0



def cat(x,y):
    Surface.blit(catImg, (x,y))


def icecream(nx,ny):
    Surface.blit(ice_cream, (nx,ny))







    #game_over = False
    #while game_over == False:
    
#game loop
running = True
while running:


#code for Cat to move
    
#set up quit when user clicks the 'x'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

#code for Icecream to move
        if event.type == pygame. KEYDOWN:
            if event.key == pygame.K_a:
                nx_change = -5

            elif event.key == pygame.K_d:
                nx_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                nx_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ny_change = -5
            elif event.key == pygame.K_s:
                ny_change = +5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                ny_change = 0
        
        



#set up x & y change to stay within window boundaries
    new_x = x + x_change
    if new_x >=0 and new_x <= display_width - cat_width:
        x += x_change

    new_y = y + y_change
    if new_y >= 0 and new_y <= display_height - cat_height:
        y += y_change

#set up nx & ny change to stay within window boundaries
    new_nx = nx + nx_change
    if new_nx >=0 and new_nx <= display_width - icecream_width:
        nx += nx_change

    new_ny = ny + ny_change
    if new_ny >= 0 and new_ny <= display_height - icecream_height:
        ny += ny_change



    catRect = pygame.Rect(x, y, cat_width, cat_height)
    icecreamRect = pygame.Rect(nx, ny, icecream_width, cat_height)
    if catRect.colliderect(icecreamRect):
        x = startx
        y = starty
        nx = startnx
        ny = startny



#draw the frame
    Surface.fill(lavender)
    cat(x,y)
    icecream(nx,ny)
    pygame.display.flip()
    
#set up fps
    clock.tick(60)


pygame.quit()





        


        
