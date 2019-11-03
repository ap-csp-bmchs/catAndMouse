import pygame
pygame.init()

display_width = 1000
display_height = 800
gameDisplay = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

pygame.display.set_caption('Cat N Mouse')

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

catImg = pygame.image.load('cat.png')

def cat(x,y):
    gameDisplay.blit(catImg, (x,y))

x = (display_width * 0.45)
y = (display_height * 0.45)
x_change = 0
y_change = 0


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

    x += x_change
    y += y_change
    gameDisplay.fill(white)
    cat(x,y)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
        

            
