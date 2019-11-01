import pygame
pygame.init()

display_width = 1000
display_height = 800
gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Cat N Mouse')

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)



while True:
    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        break

    gameDisplay.fill(white)
    pygame.display.flip()
        
pygame.quit()
            
