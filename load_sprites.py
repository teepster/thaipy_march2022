#!/usr/bin/env python3

import pygame

GlobalSpriteListDict = {}
GlobalSpriteListDict['air_explosion'] = {
	'filename': "./peach_explosion.png",
	'sprite_size': (128,128),
	'sheet_grid':(5,8),
	'scale': 1.5,
	'sprite_images': []
}


def get_sprites_from_spritesheet(sprite_key):
	global GlobalSpriteListDict

	filename = GlobalSpriteListDict[sprite_key]['filename']
	sprite_size_wh = GlobalSpriteListDict[sprite_key]['sprite_size']
	sheet_grid_wh = GlobalSpriteListDict[sprite_key]['sheet_grid']
	scale = GlobalSpriteListDict[sprite_key]['scale']

	if GlobalSpriteListDict[sprite_key]['sprite_images'] == []:
		print(f"Loading sprites from {filename}.")
		spritesheet = pygame.image.load(filename).convert()
		rows,cols = sheet_grid_wh
		sprite_w, sprite_h = sprite_size_wh
		sprites = []
		for row in range(rows):
			for col in range(cols):
				offset_x, offset_y = col*sprite_w, row*sprite_h
				#print(f"x = {offset_x} y = {offset_y}")
				sprite = pygame.Surface(sprite_size_wh)
				sprite.set_colorkey((0,0,0))
				sprite.blit(spritesheet,(0,0),(offset_x,offset_y,sprite_w, sprite_h))

				sprite = pygame.transform.scale( sprite, (int(sprite_w*scale), int(sprite_h*scale)))
				sprites.append(sprite)
		GlobalSpriteListDict[sprite_key]['sprite_images'] = sprites

	return GlobalSpriteListDict[sprite_key]['sprite_images']