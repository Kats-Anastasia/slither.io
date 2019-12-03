import random
import math
import pygame

from place import Place
import config
from ball import Ball
from food import Food
from head import Head
from snake import Snake
from network import Network
#from text_object import TextObject
import colors


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
        pygame.init()
        config.screen = pygame.display.set_mode((config.screen_width,config.screen_height))
        config.screen.fill(colors.white)
        new_snake = Snake()
        config.snakes += [new_snake]
        place = Place()
        for i in range (0): # Столько еды создастся изначально
            new_food = Food()
            config.all_food += [new_food]
        config.process = True
        while config.process:
            config.screen.fill(colors.black)
            pygame.time.delay(40)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()
            pressed = pygame.mouse.get_pressed()
            if pressed[0]:
                speeding = 2
            else:
                speeding = 1
            for s in config.snakes:
                s.move(speeding)
            while config.food_energy + config.snake_energy < config.max_energy: # Ну или сколько там
                new_food = Food()
                config.all_food += [new_food]
            for f in config.all_food:
                f.draw(new_snake.coords)
            for s in config.snakes:
                s.draw()
            place.draw(new_snake.coords)
            pygame.display.update()

if __name__ == "__main__":
    new_game = Game()
    
    
