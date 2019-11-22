import pygame
import colors
import random

from vector import Vector2d
import config

'''
Собственная энергия каждого шарика всегда равна 1
'''


class Ball():
    def __init__(self, x, y, color, r):
        '''
        Создает шарик змеи с заданными координатами и радиусом.
        '''
        
        self.r = r
        self.x = x
        self.y = y
        self.coords = Vector2d(self.x, self.y)
        self.color = color
        
    def move(self, other):
        '''
        Вводишь предыдущий шарик (который ближе к башке) и он двигает этот. Движение змеи происходит с хвоста
        '''
        self.x = other.x
        self.y = other.y
        
    def draw(self, center, r):
        '''
        Рисует шарик змеи в случае, если он попадает на экран. Пересчитывает свои "глобальные" координаты в координаты экрана.
        '''
        alfa = config.radius / r
        new_coords = (self.coords - center) * alfa + config.center
        new_r = self.r * alfa
        
        pygame.draw.circle(config.screen, self.color, (new_coords.x, new_coords.y), new_r)
        
        
        
        