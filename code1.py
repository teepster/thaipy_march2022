#!/usr/bin/env python3
# Simple pygame program

# Import and initialize the pygame library
import pygame

pygame.init()

# Set up the drawing window
SCREEN_W, SCREEN_H = 960, 540
screen = pygame.display.set_mode([SCREEN_W, SCREEN_H])

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

	# Fill the background with white
	screen.fill((255, 255, 255))

	# Draw a solid blue circle in the center
	pygame.draw.circle(screen, (0, 0, 255), (SCREEN_W//2, SCREEN_H//2), 75)

	# Flip the display
	pygame.display.flip()

# Done! Time to quit.
pygame.quit()