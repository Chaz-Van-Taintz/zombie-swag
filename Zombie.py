import pygame,math
from Ball import Ball


class Zombie(Ball):
	def __init__(self, pos):
		Ball.__init__(self, "RSC/Zombie/zombieu1.png", [0,0], pos)
		self.upImages = [pygame.image.load("RSC/Zombie/zombieu1.png"),
						 ]
		self.downImages = [pygame.image.load("RSC/Zombie/zombied1.png"),
						   ]
		self.leftImages = [pygame.image.load("RSC/Zombie/zombiel1.png"),
						   ]
		self.rightImages = [pygame.image.load("RSC/Zombie/zombier1.png"),
						    ]
		self.facing = "up"
		self.changed = False
		self.images = self.upImages
		self.frame = 0
		self.maxFrame = len(self.images) - 1
		self.waitCount = 0
		self.maxWait = 60*.25
		self.image = self.images[self.frame]
		self.rect = self.image.get_rect(center = self.rect.center)
		self.maxSpeed = 10
			
	def update(self, width, height, playerPos):
		self.facePlayer(playerPos)
		Ball.update(self, width, height)
		self.animate()
		self.changed = False
	
	def facePlayer(self, pt):
		xdiff = pt[0] - self.rect.center[0]
		ydiff = pt[1] - self.rect.center[1]
		
		if math.fabs(xdiff) > math.fabs(ydiff): #left/right
			if xdiff > 0: #right
				self.facing = "right"
				
		
	def collideWall(self, width, height):
		if not self.didBounceX:
			#print "trying to hit Wall"
			if self.rect.left < 0 or self.rect.right > width:
				self.speedx = 0
				self.didBounceX = True
				#print "hit xWall"
		if not self.didBounceY:
			if self.rect.top < 0 or self.rect.bottom > height:
				self.speedy = 0
				self.didBounceY = True
				#print "hit xWall"
	
	def animate(self):
		if self.waitCount < self.maxWait:
			self.waitCount += 1
		else:
			self.waitCount = 0
			self.changed = True
			if self.frame < self.maxFrame:
				self.frame += 1
			else:
				self.frame = 0
		
		if self.changed:	
			if self.facing == "up":
				self.images = self.upImages
			elif self.facing == "down":
				self.images = self.downImages
			elif self.facing == "right":
				self.images = self.rightImages
			elif self.facing == "left":
				self.images = self.leftImages
			
			self.image = self.images[self.frame]
