import pygame
pygame.init

#create game area
arena = pygame.display.set_mode((1000, 700))
arena.fill((0, 0, 0))
pygame.display.update()
pygame.display.set_caption("Trick Or Treat")

#create "cat" and "mouse"
char = pygame.sprite.Group
class p(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (50, 50)
trick = p()
char.add(trick)
 

