# -*- coding: utf-8 -*-

import pyglet

pyglet.resource.path = ["@game.resources.sprites"]
pyglet.resource.reindex()

mario = pyglet.resource.image("mario.jpg")
obstacle = pyglet.resource.image("obstacle.png")
background = pyglet.resource.image("background.jpg")
cloud1 = pyglet.resource.image("cloud1.png")
cloud2 = pyglet.resource.image("cloud2.png")
block = pyglet.resource.image("block.png")
sun = pyglet.resource.image("sun.jpg")
mario_spritesheet = pyglet.resource.image("mario_spritesheet.png")
grid = pyglet.image.ImageGrid(mario_spritesheet, 3, 6, item_width = 35, item_height = 50)
textures = pyglet.image.TextureGrid(grid)
mario_desno1 = textures[12:19]
mario_desno = pyglet.image.Animation.from_image_sequence(mario_desno1, 0.1, loop = True)
mario_levo1 = textures[6:12]
mario_levo = pyglet.image.Animation.from_image_sequence(mario_levo1, 0.1, loop = True)
