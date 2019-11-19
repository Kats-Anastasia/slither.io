import random
import math
import pygame


class Food():
    def __init__(self, game, x=0, y=0, DEATH=0, color=0):
        self.x = x
        self.y = y
        self.game = game
        self.r = 5
        self.game.energy += 1
        if self.x == 0 and self.y == 0:       #Создает шарик еды в случайном месте
            color = random.choice(self.game.COLORS)
            self.x = random.uniform(5, 9995)
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
class Ball():
    def __init__(self, x, y, color, game, r=25):
        self.radius = r
        self.x = x
        self.y = y
        self.color = color
        self.game = game
        pygame.draw.circle(self.game.screen, color[0], (self.x, self.y), self.r)
    def move(self, other):
        # Вводишь предыдущий шарик (который ближе к башке) и он двигает новый. Движение змеи происходит с хвоста
        self.x = other.x
        self.y = other.y
        pygame.draw.circle(self.game.screen, color[0], (self.x, self.y), self.r)
    def grow(self, event=0):
        pass
class Head(Ball): # Мб это будет просто функцией в классе Ball
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
class Snake():
    def __init__(self, color, name, game):
        self.game = game
        self.color = color
        self.name = name
        self.x = 500
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
        # отвечает за создание начальной змеи начального размера, длины и всего такого. 

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
        
        
class game():
    self.white = (255, 255, 255)
    self.black = (0,0,0)

    self.orange = (249, 179, 130)
    self.orange1 = (253, 223, 204)
    self.orange2 = (123, 53, 6)
    
    self.red = (255, 55, 65)
    self.red1 = (255, 138, 145)
    self.red2 = (130, 0, 0)
    
    self.yellow = (247, 255, 94)
    self.yellow1 = (252, 255, 187)
    self.yellow2 = (81, 85, 0)
    
    self.green = (121, 227, 126)
    self.green1 = (213, 247, 215)
    self.green2 = (13, 64, 15)
    
    self.purple = (255, 77, 255)
    self.purple1 = (255, 166, 255)
    self.purple2 = (77, 0, 77)
    
    self.blue = (189, 205, 255)
    self.blue1 = (227, 235, 255)
    self.blue2 = (0, 27, 104)
    
    self.lightblue = (156, 249, 255)
    self.lightblue1 = (223, 254, 255)
    self.lightblue2 = (0, 81, 85)
    
    self.pink = (255, 202, 208)
    self.pink1 = (255, 238, 240)
    self.pink2 = (100, 0, 13)
    
    self.ORANGE = [self.orange, self.orange1, self.orange2]
    self.RED = [self.red, self.red1, self.red2]
    self.YELLOW = [self.yellow, self.yellow1, self.yellow2]
    self.GREEN = [self.green, self.green1, self.green2]
    self.PURPLE = [self.perple, self.perple1, self.perple2]
    self.BLUE = [self.blue, self.blue1, self.blue2]
    self.LIGHTBLUE = [self.lightblue, self.lightblue1, self.lightblue2]
    self.PINK = [self.pink, self.pink1, self.pink2]

    self.COLORS = [self.ORANGE, self.RED, self.YELLOW, self.GREEN, self.PERPLE, self.BLUE, self.LIGHTBLUE, self.PINK]
    
    self.energy = 0 #Штука, обозначающая полную энергию системы. Она складывается с некоторым коэффициентом из колличества шариков змеи, количества шариков еды, может быть чего-то еще)

    def __init__(self):
        # Туть рисуется начальный экран, где вводится Имя, выбирается цвет, нажимается кнопка старта игры.        
        pygame.init()
        self.screen = pygame.display.set_mode((1000,1000))
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
    
    
    
    
    
    
    
    
    
     