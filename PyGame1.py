import pygame
pygame.init()

HEIGHT = 300
WIDTH = 500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Pygame")

walkRight = [pygame.image.load('ChacPic/tile010.png'),pygame.image.load('ChacPic/tile011.png'),pygame.image.load('ChacPic/tile012.png'),pygame.image.load('ChacPic/tile013.png'),pygame.image.load('ChacPic/tile014.png'),pygame.image.load('ChacPic/tile015.png')]
stand = [pygame.image.load('ChacPic/tile000.png'),pygame.image.load('ChacPic/tile001.png'),pygame.image.load('ChacPic/tile002.png'),pygame.image.load('ChacPic/tile003.png')]
background = pygame.image.load('ChacPic/bg.jpg')
attack = [pygame.image.load('ChacPic/tile040.png'),pygame.image.load('ChacPic/tile041.png'),pygame.image.load('ChacPic/tile042.png'),pygame.image.load('ChacPic/tile043.png'),pygame.image.load('ChacPic/tile044.png'),pygame.image.load('ChacPic/tile045.png'),pygame.image.load('ChacPic/tile046.png'),pygame.image.load('ChacPic/tile047.png'),pygame.image.load('ChacPic/tile048.png'),pygame.image.load('ChacPic/tile049.png'),pygame.image.load('ChacPic/tile050.png'),pygame.image.load('ChacPic/tile051.png'),pygame.image.load('ChacPic/tile052.png'),pygame.image.load('ChacPic/tile053.png'),pygame.image.load('ChacPic/tile054.png'),pygame.image.load('ChacPic/tile055.png'),]
spell = [pygame.image.load('ChacPic/tile031.png'),pygame.image.load('ChacPic/tile032.png'),pygame.image.load('ChacPic/tile033.png'),pygame.image.load('ChacPic/tile034.png'),pygame.image.load('ChacPic/tile035.png'),pygame.image.load('ChacPic/tile036.png'),pygame.image.load('ChacPic/tile037.png'),pygame.image.load('ChacPic/tile038.png')]
bullet = pygame.image.load('ChacPic/bullet2.png')

clock = pygame.time.Clock()

class player():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.standLeft = False
        self.standRight = False
        self.attacking = False
        self.spelling = False
        self.walkCount = 0
        self.standCount = 0
        self.attackCount = 0
        self.spellCount = 0

    def draw(self,win):
        if self.walkCount + 1 >= 30:
            self.walkCount = 0
        if self.standCount + 1 >= 21:
            self.standCount = 0
        if self.attackCount + 1 >= 48:
            self.attackCount = 0
        if self.spellCount + 1 >= 24:
            self.spellCount = 0
        if self.right:
            win.blit(walkRight[self.walkCount // 5], (self.x, self.y))
            self.walkCount += 1
        elif self.left:
            win.blit(pygame.transform.flip(walkRight[self.walkCount // 5], True, False), (self.x, self.y))
            self.walkCount += 1
        elif self.attacking:
            if self.standRight:
                win.blit(attack[self.attackCount // 3], (self.x, self.y))
                self.attackCount += 1
            else:
                win.blit(pygame.transform.flip(attack[self.attackCount // 3], True, False), (self.x, self.y))
                self.attackCount += 1
        elif self.spelling:
            if self.standRight:
                win.blit(spell[self.spellCount // 3], (self.x, self.y))
                self.spellCount += 1
            else:
                win.blit(pygame.transform.flip(spell[self.spellCount // 3], True, False), (self.x, self.y))
                self.spellCount += 1
        elif self.standRight:
            win.blit(stand[self.standCount // 5], (self.x, self.y))
            self.standCount += 1
        else:
            win.blit(pygame.transform.flip(stand[self.standCount // 5], True, False), (self.x, self.y))
            self.standCount += 1

class projectile():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        if assasin.standRight:
            self.vel = 8 * 1
        else:
            self.vel = 8 * -1

    def draw(self,win):
        if self.vel > 0:
            win.blit(bullet, (self.x, self.y))
        elif self.vel < 0:
            win.blit(pygame.transform.flip(bullet, True, False), (self.x, self.y))
def redrawGameWindow():
    global walkCount, standCount,attackCount
    win.blit(background,(0,0))
    assasin.draw(win)
    for bulletCount in bullets:
        bulletCount.draw(win)
    pygame.display.update()

#mainloop
assasin = player(50,225,50,37)
bullets = []
run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for bulletCount in bullets:
        if bulletCount.x < WIDTH and bulletCount.x > 0:
            bulletCount.x += bulletCount.vel
        else:
            bullets.pop(bullets.index(bulletCount))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and assasin.x > 0:
        assasin.x -= assasin.vel
        assasin.left = True
        assasin.right = False
        assasin.standLeft = True
        assasin.standRight = False
        assasin.attacking = False
        assasin.spelling = False
        assasin.standCount = 0
        assasin.attackCount = 0
        assasin.spellCount = 0
    elif keys[pygame.K_RIGHT] and assasin.x < WIDTH - assasin.width:
        assasin.x += assasin.vel
        assasin.right = True
        assasin.left = False
        assasin.standLeft = False
        assasin.standRight = True
        assasin.attacking = False
        assasin.spelling = False
        assasin.standCount = 0
        assasin.attackCount = 0
        assasin.spellCount = 0
    elif keys[pygame.K_z]:
        assasin.right = False
        assasin.left = False
        assasin.attacking = True
        assasin.spelling = False
        assasin.walkCount = 0
        assasin.standCount = 0
        assasin.spellCount = 0
    elif keys[pygame.K_x]:
        assasin.right = False
        assasin.left = False
        assasin.attacking = False
        assasin.spelling = True
        assasin.walkCount = 0
        assasin.standCount = 0
        assasin.attackCount = 0
        if len(bullets) < 4 and assasin.spellCount == 10:
            bullets.append(projectile(round(assasin.x + assasin.width//2),round(assasin.y + assasin.height//2)))
    else:
        assasin.right = False
        assasin.left = False
        assasin.attacking = False
        assasin.walkCount = 0
        assasin.attackCount = 0
        assasin.spellCount = 0

    if not assasin.isJump:
        # if keys[pygame.K_UP] and y > 0:
        #     y -= vel
        # if keys[pygame.K_DOWN] and y < 500 - height:
        #     y += vel
        if keys[pygame.K_SPACE]:
            assasin.isJump = True
            assasin.right = False
            assasin.left = False
            assasin.walkCount = 0
            assasin.standCount = 0
            assasin.attackCount = 0
            assasin.spellCount = 0
    else:
        if assasin.jumpCount >= -10:
            assasin.y = assasin.y + assasin.jumpCount**2*0.25 if assasin.jumpCount < 0 else assasin.y - assasin.jumpCount**2*0.25
            assasin.jumpCount -= 1
        else:
            assasin.isJump = False
            assasin.jumpCount = 10

    redrawGameWindow()

pygame.quit()