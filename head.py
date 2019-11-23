import pygame
import colors
import random
import math

from ball import Ball
import config
'''
Не решенные проблемы:
3) Прорисовка глаз змеи, и их поворот при повороте змеи
'''

class Head(Ball):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.r = 25
        self.color = color
        self.alfa = 0
        self.v = 1
        self.vx = self.v
        self.vy = 0
    def move(self, speeding):
        #Обработка мышки
        
        '''
        Движение происходит с помощью считывания координат мышки, если
        угол между скоростью змеи и радиус-вектором до координат мышки
        больше 90, то он просто заменяется на 90 градусов. Если меньше
        90, то он проецирует ускорение на ось, перпендикулярную скорости
        и точно так же прибавляет ускорение. В итоге змея всегда движется
        по окружности с каким-нибудь радиусом и движение происходит без
        изломов.
        '''
        
        min_radius = self.r * config.coefficient * speeding
        acceleration = self.v ** 2 / min_radius
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_alfa = math.atan2((mouse_y - self.y), (mouse_x - self.x))
        self_alfa = math.atan2(self.vy, self.vx)
        delta_alfa = mouse_alfa - self.alfa
        
        if math.fabs(delta_alfa) < math.pi / 2:
            acceleration *= math.cos(math.pi / 2 - math.copysign(delta_alfa, 1))
        delta_alfa = math.copysign(math.pi/2, delta_alfa)
        mouse_alfa = self_alfa + delta_alfa
        self.vx += acceleration * math.cos(mouse_alfa)
        self.vy += acceleration * math.sin(mouse_alfa)
        self.x += self.vx
        self.y += self.vy
        
    def draw(self, a):
        '''
        Переменные a и b нужны чтобы не прописывать отдельно
        движение для головы от остальных шариков. Так они нигде
        не используются.
        Голова рисуется все время одинаковой. Потом, возможно, будут добавлены глаза и какая-то такая фигня
        '''
        
        pygame.draw.circle(config.screen, self.color, (int(config.center.x), int(config.center.y)), config.radius)