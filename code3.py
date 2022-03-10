#!/usr/bin/env python3
# Simple pygame program

# Import and initialize the pygame library

import pygame
import math
from target import Target
from missile_path import Path
from missile import Missile

pygame.init()

FPS = 60 # frames per second
# Set up the drawing window
SCREEN_W, SCREEN_H = 960, 540
screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])
clock = pygame.time.Clock()

LAUNCH_SITE_COORD = SCREEN_W//2, SCREEN_H

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
			t = Target(target_coord)
			pth = Path(LAUNCH_SITE_COORD, target_coord)
			missile = Missile(LAUNCH_SITE_COORD, target_coord)

			targetGroups.add(t)
			targetGroups.add(pth)
			targetGroups.add(missile)

	# Fill the background with white
	screen.fill((255, 255, 255))

	targetGroups.update()
	targetGroups.draw(screen)

	# Flip the display
	pygame.display.flip()
	clock.tick(FPS)

# Done! Time to quit.
pygame.quit()