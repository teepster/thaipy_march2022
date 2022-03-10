#!/usr/bin/env python3

import pygame
import math

def blit_rotate(image, pos, originPos, angle):
	# https://stackoverflow.com/questions/59909942/how-can-you-rotate-an-image-around-an-off-center-pivot-in-pygame
	image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
	offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
	rotated_offset = offset_center_to_pivot.rotate(-angle)
	rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
	rotated_image = pygame.transform.rotate(image, angle)
	rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
	return rotated_image, rotated_image_rect
  
class Missile(pygame.sprite.Sprite):
	ASSET_FILE = "./missile.png"
	REDUCTION_SCALE = 8
	PIVOTX = 213
	PIVOTY = 510
	VELOCITY = 12

	def __init__(self, launch_pos, destination_pos):
		pygame.sprite.Sprite.__init__(self)

		load_image = pygame.image.load(self.ASSET_FILE).convert_alpha()
		w,h = load_image.get_size()
		sw,sh = w//self.REDUCTION_SCALE, h//self.REDUCTION_SCALE
		self.upright_rocket_img = pygame.transform.scale(load_image,(sw,sh))

		self.src_pos = launch_pos
		self.des_pos = destination_pos

		# what is my rotation?
		dest_x,dest_y = self.des_pos
		source_x,source_y = self.src_pos

		# i hate the pg coordinate system. :-(
		dx = source_x-dest_x
		dy = source_y-dest_y
		if dx == 0:
			self.rotation = 0
		else:
			self.rotation = math.degrees( math.atan( dx / dy ) ) 

		# trajectory precalculations
		# the following values are constant because rotation is constant
		self.scaled_pivot_x, self.scaled_pivot_y = self.PIVOTX//self.REDUCTION_SCALE, self.PIVOTY//self.REDUCTION_SCALE
		self.sinrotation = math.sin(math.radians(self.rotation))
		self.cosrotation = math.cos(math.radians(self.rotation))
		self.distance_per_tick = math.sqrt(self.VELOCITY*self.sinrotation * self.VELOCITY*self.sinrotation +\
											 self.VELOCITY*self.cosrotation * self.VELOCITY*self.cosrotation
											)
		self.max_distance = math.sqrt( dx*dx + dy*dy )	
		self.distance_traveled = 0.0
		self.image, self.rect = blit_rotate(self.upright_rocket_img, 
											self.src_pos,
											(self.scaled_pivot_x, self.scaled_pivot_y), 
											self.rotation
											)

	def update(self):
		self.distance_traveled += self.distance_per_tick
		if self.distance_traveled > self.max_distance:
			self.kill()
		else:
			dx,dy = self.distance_traveled*self.sinrotation, self.distance_traveled*self.cosrotation
			current_pos = self.src_pos[0] - int(dx), self.src_pos[1] - int(dy)

			self.image, self.rect = blit_rotate(self.upright_rocket_img, 
												current_pos,
												(self.scaled_pivot_x, self.scaled_pivot_y), 
												self.rotation
												)
