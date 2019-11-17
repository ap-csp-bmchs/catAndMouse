import pygame
import random
import time

pygame.init()

display_width = 1000
display_height = 800
gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Cat N Mouse')
clock = pygame.time.Clock()

catImg = pygame.image.load('cat.png')
mouseImg = pygame.image.load('mouse.png')
cheeseImg = pygame.image.load('cheese.png')
cScoreImg = pygame.image.load('cScore.png')
mScoreImg = pygame.image.load('mScore.png')
catWinImg = pygame.image.load('big_cat.png')
mouseWinImg = pygame.image.load('big_mouse.png')
points = ['zero.png', 'one.png', 'two.png', 'three.png', 'four.png', 'five.png']
cpoint_count = 0
cpointsImg = pygame.image.load(points[0])
mpoint_count = 0
mpointsImg = pygame.image.load(points[0])



white = (255, 255, 255)
black = (0, 0, 0)

cat_width = 131
cat_height = 75
mouse_width = 38
mouse_height = 25
cheese_width = 35
cheese_height = 34
cScore_width = 206
cScore_height = 29
mScore_width = 206
mScore_height = 29

#cat starting point info
x = (50)
y = (display_height - cat_height*2)
catRect = pygame.Rect(x, y, cat_width, cat_height)
#mouse starting point info
mx = (display_width - mouse_width)
my = 0
mouseRect = pygame.Rect(mx, my, mouse_width, mouse_height)
#cheese starting point info
cx = 0
cy = display_height - cheese_height
cheeseRect = pygame.Rect(cx, cy, cheese_width, cheese_height)
#score location
sx = 0
sy = 0

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
#catRect = catImg.get_rect()
#mouseRect = mouseImg.get_rect()
#cheeseRect = cheeseImg.get_rect()

def cat(x,y):
    gameDisplay.blit(catImg, (x,y))

def mouse(mx,my):
    gameDisplay.blit(mouseImg, (mx,my))

def cheese(cx,cy):
    gameDisplay.blit(cheeseImg, (cx,cy))

#game loop
cat_win = False
mouse_win = False
game_over = False
while game_over == False:
    
#set up quit when user clicks the 'x'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

#set up key press definitions for controlling the cat
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if cpoint_count < mpoint_count:
                    x_change = -10
                else:
                    x_change = -5
                    
            elif event.key == pygame.K_RIGHT:
                if cpoint_count < mpoint_count:
                    x_change = 10
                else:
                    x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
                

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if cpoint_count < mpoint_count:
                    y_change = -10
                else:
                    y_change = -5
            elif event.key == pygame.K_DOWN:
                if cpoint_count < mpoint_count:
                    y_change = 10
                else:
                    y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0


#set up key press definitions for controlling the mouse
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if mpoint_count < cpoint_count:
                    mx_change = -10
                else:
                    mx_change = -5
                    
            elif event.key == pygame.K_d:
                if mpoint_count < cpoint_count:
                    mx_change = 10
                else:                
                    mx_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                mx_change = 0
                

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if mpoint_count < cpoint_count:
                    my_change = -10
                else:                
                    my_change = -5
            elif event.key == pygame.K_s:
                if mpoint_count < cpoint_count:
                    my_change = 10
                else:                
                    my_change = +5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                my_change = 0

#set up x & y change of cat to stay within window boundaries
    
    new_x = x + x_change
    new_y = y + y_change
    if new_x >=0 and new_x <= display_width - cat_width:
        x += x_change

                                    
    if new_y >= 0 and new_y <= display_height - cat_height:
        y += y_change
    

#set up x & y change of mouse to stay within window boundaries
    new_mx = mx + mx_change
    new_my = my + my_change
        
    if new_mx >=0 and new_mx <= display_width - mouse_width:
        mx += mx_change

            
    if new_my >= 0 and new_my <= display_height - mouse_height:
        my += my_change


#set up a 3,2,1 countdown with images between points
    catRect = pygame.Rect(x, y, cat_width, cat_height)
    mouseRect = pygame.Rect(mx, my, mouse_width, mouse_height)
    
    if catRect.colliderect(mouseRect):
        x = (50)
        y = (display_height - cat_height*2)
        mx = (display_width - mouse_width)
        my = 0
        cpoint_count += 1
        cpointsImg = pygame.image.load(points[cpoint_count])
        if cpoint_count == 5:
            game_over = True
            cat_win = True
            
                        
            
        
    if mouseRect.colliderect(cheeseRect):
        mx = (display_width - mouse_width)
        my = 0        
        x = (50)
        y = (display_height - cat_height*2)
        mpoint_count += 1
        mpointsImg = pygame.image.load(points[mpoint_count])  
        if mpoint_count == 5:
            game_over = True 
            mouse_win = True
        
            
                 
        

#draw the frame
    gameDisplay.fill(white)
    cat(x,y)
    mouse(mx,my)
    cheese(cx,cy)
    
    if cat_win == True:
        gameDisplay.blit(catWinImg, (display_width * .35, display_height * .35))
        gameDisplay.blit(cScoreImg, (sx,sy))
        gameDisplay.blit(mScoreImg, (0, cScore_height + 10))
        gameDisplay.blit(cpointsImg, (cScore_width,0))
        gameDisplay.blit(mpointsImg, (mScore_width,mScore_height+10))        
        pygame.display.flip()
        time.sleep(10)
        pygame.quit() 
    elif mouse_win == True:
        gameDisplay.blit(mouseWinImg, (display_width * .35, display_height * .35))
        gameDisplay.blit(cScoreImg, (sx,sy))
        gameDisplay.blit(mScoreImg, (0, cScore_height + 10))
        gameDisplay.blit(cpointsImg, (cScore_width,0))
        gameDisplay.blit(mpointsImg, (mScore_width,mScore_height+10)) 
        pygame.display.flip()
        time.sleep(10)
        pygame.quit()    
    else:
        gameDisplay.blit(cScoreImg, (sx,sy))
        gameDisplay.blit(mScoreImg, (0, cScore_height + 10))
        gameDisplay.blit(cpointsImg, (cScore_width,0))
        gameDisplay.blit(mpointsImg, (mScore_width,mScore_height+10))
        pygame.display.flip()
#set up fps
    clock.tick(60)
    
pygame.quit()

   
    
        

            
