#!/usr/bin/env python3

import pygame

ANIMATION_DELAY = 1

class Explosion(pygame.sprite.Sprite):
	def __init__(self, pos, spritelist):
		pygame.sprite.Sprite.__init__(self)

		self.images = spritelist
		self.imageIndex = 0
		self.maxImageIndex = len(spritelist)
		self.image = self.images[self.imageIndex]
		self.mask = pygame.mask.from_surface(self.image)
		self.animation_delay = ANIMATION_DELAY
		self.ticks = 0

		self.rect = self.image.get_rect()
		self.rect.center = pos

	def update(self):
		# count ticks until reach ticks before advance, once that has reached, do something,
		# otherwise skip
		self.ticks += 1
		
		# should we do anything now?
		if self.ticks >= self.animation_delay:
			# advance frame
			self.imageIndex = self.imageIndex + 1
			if self.imageIndex >= self.maxImageIndex:
				self.imageIndex = 0
				self.kill()
			else:
				self.image = self.images[self.imageIndex]
				self.mask = pygame.mask.from_surface(self.image)
			self.ticks = 0
		else:
			pass # skip updating.
