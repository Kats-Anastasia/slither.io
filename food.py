import pygame
import colors
import random

class Food():
    def __init__(self, game, x=0, y=0, DEATH=0, color=0):
        self.x = x
        self.y = y
        self.game = game
        self.r = 5
        self.game.energy += 1
        if self.x == 0 and self.y == 0:       #Создает шарик еды в случайном месте
            color = random.choice(self.game.COLORS)
            self.x = random.uniform(5, 9995)  #фиксить параметры окна
            self.y = random.uniform(5, 9995) 
            pygame.draw.circle(self.game.screen, color[2], (self.x, self.y), self.r + 4)
            pygame.draw.circle(self.game.screen, color[0], (self.x, self.y), self.r)
            pygame.draw.circle(self.game.screen, color[1], (self.x, self.y), self.r - 5)
        else:
            if Death !=0:          # Если змея умерла, создает большие шарики еды на месте змеи
                self.r = 25        # Например
                pygame.draw.circle(self.game.screen, color[2], (self.x, self.y), self.r + 4)
                pygame.draw.circle(self.game.screen, color[0], (self.x, self.y), self.r)
                pygame.draw.circle(self.game.screen, color[1], (self.x, self.y), self.r - 5)
            else:                  # Если змея оставляет след, генерит шарики еды
                pygame.draw.circle(self.game.screen, color[2], (self.x, self.y), self.r + 4)
                pygame.draw.circle(self.game.screen, color[0], (self.x, self.y), self.r)
                pygame.draw.circle(self.game.screen, color[1], (self.x, self.y), self.r - 5)
    def eaten(self, other):
        # Говорит скоко новых шариков создавать (нужно для наследования)
        pass
        
        
class Big_food(Food):
    def __init__(self, event):
        # может быть будет зависеть от чего-то другого, не знаю. В общем если кнопка мыши зажата, он выдет 3 (например)
        # если не зажата, то просто 1. Это коэффециент, на который будет умножаться наша конечная скорость.
        pass
        # Выглядит как большая еда, которая еще и двигается как-то интересно
        pass
    def move(self):
        # Она там как-то быстро движется, надо подумать как
        pass
    def something(self):
        # хз что это за штука
        pass
    def eaten(self, event):
        # Говорит скоко новых шариков создавать. Это число сильно больше чем при обычной еде.
        pass