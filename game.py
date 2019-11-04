import pygame
pygame.init

arnea = pygame.display.set_mode((1000, 700))








def cat():
    direction = input("Would you like to move forward/backward/left/right?")
    if direction == forward():
        cat.forward(50)
    elif direction == backward():
        cat.backward(50)
    elif direction == left():
        cat.left(90)
        cat.forward(50)
    elif direction == right():
        cat.right(90)
        cat.forward(50)

def mouse():
    if random == 1():
        mouse.forward(50)
    elif random == 2():
        mouse.backward(50)
    elif random == 3():
        mouse.left(90)
        mouse.forward(50)
        mouse.forward(50)
    elif random == 4():
        mouse.right(90)
        mouse.forward(50)

def mouse_two():
    'yes'





game_over = False
while game_over ==False:
    
    for event in pygameevent.get():
        if event.type == pygame.QUIT:
            game_over = True

















pygame.quit()
