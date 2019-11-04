import pygame
pygame.init()

display_width = 1000
display_height = 800
gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Cat N Mouse')
clock = pygame.time.Clock()

catImg = pygame.image.load('cat.png')

white = (255, 255, 255)
black = (0, 0, 0)



x = (display_width * 0.45)
y = (display_height * 0.45)
x_change = 0
y_change = 0
cat_width = 131
cat_height = 75
new_x = 0
new_y = 0

def cat(x,y):
    gameDisplay.blit(catImg, (x,y))

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

#set up x & y change to stay within window boundaries
    new_x = x + x_change
    if new_x >=0 and new_x <= display_width - cat_width:
        x += x_change

    new_y = y + y_change
    if new_y >= 0 and new_y <= display_height - cat_height:
        y += y_change

#draw the frame
    gameDisplay.fill(white)
    cat(x,y)
    pygame.display.flip()
#set up fps
    clock.tick(60)


pygame.quit()
        

            
