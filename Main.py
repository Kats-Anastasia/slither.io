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

'''
Не решенные проблемы, их тут дофига и с горкой:
1) Ничего не работает, надо как следует писать этот код
'''

'''
Энергия - сложная хуйня, необходимость в которой объясняется тем, что игра должна
бесконечно долго работать, и при этом не не должна исчезать вся еда с одной стороны,
и не появлялись слишком много еды или слишком большие змеи с другой. Примерно как
сумма массы и энергии постоянна в мире, так и здесь сумма с неким коэффициентом
еды и "массы" змей постоянна. Чтобы еда продолжала генерироваться, приходится
рассчитать "потери" энергии вникуда: например, энергия змеи перед смертью была 30
условных единиц, но змея, которая полностью съела еду-останки, получила всего 20.
Оставшаяся энергия ушла в общий "банк" и в дальнейшем будет сгенерирована в виде
новых фишек еды. За все это отвечают константы food_energy, snake_energy, energy.

Собственная энергия каждого шарика равна 1. Фишки еды весят линейно от радиуса и при r = 5 
стоят 2.5 единицы энергии. При смерти на месте каждого третьего шарика змеи создается
1 шарик с радиусом 5. Получается, что за каждые три шарика выделяется 0.5 единиц энергии.
Эта энергия уйдет на генерацию новых фишек еды.
'''


class Game():

    def __init__(self):
        # Туть рисуется начальный экран, где вводится Имя, выбирается цвет, нажимается кнопка старта игры.        
        pygame.init()
        config.screen = pygame.display.set_mode((config.screen_wight, config.screen_height))
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
        config.screen = pygame.display.set_mode((config.screen_wight,config.screen_height))
        self.new_snake = Snake(name=self.name, color=self.color, game=self)
        config.snakes += [new_snake]
        for i in range (100): # Столько еды создастся изначально
            new_food = Food(game)
            config.all_food += [new_food]
        process = True
        while process:
            for s in config.snakes:
                s.move()
            while self.energy < 10000: # Ну или сколько там
                new_food = Food()
                config.all_food += new_food
            for s in config.snakes:
                s.hit(self)
            pygame.time.delay(200) #Ну или сколько там нужно времени (между движениями змейки)

new_game = game()
    
    
    
    
    
    
    
    
    
     