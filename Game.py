import pygame, sys, random
from Ball import Ball
from Player import Player
from Bullet import *
from Zombie import *
#from Title import Title
from Score import *


pygame.init()

clock = pygame.time.Clock()

width = 900 
height = 615
size = width, height

screen = pygame.display.set_mode(size)

bgColor = r,g,b = 100, 30, 100
bgImage = pygame.image.load("RSC/Background/FlameWhisps.png").convert()
bgRect = bgImage.get_rect()



player = Player([width/2, height/2])

enemies = []

bullets = []

players = []

score = Score([width-300, height-25], "Score: ", 80)

spawnRate = .1 #seconds

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.go("up")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("right")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.go("down")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("left")
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                bullets += player.shoot()
            if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                player.gun = player.pistol
                player.shoot("stop")
            if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                player.gun = player.shotGun
                player.shoot("stop")
            if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                player.gun = player.uzi
                player.shoot("stop")
            if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                player.gun = player.joker
                player.shoot("stop")
            if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                player.gun = player.exploder
                player.shoot("stop")
            if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                player.gun = player.laser
                player.shoot("stop")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                player.go("stop up")
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.go("stop down")
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.go("stop left")
            if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                player.shoot("stop")
            
    if len(enemies) < 120000:
        if random.randint(0, int(spawnRate*60)) == 0:
            side = random.randint(1,4)
            kind = random.randint(1,121)
            if side == 1: #top
                if kind <30:
                    enemies += [Zombie([random.randint(0,width),-50])]
                elif kind <50:
                    enemies += [RedZombie([random.randint(0,width),-50])]
                elif kind <71:
                    enemies += [Maoira([random.randint(0,width),-50])]
                elif kind <77:
                    enemies += [Phantom([random.randint(0,width),-50])]
                elif kind <86:
                    enemies += [Druflyll([random.randint(0,width),-50])]
                elif kind <101:
                    enemies += [Chatterbox([random.randint(0,width),-50])]
                elif kind <102:
                    enemies += [Illuminatus([random.randint(0,width),-50])]
                elif kind <111:
                    enemies += [Raksasha([random.randint(0,width),-50])]
                elif kind <122:
                    enemies += [Ghast([random.randint(0,width),-50])]
                
                    
            elif side == 2: #right
                if kind <30:
                    enemies += [Zombie([width+50, random.randint(0,height)])]
                elif kind <50:
                    enemies += [RedZombie([width+50, random.randint(0,height)])]
                elif kind <71:
                    enemies += [Maoira([width+50, random.randint(0,height)])]
                elif kind <77:
                    enemies += [Phantom([width+50, random.randint(0,height)])]
                elif kind <86:
                    enemies += [Druflyll([width+50, random.randint(0,height)])]
                elif kind <101:
                    enemies += [Chatterbox([width+50, random.randint(0,height)])]
                elif kind <102:
                    enemies += [Illuminatus([width+50, random.randint(0,height)])]
                elif kind <111:
                    enemies += [Raksasha([width+50, random.randint(0,height)])]
                elif kind <122:
                    enemies += [Ghast([width+50, random.randint(0,height)])]
                
                    
            elif side == 3: #bottom
                if kind <30:
                    enemies += [Zombie([random.randint(0,width),height+50])]
                elif kind <50:
                    enemies += [RedZombie([random.randint(0,width),height+50])]
                elif kind <71:
                    enemies += [Maoira([random.randint(0,width),height+50])]
                elif kind <77:
                    enemies += [Phantom([random.randint(0,width),height+50])]
                elif kind <86:
                    enemies += [Druflyll([random.randint(0,width),height+50])]
                elif kind <101:
                    enemies += [Chatterbox([random.randint(0,width),height+50])]
                elif kind <102:
                    enemies += [Illuminatus([random.randint(0,width),height+50])]
                elif kind <111:
                    enemies += [Raksasha([random.randint(0,width),height+50])]
                elif kind <122:
                    enemies += [Ghast([random.randint(0,width),height+50])]
               
                    
            elif side == 4: #left
                if kind <30:
                    enemies += [Zombie([-50, random.randint(0,height)])]
                if kind <50:
                    enemies += [RedZombie([-50, random.randint(0,height)])]
                elif kind <71:
                    enemies += [Maoira([-50, random.randint(0,height)])]
                elif kind <77:
                    enemies += [Phantom([-50, random.randint(0,height)])]
                elif kind <86:
                    enemies += [Druflyll([-50, random.randint(0,height)])]
                elif kind <101:
                    enemies += [Chatterbox([-50, random.randint(0,height)])]
                elif kind <102:
                    enemies += [Illuminatus([-50, random.randint(0,height)])]
                elif kind <111:
                    enemies += [Raksasha([-50, random.randint(0,height)])]
                elif kind <121:
                    enemies += [Ghast([-50, random.randint(0,height)])]
                elif kind <122:
                    enemies += [BadJuju([-50, random.randint(0,height)])]
    
    if len(enemies) > 60:
        bgImage = pygame.image.load("RSC/Background/OurSavior.png").convert()

    
    
    player.update(width, height)
    score.update()
    if player.shooting:
        bullets += player.shoot()
    for enemy in enemies:
        enemy.update(width, height, player.rect.center)
    for bullet in bullets:
        bullet.update(width, height)
        
    for bullet in bullets:
        for enemy in enemies:
            oldBlen = len(bullets)
            bullets += bullet.collideZombie(enemy)
            enemy.collideBullet(bullet)
            if not enemy.living:
                if enemy.kind == "zombie":
                    score.increaseScore(100)
                    enemies.remove(enemy)
                elif enemy.kind == "maoira":
                    score.increaseScore(500)
                    enemies.remove(enemy)
                elif enemy.kind == "druflyll":
                    score.increaseScore(3500)
                    enemies.remove(enemy)
                elif enemy.kind == "phantom":
                    score.increaseScore(5000)
                    enemies.remove(enemy)
                elif enemy.kind == "chatterbox":
                    score.increaseScore(2000)
                    enemies.remove(enemy)
                elif enemy.kind == "illuminatus":
                    score.increaseScore(666666)
                    enemies.remove(enemy)  
                elif enemy.kind == "raksasha":
                    score.increaseScore(7500)
                    enemies.remove(enemy) 
                elif enemy.kind == "ghast":
                    score.increaseScore(7500)
                    enemies.remove(enemy)     
                elif enemy.kind == "badjuju":
                    score.increaseScore(35353535353535353535353535353535)
                    enemies.remove(enemy)        
        
        if not bullet.living:
            bullets.remove(bullet)
    
    #for enemy in enemies:
        #for bullet in bullets:
            #enemy.collideBullet(bullet)
    
    #for enemy in enemies:
        #if not enemy.living:
            
            #enemies.remove(enemy)
    #for bullet in bullets:
        #if not bullet.living:
            #bullets.remove(bullet)
    
    for player in players:
        if not player.living:
            players.remove(player)
    
    #for i, z in enumerate(enemies):
        #print i, z.rect.center
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    for enemy in enemies:
        screen.blit(enemy.image, enemy.rect)
    for bullet in bullets:
        screen.blit(bullet.image, bullet.rect)
    screen.blit(player.image, player.rect)
    screen.blit(score.image, score.rect)
    pygame.display.flip()
    clock.tick(60)




