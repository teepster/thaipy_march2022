#!/usr/bin/env python3

import pygame
import math

BLUE_GRAY = (55, 85, 100)
LINE_WIDTH = 3

def getWidthAndHeight(pos1, pos2):
	return abs(pos2[0]-pos1[0]),abs(pos2[1]-pos1[1])

class Path(pygame.sprite.Sprite):
	""" Create a line path from the launch position to the targetted destination pos."""
	def __init__(self,launch_pos,destination_pos):
		pygame.sprite.Sprite.__init__(self)
		window_w,window_h = getWidthAndHeight(launch_pos,destination_pos)
		self.image = pygame.Surface((window_w,window_h),pygame.SRCALPHA)
		if launch_pos[0]<destination_pos[0]:
			# To the right
			pygame.draw.line(self.image,BLUE_GRAY,(0,window_h),(window_w,0), width=LINE_WIDTH)
		else:
			#To the left
			pygame.draw.line(self.image,BLUE_GRAY,(0,0),(window_w,window_h), width=LINE_WIDTH)
		self.rect = pygame.Rect(0,0,window_w,window_h)
		topleft_coord = min(launch_pos[0],destination_pos[0]), min(launch_pos[1],destination_pos[1])	
		self.rect.topleft = topleft_coord
