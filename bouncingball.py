import sys, pygame

pygame.init()

width = 320
height = 240
SIZE = width, height

SPEED = [1, 1]
BLACK = 0, 0, 0

screen = pygame.display.set_mode(SIZE)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(SPEED)
    if ballrect.left < 0 or ballrect.right > width:
        SPEED[0] = -SPEED[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        SPEED[1] = -SPEED[1]

    screen.fill(BLACK)
    screen.blit(ball, ballrect)
    pygame.display.flip()