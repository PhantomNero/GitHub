import pygame
import random
import time

def rand(list):
    r = random.randint(0, 3)
    list.append(r)
    return list

def start(list):
    time.sleep(2)
    global pgreen,pred,pblue,pyellow
    x=list[-1]
    pygame.mixer.music.play()
    pred = pygame.image.load("pred.png")
    pgreen = pygame.image.load("pgreen.png")
    pblue = pygame.image.load("pblue.png")
    pyellow = pygame.image.load("pyellow.png")
    if x==0:
        pred=pygame.image.load("red.png")
    elif x==1:
        pgreen=pygame.image.load("green.png")
    elif x==2:
        pblue=pygame.image.load("blue.png")
    else:
        pyellow = pygame.image.load("yellow.png")

def guess(list,f):
    global level,pl
    time.sleep(0.5)
    global pgreen,pred,pblue,pyellow
    x=f

    pred = pygame.image.load("pred.png")
    pgreen = pygame.image.load("pgreen.png")
    pblue = pygame.image.load("pblue.png")
    pyellow = pygame.image.load("pyellow.png")
    if x!=-1:
        pygame.mixer.music.play()
        pl.append(x)
        if x==0:
            pred=pygame.image.load("red.png")
        elif x==1:
            pgreen=pygame.image.load("green.png")
        elif x==2:
            pblue=pygame.image.load("blue.png")
        else:
            pyellow = pygame.image.load("yellow.png")


pygame.init()
screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
FPS = 30
name = 'Rbut'
pygame.display.set_caption(name)
level = 1

running = True
my_font = pygame.font.SysFont('None', 60)
text1 = my_font.render('Уровень: ' + str(level), True, (0, 0, 0))
bg = pygame.image.load("bg.jpg")
pred = pygame.image.load("pred.png")
pgreen = pygame.image.load("pgreen.png")
pblue = pygame.image.load("pblue.png")
pyellow = pygame.image.load("pyellow.png")
bip = pygame.mixer.music.load("bip.mp3")
pos = []
pl = []
f=-1
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                f=0
            if event.key == pygame.K_g:
                f=1
            if event.key == pygame.K_b:
                f=2
            if event.key == pygame.K_y:
                f=3
    if len(pos) < level:
        pos = rand(pos)
        start(pos)
    else:
        guess(pos,f)
    if len(pl)!=0:
        if pl[-1]!=pos[len(pl)-1]:
            pygame.quit()
        if len(pl)==level and pl==pos:
            level+=1
            pl=[]
            pos=[]
    text1 = my_font.render('Уровень: ' + str(level), True, (0, 0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(text1, (700, 50))
    screen.blit(pred, (200, 150))
    screen.blit(pgreen, (500, 150))
    screen.blit(pblue, (200, 450))
    screen.blit(pyellow, (500, 450))
    pygame.display.flip()
    f=-1
    print(pos)
pygame.quit()
