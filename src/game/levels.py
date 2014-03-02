# -*- coding: utf-8 -*-

class Level():

    def __init__(self, game, *args,**kwargs):
        self.game = game

    def beri(self):
        with open('bloki.txt', 'r') as f:
            for item in f:
                self.game.bloki.append([i.strip() for i in item.split()])

        return(self.game.bloki)
