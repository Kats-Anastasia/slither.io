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

class window():
    def __init__(self):
        pass
    def start_game(self, ivent=0)
        pygame.init()
        screen = pygame.display.set_mode((800, 600))
        clock = pygame.time.Clock()
        background_image = pygame.image.load('images/background2.jpg') # не сработает, так как фотка не ежит там где нужно (А это где?)
        while True:
            screen.fill((192, 192, 192))
            pygame.display.update()
            clock.tick(60)
    # Хз как эта штука работает, должна создавать окно с заставкой, где можно ввести имя и выбрать цвет этой гусеницы-змеи-крокодила
    # Мб в этом классе, мб в другом само окно игровое, на котором генерируется все (уже в игре, не заставка)


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
        
    def grow(self, ivent=0)
        
    
class head(ball):
    def __init__(self, x, y, r = 10)

class meal():
    def __init__(self, x, y, r=2):
        self.x = x
        self.y = y
        self.r = r
        self.timer = 0

    def pulsation(self):
        # Мерцание

    def move(self):
        # Медленное движение по кругу

    def eaten(self, other):
        # Говорит скоко новых шариков создавать (нужно для наследования)
        pass


class big_meal(food):
    def __init__(self, ivent):
        # может быть будет зависеть от чего-то другого, не знаю. В общем если кнопка мыши зажата, он выдет 3 (например)
        # если не зажата, то просто 1. Это коэффециент, на который будет умножаться наша конечная скорость.
        
        # Выглядит как большая еда, которая еще и двигается как-то интересно
        pass
    def move(self):
        # Она там как-то быстро движется, надо подумать как
        pass
    def something(self):
        # хз что это за штука
    def eaten(self, event):
        # Говорит скоко новых шариков создавать. Это число сильно больше чем при обычной еде.
        pass


class snake():
    def __init__(self, color, name):
        self.color = color
        self.name = name
        self.x = 500
        self.y = 500
        
        self.balls = []
        self.an = 0
        
        for i in range(50):
            x1 = 
        # name - имя змеи, висящее над ней и которое вводится при запуске, тогда же выбирается и цвет.
        # отвечает за создание начальной змеи начального размера, длины и всего такого. 

    def targeting(self, event = 0)
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


class new_game(): # Делает дохуя всего, прописывать будем ближе к концу, либо наоборот в начале.
    def __init__():
        self.meals = []
        
        Nastya = snake(color='blue', name="Отпочковаться")
        Masha = snake(color='green', name="Хрючево")
        Dasha = snake(color='pink', name="Живи")
        
        # Допустим, мы создали поле 1000*1000
        
        for i in range(500): # создаем кучу еды начальной
            x1 = random.randrange(10, 990)
            y1 = random.randrange(10, 990)
            new_meal = meal(x=x1, y=y1)
            meals += [new_meal]
        
        
    
    
    
    
    
    
    
    
    
     