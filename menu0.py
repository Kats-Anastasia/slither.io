import pygame
import config   
import colors

'''черновик для меню'''


background = pygame.display.set_mode((config.screen_width, config.screen_height))
background.fill((картин0чка))#хз 

# поверхность, на которой будет отображаться название игры 
#просто существует, точно никуда вносить
name = pygame.Surface((400, 80))
name.fill(colors.green)
name.set_alpha(224)#прозрачность
background.blit(name,(200,120))
#текст названия игры
f_name = pygame.font.Font(None, 36)
text_name1 = f_name.render('slither', 1, (colors.green))
text_name2 = f_name.render('.oi', 1, (colors.purple))
background.blit(text_name1, (200, 120))#фиксить координаты
background.blit(text_name2, (500, 120))#фиксить координаты



# куда прилепим кнопку play
play = pygame.Surface((160, 80))
play.fill(green)
surf.set_alpha(99)#прозрачность
background.blit(play,(320,400))
#слово плэй
f_play = pygame.font.SysFont('serif', 20)
text_play = f_play.render("Play", 0, (white)) 


        
 

        
 

 

 
