# -*- coding: utf-8 -*-
from __future__ import division

from cocos.actions import Move
from cocos.sprite import Sprite

from game.resources import resources

class Oblacki(Sprite):
    def __init__(
            self,
            position = (800, 400),
            velocity = (-10, 0),
            speed = 10,
            *args,
            **kwargs):

        kwargs['position'] = position

        super(Oblacki, self).__init__(resources.cloud1, *args, **kwargs)
        self.speed = speed
        self.velocity = velocity

        self.do(Move())
        self.schedule(self.update)

    def update(self, dt):
        if self.position[0] < 0:
            self.position = 810, 30
