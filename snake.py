import pygame
import colors
import random
import Ball
import Snake

class Snake():
    def __init__(self, color, name, game):
        self.game = game
        self.color = color
        self.name = name
        self.x = 500 #мб внести в конфигу
        self.y = 500
        self.lenght = 0
        self.timer = 0
        self.balls = []
        head = Head(color=self.color, x=self.x, y=self.y, game=self.game, snake=self)
        self.balls += [head]
        self.leght += 1
        for i in range(50):
            new_ball = Ball(x=self.x + i, y=self.y, game=self.game, color=self.color)
            self.balls += [new_ball]
            self.lenght += 1
        for b in self.balls:
            if self.balls.index(b) > 0:
                b.move(self.balls[(self.balls.index(b) - 1)]
            else: b.move()
        # name - имя змеи, висящее над ней и которое вводится при запуске, тогда же выбирается и цвет.

    def targeting(self, event = 0): #Нужно объединить со следующей функцией
        pass
    
    def move(self):
        # Пока без поправки бонусов
        pass
        

    def hit(self):
        for s in self.game.snakes:
        # Чекает столкнулась ли наша башка с чьим-то туловищем. Только вот хз что делать если столкнулись две башки
        # Мб смотреть чей радиус вектор скорости под меньшим углом направлен к центру башки второй? Думою это лучше всего (правда блин как углы то считать?)
        # Затем самоуничтожается, превращается в большую еду каждый шарик змейки, ждет некоторое время и выкидывает на экран геймовера.
            pass
        pass
        
    def eat(self, other):
        # Чекает столкнулась ли башка с едой, создает новый шарик, убивает еду, мб что еще делает что я забыла
        pass
    
    def destroyed(self):
        #Уничтожет змею, на месте каждого шарика создает большую еду
        pass