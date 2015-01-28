import pygame, sys, random
from Ball import Ball
from Player import Player
from Bullet import *
from Zombie import Zombie
#from Text import Text
#from Title import Title
#from Score import Score
#from Powerup import Powerup


pygame.init()

clock = pygame.time.Clock()

width = 900 
height = 600
size = width, height

screen = pygame.display.set_mode(size)

bgColor = r,g,b = 100, 30, 100
bgImage = pygame.image.load("RSC/Background/background1.png").convert()
bgRect = bgImage.get_rect()



player = Player([width/2, height/2])

enemies = []

bullets = []

spawnRate = .33 #seconds

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
			
	if len(enemies) < 120:
		if random.randint(0, int(spawnRate*60)) == 0:
			side = random.randint(1,4)
			if side == 1: #top
				enemies += [Zombie([random.randint(0,width),-50])]
			elif side == 2: #right
				enemies += [Zombie([width+50, random.randint(0,height)])]
			elif side == 3: #bottom
				enemies += [Zombie([random.randint(0,width),height+50])]
			elif side == 4: #left
				enemies += [Zombie([-50, random.randint(0,height)])]
		
	player.update(width, height)
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
				enemies.remove(enemy)
		if not bullet.living:
			bullets.remove(bullet)
	
	#for enemy in enemies:
		#for bullet in bullets:
			#enemy.collideBullet(bullet)
		#for exploder in exploders:
			#enemy.collideBullet(exploder)
	
	for enemy in enemies:
		if not enemy.living:
			enemies.remove(enemy)
	for bullet in bullets:
		if not bullet.living:
			bullets.remove(bullet)
	
	#for exploder in exploders:
		#if not exploder.living:
			#exploder.remove(exploder)
	
	#for i, z in enumerate(enemies):
		#print i, z.rect.center
	
	bgColor = r,g,b
	screen.fill(bgColor)
	screen.blit(bgImage, bgRect)
	for enemy in enemies:
		screen.blit(enemy.image, enemy.rect)
	for bullet in bullets:
		screen.blit(bullet.image, bullet.rect)
	#for exploder in exploders:
		#screen.blit(exploder.image, exploder.rect)
	screen.blit(player.image, player.rect)
	pygame.display.flip()
	clock.tick(60)




