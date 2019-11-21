import random
import math
import pygame

import config
from ball import Ball
from food import Food and Big_food #хз
from head import Head
from snake import Snake
#from text_object import TextObject
import colors


    
class Game():
    
    self.energy = 0 #Штука, обозначающая полную энергию системы. Она складывается с некоторым коэффициентом из колличества шариков змеи, количества шариков еды, может быть чего-то еще)

    def __init__(self):
        # Туть рисуется начальный экран, где вводится Имя, выбирается цвет, нажимается кнопка старта игры.        
        pygame.init()
        self.screen = pygame.display.set_mode((configuration.screen_wight, configuration.screen_height))
        start = True
        self.color = 0
        self.name = 0
        while start: # Может лучше не так, а просто чтобы он ждал пока не произойдет событие. Но я не знаю как это сделать
            for i in pygame.event.get():
                # if i.type == pygame. # Штука, отвечающая за нажатие кнопки
                start = False
            # Тут еще хуйня, которая выполняет выбор цвета змеи, вводит название
            pygame.time.delay(20)
        self.start_game(name=self.name, color=self.color)
    def start_game(self):
        self.screen = pygame.display.set_mode((1000,1000))
        self.new_snake = Snake(name=self.name, color=self.color, game=self)
        self.snakes = []
        self.snakes += [new_snake]
        self.all_food = []
        for i in range (100): # Столько еды создастся изначально
            new_food = Food(game)
            self.all_food += [new_food]
        process = True
        while process:
            self.new_snake.timer += 1 # (ну или сколько там (возможно, таймер не нужен, а он будет только на фишки еды)
            for s in self.snakes:
                s.move()
            if self.energy < 1000: # Ну или сколько там
                new_food = Food(game)
                self.all_food += new_food
            for s in snakes:
                s.hit(self)
            pygame.time.delay(200) #Ну или сколько там нужно времени (между движениями змейки)

new_game = game()
    
    
    
    
    
    
    
    
    
     