# -*- coding: utf-8 -*-

from __future__ import division

from cocos.actions import Move
from cocos.collision_model import AARectShape
from cocos.director import director
from cocos.sprite import Sprite
from pyglet.window import key

import pyglet

from game import utils
from game.resources import resources

class Player(Sprite):
    def __init__(
            self,
            position = (25, 25),
            velocity = (0, 0),
            speed = 400,
            gravity = -1300,
            *args,
            **kwargs):

        # Push the needed attributes into kwargs
        kwargs['position'] = position

        super(Player, self).__init__(resources.mario_desno, *args, **kwargs)
        self.a = 0
        self.b = 0
        self.speed = speed
        self.gravity = gravity
        self.velocity = velocity
        self.on_block = False

        self.cshape = AARectShape(self.position, self.width//3, self.height//2)

        self.jumping = False
        self.do(Move())

        self.schedule(self.update)

    def update(self, dt):
        self.cshape.center = self.position

        win_width, win_height = director.get_window_size()

        xmin = self.width//2
        xmax = win_width - xmin

        ymin = self.height//2

        if self.position[1] <= ymin:
            self.position = (self.position[0], ymin)
            self.velocity = (self.velocity[0], 0)

            self.jumping = False
        if self.position[0] < xmin:
            self.position = (xmin, self.position[1])
        elif self.position[0] > xmax:
            self.position = (xmax, self.position[1])
        else:
            pass
        if self.on_block:
            self.jumping = False
        self.handle_keys()
        if self.position[1] > 0 and self.on_block == False:

            self.jumping = True

        #if self.velocity[0] == 0:
            #self.image = resources.mario_desno1

    def handle_keys(self):
        vel = [0, self.velocity[1]]
        # if utils.keys[key.LEFT]:
        #     vel[0] -= self.speed//2
        #     self.animate(resources.mario_levo1)
        # if utils.keys[key.RIGHT]:
        #     vel[0] += self.speed//2
        #     self.animate(resources.mario_desno1)
        if utils.keys[key.UP]:
            if not self.jumping:
                vel[1] += (self.speed + 100)
                self.jumping = True
                self.on_block = False
        if utils.keys[key.DOWN]:
            if self.jumping:
                pass
            else:
                self.position = (self.position[0], self.position[1]-25)


        self.velocity = tuple(vel)
