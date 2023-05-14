import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_position = [0, 0, 0]

clock = pygame.time.Clock()


def glVertex3f(param, param1, param2):
    pass


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[K_LEFT]:
        player_position[0] -= 0.1
    elif keys[K_RIGHT]:
        player_position[0] += 0.1

    if keys[K_UP]:
        player_position[1] += 0.1
    elif keys[K_DOWN]:
        player_position[1] -= 0.1

    if keys[K_SPACE]:
        player_position[2] += 0.1

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    gluPerspective(45, (SCREEN_WIDTH/SCREEN_HEIGHT), 0.1, 50.0)
    glTranslatef(player_position[0], player_position[1], -5)

    glBegin(GL_QUADS)
    glColor3f(0,1,0)
    glVertex3f(1,1,-1)
    glVertex3f(-1,1,-1)
    glVertex3f(-1,1,1)
    glVertex3f(1,1,1)

    glColor3f(1,0.5,0)
    glVertex3f(1,-1,1)
    glVertex3f(-1,-1,1)
    glVertex3f(-1,-1,-1)
    glVertex3f(1,-1,-1)

    glColor3f(1,0,0)
    glVertex3f(1,1,1)
    glVertex3f(-1,1,1)
    glVertex3f(-1,-1,1)
    glVertex3f(1,-1,1)

    glColor3f(1,1,0)
    glVertex3f(1,-1,-1)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1,1,-1)
    glVertex3f(1,1,-1)

    glColor3f(0,0,1)
    glVertex3f(-1,1,1)
    glVertex3f(-1,1,-1)
    glVertex3f(-1,-1,-1)
    glVertex3f(-1,-1,1)

    glColor3f(1,0,1)
    glVertex3f(1,1,-1)
    glVertex3f(1,1,1)
    glVertex3f(1,-1,1)
    glVertex3f(1,-1,-1)
    glEnd()

    pygame.display.flip()
    clock.tick(60)
