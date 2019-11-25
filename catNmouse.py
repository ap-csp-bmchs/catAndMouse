import pygame
import random
import time

pygame.init()

display_width = 1000
display_height = 800
gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Cat N Mouse')
clock = pygame.time.Clock()
timer = 0

# store all images into variables
catImg = pygame.image.load('cat.png')
mouseImg = pygame.image.load('mouse.png')
wall1Img = pygame.image.load('wall1.png')
wall2Img = pygame.image.load('wall2.png')
cheeseImg = pygame.image.load('cheese.png')
cScoreImg = pygame.image.load('cScore.png')
mScoreImg = pygame.image.load('mScore.png')
catWinImg = pygame.image.load('big_cat.png')
mouseWinImg = pygame.image.load('big_mouse.png')
dogImg = pygame.image.load('dog.png')

points = ['zero.png', 'one.png', 'two.png', 'three.png', 'four.png', 'five.png']
cpoint_count = 0
cpointsImg = pygame.image.load(points[0])
mpoint_count = 0
mpointsImg = pygame.image.load(points[0])
white = (255, 255, 255)
black = (0, 0, 0)
cat_width = 131
cat_height = 75
dog_width = 219
dog_height = 195
mouse_width = 38
mouse_height = 25
cheese_width = 35
cheese_height = 34
cScore_width = 206
cScore_height = 29
mScore_width = 206
mScore_height = 29
wall1_width = 130
wall1_height = 33
wall2_width = 33
wall2_height = 130

# cat starting point info
cat_startx = 250
cat_starty = 550
x = 250
y = 550
catRect = pygame.Rect(x, y, cat_width, cat_height)
# mouse starting point info
mouse_startx = display_width - 200
mouse_starty = 100
mx = display_width - 200
my = 100
mouseRect = pygame.Rect(mx, my, mouse_width, mouse_height)
# cheese starting point info
cx = 0
cy = display_height - cheese_height
cheeseRect = pygame.Rect(cx, cy, cheese_width, cheese_height)
# dog starting point info
dx = random.randint(0, display_width - dog_width)
dy = random.randint(0, display_height - dog_height)
# wall starting point info
w1x = (mouse_width + 3)
w1y = (display_height - (wall2_height + mouse_height + 3))
w2x = (w1x + wall1_width)
w2y = (display_height - (wall2_height + mouse_height + 3))
wall1Rect = pygame.Rect(w1x, w1y, wall1_width, wall1_height)
wall2Rect = pygame.Rect(w2x, w2y, wall2_width, wall2_height)

# score location
sx = 0
sy = 0

# cat location change variables
x_change = 0
y_change = 0
new_x = 0
new_y = 0

# mouse location change variables
mx_change = 0
my_change = 0
new_mx = 0
new_my = 0


def cat():
    gameDisplay.blit(catImg, (x, y))


def mouse():
    gameDisplay.blit(mouseImg, (mx, my))


def cheese():
    gameDisplay.blit(cheeseImg, (cx, cy))


def wall1():
    gameDisplay.blit(wall1Img, (w1x, w1y))


def wall2():
    gameDisplay.blit(wall2Img, (w2x, w2y))

def dog(dx, dy):
    gameDisplay.blit(dogImg, (dx, dy))


# game loop
cat_win = False
mouse_win = False
game_over = False

while not game_over:
    # set up quit when user clicks the 'x'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # set up key press definitions for controlling the cat
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if cpoint_count < mpoint_count:
                    x_change = -10
                else:
                    x_change = -3

            elif event.key == pygame.K_RIGHT:
                if cpoint_count < mpoint_count:
                    x_change = 10
                else:
                    x_change = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if cpoint_count < mpoint_count:
                    y_change = -10
                else:
                    y_change = -3
            elif event.key == pygame.K_DOWN:
                if cpoint_count < mpoint_count:
                    y_change = 10
                else:
                    y_change = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

        # set up key press definitions for controlling the mouse
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

    # set up x & y change of cat to stay within window boundaries
    new_x = x + x_change
    new_y = y + y_change
    # is cat within screen
    if 0 <= new_x <= display_width - cat_width:
        # is cat touching wall 1 after x movement?
        if w1x < new_x < w1x + wall1_width or w1x < new_x + cat_width < w1x + wall1_width:
            if catRect.colliderect(wall1Rect):
                x_change = 0
        # is cat touching wall 2 after x movement?
        if w2x < new_x < w2x + wall2_width or w2x < new_x + cat_width < w2x + wall2_width:
            if catRect.colliderect(wall2Rect):
                x_change = 0
        x += x_change
    if 0 <= new_y <= display_height - cat_height:
        # is cat touching wall 1 after y movement?
        if w1y < new_y < w1y + wall1_height or w1y < new_y + cat_height < w1y + wall1_height:
            if catRect.colliderect(wall1Rect):
                y_change = 0
        # is cat touching wall 2 after y movement?
        if w2y < new_y < w2y + wall2_height or w2y < new_y + cat_height < w2y + wall2_height:
            if catRect.colliderect(wall2Rect):
                y_change = 0
        y += y_change

    # set up x & y change of mouse to stay within window boundaries
    new_mx = mx + mx_change
    new_my = my + my_change

    if 0 <= new_mx <= display_width - mouse_width:
        # is mouse touching wall 1 after x movement?
        if w1x < new_mx < w1x + wall1_width or w1x < new_mx + mouse_width < w1x + wall1_width:
            if mouseRect.colliderect(wall1Rect):
                mx_change = 0
        # is mouse touching wall 2 after x movement?
        if w2x < new_mx < w2x + wall2_width or w2x < new_mx + mouse_width < w2x + wall2_width:
            if mouseRect.colliderect(wall2Rect):
                mx_change = 0
        mx += mx_change

    if 0 <= new_my <= display_height - mouse_height:
        # is mouse touching wall 1 after y movement?
        if w1y < new_my < w1y + wall1_height or w1y < new_my + mouse_height < w1y + wall1_height:
            if mouseRect.colliderect(wall1Rect):
                my_change = 0
        # is mouse touching wall 2 after y movement?
        if w2y < new_my < w2y + wall2_height or w2y < new_my + mouse_height < w2y + wall2_height:
            if mouseRect.colliderect(wall2Rect):
                my_change = 0
        my += my_change

    # set up collisions between cat, mouse, cheese
    catRect = pygame.Rect(x, y, cat_width, cat_height)
    mouseRect = pygame.Rect(mx, my, mouse_width, mouse_height)

    if catRect.colliderect(mouseRect):
        x = cat_startx
        y = cat_starty
        mx = mouse_startx
        my = mouse_starty
        cpoint_count += 1
        cpointsImg = pygame.image.load(points[cpoint_count])

        pygame.mixer.music.load('catYum.wav')
        pygame.mixer.music.play(0)
        if cpoint_count == 5:
            game_over = True
            cat_win = True

    if mouseRect.colliderect(cheeseRect):
        mx = mouse_startx
        my = mouse_starty
        x = cat_startx
        y = cat_starty
        mpoint_count += 1
        mpointsImg = pygame.image.load(points[mpoint_count])
        pygame.mixer.music.load('mouseYum.wav')
        pygame.mixer.music.play(0)
        if mpoint_count == 5:
            game_over = True
            mouse_win = True

    # draw the frame
    gameDisplay.fill(white)
    cat()
    mouse()
    cheese()
    wall1()
    wall2()
    if dx < 0 or dx + dog_width > display_width:
        dx = random.randint(0, display_width - dog_width)
    if dy < 0 or dy + dog_height > display_height:
        dy = random.randint(0, display_height - dog_height)
    dog(dx, dy)
    dx += 5
    dy += 5

    # cat win ending
    if cat_win:
        gameDisplay.blit(catWinImg, (display_width * .35, display_height * .35))
        gameDisplay.blit(cScoreImg, (sx, sy))
        gameDisplay.blit(mScoreImg, (0, cScore_height + 10))
        gameDisplay.blit(cpointsImg, (cScore_width, 0))
        gameDisplay.blit(mpointsImg, (mScore_width, mScore_height + 10))
        pygame.display.flip()
        pygame.mixer.music.load('catCall.wav')
        pygame.mixer.music.play(0)
        time.sleep(10)
        pygame.quit()

    # mouse win ending
    elif mouse_win:
        gameDisplay.blit(mouseWinImg, (display_width * .35, display_height * .35))
        gameDisplay.blit(cScoreImg, (sx, sy))
        gameDisplay.blit(mScoreImg, (0, cScore_height + 10))
        gameDisplay.blit(cpointsImg, (cScore_width, 0))
        gameDisplay.blit(mpointsImg, (mScore_width, mScore_height + 10))
        pygame.display.flip()
        pygame.mixer.music.load('mouseCall.wav')
        pygame.mixer.music.play(0)
        time.sleep(10)
        pygame.quit()

    # if nobody has won
    else:
        gameDisplay.blit(cScoreImg, (sx, sy))
        gameDisplay.blit(mScoreImg, (0, cScore_height + 10))
        gameDisplay.blit(cpointsImg, (cScore_width, 0))
        gameDisplay.blit(mpointsImg, (mScore_width, mScore_height + 10))
        pygame.display.flip()

    # set up fps
    clock.tick(60)
    timer += 1

# if game loop has been broken
pygame.quit()
