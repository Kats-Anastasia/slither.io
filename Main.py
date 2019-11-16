import random
import math
import pygame
from game_object import GameObject

class Ball(GameObject):
    def __init__(self, x, y, r, color, speed):
        GameObject.__init__(self, 
                            x - r, 
                            y - r, 
                            r * 2, 
                            r * 2, 
                            speed)
        self.radius = r
        self.diameter = r * 2
        self.color = color

    def draw(self, surface):
        pygame.draw.circle(surface, 
                           self.color, 
                           self.center, 
                           self.radius)

class ball():
    def __init__(self, x, y, r, color, speed):
        GameObject.__init__(self, 
                            x - r, 
                            y - r, 
                            r * 2, 
                            r * 2, 
                            speed)
        self.radius = r
        self.diameter = r * 2
        self.color = color

        self.timer = 0

    def draw(self, surface):
        pygame.draw.circle(surface, 
                           self.color, 
                           self.center, 
                           self.radius)
        # Вводишь координаты x и y центра шарика, он генерит шарик, больше ничего не делает
        
    def move(self, other):
        # Вводишь предыдущий шарик (который ближе к бошке) и он двигает новый. Движение змеи происходит с хвоста
        self.x = other.x
        self.y = other.y
        
    def grow(self, ivent=0):
        pass
    
class head(ball): # Мб это будет просто функцией в классе Ball
    def __init__(self, x, y, r = 10):
        pass

class meal():
    def __init__(self, x=0, y=0, r=2):
        self.x = x
        self.y = y
        self.r = r
        self.timer = 0
        if x == 0 and y == 0:
            #Создает шарик в случайном месте
            pass
        else:
            #Создает большой шарик на месте сдохшей змеи
            pass

    def pulsation(self):
        # Мерцание
        pass

    def move(self):
        # Медленное движение по кругу
        pass

    def eaten(self, other):
        # Говорит скоко новых шариков создавать (нужно для наследования)
        pass


class big_meal(food):
    def __init__(self, ivent):
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


class snake(window):
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.x = 500
        self.y = 500
        
        self.balls = []
        self.an = 0
        self.timer = 0
        for i in range(50):
            pass
        # name - имя змеи, висящее над ней и которое вводится при запуске, тогда же выбирается и цвет.
        # отвечает за создание начальной змеи начального размера, длины и всего такого. 

    def targeting(self, event = 0): #Нужно объединить со следующей функцией
        if event:
            self.an = math.atan2((event.y-self.y), (event.x-self.x))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )
    
    def move(self):
        # Запускает бонусы
        # Двигает змею с поправками бонусов
        pass

    def hit(self, other):
        # Чекает столкнулась ли наша башка с чьим-то туловищем. Только вот хз что делать если столкнулись две башки
        # Мб смотреть чей радиус вектор скорости под меньшим углом направлен к центру башки второй? Думою это лучше всего (правда блин как углы то считать?)
        # Затем самоуничтожается, превращается в большую еду каждый шарик змейки, ждет некоторое время и выкидывает на экран геймовера.
        pass
    
    def eat(self, other):
        # Чекает столкнулась ли башка с едой, создает новый шарик, убивает еду, мб что еще делает что я забыла
        pass
    
    def destroyed(self):
        #Уничтожет змею, на месте каждого шарика создает большую еду

class game():
    def __init__(self):
        # Туть рисуется начальный экран, где вводится Имя, выбирается цвет, нажимается кнопка старта игры.        
        pygame.init()
        screen = pygame.display.set_mode(1000,1000)
        start = True
        self.color = 0
        self.name = 0
        while start: # Может лучше не так, а просто чтобы он ждал пока не произойдет событие. Но я не знаю как это сделать
            for i in pygame.event.get():
                # if i.type == pygame. # Штука, отвечающая за нажатие кнопки
                start = false
                pass
            # Тут еще хуйня, которая выполняет выбор цвета змеи, вводит название
            pygame.time.delay(20)
        self.start_game(name=self.name, color=self.color)

    def start_game(self, name, color):
        screen = pygame.display.set_mode(1000,1000)
        clock = pygame.time.Clock()
        self.name = name
        self.color = color
        new_snake = snake(name=self.name, color=self.color)
        snakes = []
        snakes += new_snake
        self.meals = []
        for i in range (100): # Столько еды создастся изначально
             new_meal = meal()
             self.meals += new_meal()

        process = True
        meal.timer = 0
        while process:
            snake.timer += 1 # (ну или сколько там (возможно, таймер не нужен, а он будет только на фишки еды)
            meal.timer += 1
            for s in snakes:
                s.move()
            if meal.timer >= 5: # Ну или сколько там (Если нужно меньше, можно просто создавать много шариков еды за раз)
                new_meal = meal()
                self.meals += new_meal
            for s in snakes:
                for l in snakes:
                    if l != s:
                        if s.hit(l):
                            s.destroyed() 
                            # Для нужной змейки выход из экрана, но возможно здесь вообще надо по-другому писать, надо чекать как работает это все по сети
            pygame.time.delay(200) #Ну или сколько там нужно времени (между движениями змейки)

new_game = game()
    
    
    
    
    
    
    
    
    
     