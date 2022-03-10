#!/usr/bin/env python3
# Simple pygame program

# Import and initialize the pygame library

import pygame

from load_sprites import get_sprites_from_spritesheet
from explosion import Explosion

pygame.init()

FPS = 60 # frames per second
# Set up the drawing window
SCREEN_W, SCREEN_H = 960, 540
screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])
clock = pygame.time.Clock()
EXPLOSION_SPRITES = get_sprites_from_spritesheet('air_explosion') 

targetGroups = pygame.sprite.Group()

# Run until the user asks to quit
running = True

while running:
	# Did the user click the window close button?
	# or hit the escape key?
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			keys = pygame.key.get_pressed()
			if keys[pygame.K_ESCAPE]:
				running = False	

		if event.type == pygame.MOUSEBUTTONDOWN:
			target_coord = pygame.mouse.get_pos()
			# create a new rocket and add it to the sprite group.
			
			explosion = Explosion( target_coord, EXPLOSION_SPRITES )
			targetGroups.add(explosion)

	# Fill the background with white
	screen.fill((4, 4, 4))

	targetGroups.update()
	targetGroups.draw(screen)

	# Flip the display
	pygame.display.flip()
	clock.tick(FPS)
	
# Done! Time to quit.
pygame.quit()