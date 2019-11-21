import pygame
import colors
import random

class Ball():
    def __init__(self, x, y, color, game, r):
        self.r = random.uniform(2, 5)
        self.x = x
        self.y = y
        self.color = color
        self.game = game
        pygame.draw.circle(self.game.screen, color[0], (self.x, self.y), self.r)
    def move(self, other):
        # Вводишь предыдущий шарик (который ближе к башке) и он двигает новый. Движение змеи происходит с хвоста
        self.x = other.x
        self.y = other.y
        pygame.draw.circle(self.game.screen, color[0], (self.x, self.y), self.r)
    def grow(self, event=0):
        pass
		