import pygame
from pygame.locals import *
import time
import random

import pygame.surface

SIZE=40
background_color=(110,110,5)

class Apple:
    def __init__(self,parent_screen):
        self.image=pygame.image.load("assets/apple (1).jpg").convert()
        self.parent_screen=parent_screen
        self.x = SIZE*3
        self.y = SIZE*3
    def draw(self):
        self.parent_screen.blit(self.image,(self.x,self.y))        
        pygame.display.flip()

    def move(self):
        self.x=random.randint(0,31)*SIZE
        self.y=random.randint(0,17)*SIZE


class Snake:
    def __init__(self, parent_screen,length):
        self.length = length
        self.parent_screen=parent_screen
        self.block=pygame.image.load("assets/block.jpg").convert()
        self.direction="down"
        self.x=[SIZE]*length
        self.y=[SIZE]*length
    
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

   
   
    def draw(self):
        # self.parent_screen.fill(background_color)
        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))        
        pygame.display.flip()

    def move_left(self):
        self.direction="left"
    def move_right(self):
        self.direction="right"
    def move_up(self):
        self.direction="up"
    def move_down(self):
        self.direction="down"

    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        if self.direction =="up":
            self.y[0] -=SIZE
        if self.direction =="down":
            self.y[0] +=SIZE
        if self.direction =="right":
            self.x[0] +=SIZE
        if self.direction =="left":
            self.x[0] -=SIZE
        
        self.draw() 

        


class GAME:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("DPP Snake and Apple Game")

        pygame.mixer.init()
        self.play_background_music()

        self.screen = pygame.display.set_mode((1280, 720))
        self.snake=Snake(self.screen,1)
        self.snake.draw()
        self.apple= Apple(self.screen)
        self.apple.draw()
    
    
    def is_collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1 < x2 + SIZE:
             if y1 >= y2 and y1 < y2 + SIZE:
                return(True)
        return(False)

 
    def display_score(self):
        font = pygame.font.SysFont('arial',30)
        score = font.render(f"Score: {self.snake.length}", True,(255,255,255))
        self.screen.blit(score,(1100,10))
    

    def play_background_music(self):
        pygame.mixer.music.load("assets/bg_music_1 (1).mp3")
        pygame.mixer.music.play()
    
    def render_background(self):
        bg=pygame.image.load("assets/background.jpg")
        self.screen.blit(bg,(0,0))
    
    def play(self):
         self.render_background() 
         self.snake.walk()
         self.apple.draw()
         self.display_score()
         pygame.display.flip()
    

         #Snake colliding with apple
         if self.is_collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            sound=pygame.mixer.Sound("assets/ding.mp3")
            pygame.mixer.Sound.play(sound)
            self.snake.increase_length()
            self.apple.move()

         # Snake colliding itself
         for i in range(1,self.snake.length):
            if self.is_collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                sound=pygame.mixer.Sound("assets/crash.mp3")
                pygame.mixer.Sound.play(sound)
                raise "Game Over"
        # snake colliding with the boundries of the window
         if not (0 <= self.snake.x[0] <= 1280 and 0 <= self.snake.y[0] <= 720):
                sound=pygame.mixer.Sound("assets/crash.mp3")
                pygame.mixer.Sound.play(sound)
                raise "Hit the boundry error"
        
    def show_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial',30)
        line1=font.render(f"Game is over! Your score is {self.snake.length}", True,(255,255,255) )
        self.screen.blit(line1,(450,260))
        line2=font.render("To play the game again press Enter. To exit press Escape: ",True,(255,255,255))
        self.screen.blit(line2,(300,300))
        pygame.display.flip()

        pygame.mixer.music.pause()

    def reset(self):
        self.snake=Snake(self.screen,1)
        self.apple= Apple(self.screen)

    def run(self):
        running=True
        pause=False

        while running:
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running=False
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.unpause()
                        pause=False
                    if not pause:
                        if event.key==pygame.K_DOWN:
                            self.snake.move_down()
                        if event.key==pygame.K_UP:
                            self.snake.move_up()
                        if event.key==pygame.K_LEFT:
                            self.snake.move_left()
                        if event.key==pygame.K_RIGHT:
                            self.snake.move_right()
                
                elif event.type==pygame.QUIT:
                    running=False 
            try:
                if not pause:
                    self.play()
            except Exception as e :
                self.show_game_over()
                self.reset()
                pause=True

            
            time.sleep(0.1)
                
    
 

if __name__=="__main__":
    game = GAME()
    game.run()



    

   
    


