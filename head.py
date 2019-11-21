import pygame
import colors
import random
import Ball

class Head(Ball): # Мб это будет просто функцией в классе Ball НЕ БУДЕТ
    def __init__(self, x, y, color, game, snake):
        self.x = x
        self.y = y
        self.r = 25
        self.game = game
        self.snake = snake
        self.color = color
        pygame.draw.circle(self.game.screen, self.color[0],(self.x, self.y), self.r)
        pygame.draw.circle(self.game.screen, self.game.white, (self.x, self, y), self.r) #Бляяяяя а как, тут же надо координаты постоянно пересчитывать как-то...
    def move(self):
        #Обработка мышки
        self.snake.x = self.x
        self.snake.y = self.y
    def hit(self, other): #Пока хз, может и не нужна, но кажется надо
        pass