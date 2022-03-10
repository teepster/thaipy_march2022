#!/usr/bin/env python3

import pygame
import math

Target_BASE_SIZE = 8
RED = (215,75,75)
TargetLockImage = pygame.Surface((Target_BASE_SIZE,Target_BASE_SIZE))
TargetLockImage.fill(RED)

class Target(pygame.sprite.Sprite):
	MAX_SIZE_SCALE = 2
	FREQUENCY = 8 

	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = TargetLockImage

		self.centerLocation = pos
		self.rect = self.image.get_rect()
		self.rect.center = self.centerLocation
 
	def update(self):
		# throb according to frequency.
		tks = pygame.time.get_ticks()
		scaleFactor = 1 + self.MAX_SIZE_SCALE*abs(math.sin(self.FREQUENCY*tks/1000))
		w,h = TargetLockImage.get_size()
		sw,sh = int(scaleFactor*w), int(scaleFactor*h)
		self.image = pygame.transform.scale(TargetLockImage,( sw, sh ))

		# reset the center position
		self.rect = self.image.get_rect()
		self.rect.center = self.centerLocation