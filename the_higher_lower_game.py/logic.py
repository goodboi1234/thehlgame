import pygame
import sys
from dict_data import most_searched_google as data
import random

class logic(pygame.sprite.Sprite):
    def __init__(self , group , screen):
        super().__init__(group)
        self.val()
        self.screen = screen
        self.text = "thanks for playing the game"
        self.font = pygame.font.SysFont("fonts/test/easvhs.ttf" , 36)
        self.inst = "press 'h' for high or 'l' for low"
        self.play = True
        self.count = 0
        self.high = pygame.image.load("/Users/zeeldarji/Desktop/python files/the_higher_lower_game.py/bg/Screenshot 2024-01-08 at 3.02.49 PM.png")
        self.low = pygame.image.load("/Users/zeeldarji/Desktop/python files/the_higher_lower_game.py/bg/Screenshot 2024-01-08 at 3.04.29 PM.png")
        self.high_rect = self.high.get_rect(center = (150 , 100))
        self.low_rect = self.low.get_rect(center = (550 , 100))

    def val(self):
        self.k1 , self.v1 = random.choice(list(data.items()))
        while True:
            self.k2 , self.v2 = random.choice(list(data.items()))
            if self.k2 != self.k1 and self.v2 != self.v1:
                break
            else:
                continue

    #the interaction
    def interaction(self):
        posi = pygame.mouse.get_pos()
        self.text = f"do you think {self.k2} is more searched then {self.k1} or less searched"
        if (posi[0]<=self.high_rect.right and posi[0]>= self.high_rect.left) and\
            (posi[1]<= self.high_rect.bottom and posi[1] >= self.high_rect.top)\
            and self.v2 <=self.v1:
            print("you won")
            self.text = "you are right"
            self.play = True
            self.count+=1
        if pygame.mouse.get_pos() == (550 , 100) and pygame.mouse.get_pressed()[0] and self.v2 >= self.v1:
            print("you won")
            self.text = "you are right"
            self.play = True
            self.count +=1
            pygame.event.clear(pygame.key.get_pressed())
        if (posi[0] <= self.high_rect.right and posi[0] >= self.high_rect.left) and\
              (posi[1] <= self.high_rect.bottom and posi[1] >= self.high_rect.top) and\
                self.v2 >= self.v1:
                print("sorry, you lost")
                self.play = False
            
        if pygame.mouse.get_pos() == (550 , 100) and pygame.mouse.get_pressed()[0] and self.v2<=self.v1:
            print("you lost")
            self.play = False
            pygame.event.clear(pygame.key.get_pressed())
        if self.play == True and self.text == "you are right":
            self.k1 = self.k2
            self.v1 = self.v2
            while True:
                self.k2 , self.v2 = random.choice(list(data.items()))
                if self.k2 != self.k1 and self.v2!= self.v1:
                    break
                else:
                    continue
            self.play = False

        if self.play == False:
            self.text = f"sorry you lost, your total lscore is {self.count}"

    def update(self):
        #RENDERING THE TEXTS INTO THE FONT
        self.t  = self.font.render(self.text , True , (255 , 255  , 255))
        self.change = self.font.render(self.inst , True , (255 , 0 , 0))
        self.screen.blit(self.t , (100 , 200))
        self.screen.blit(self.change , (600 , 100))
        self.screen.blit(self.high , self.high_rect)
        self.screen.blit(self.low , self.low_rect)
        self.interaction()
        if pygame.key.get_pressed()[pygame.K_h] or pygame.key.get_pressed()[pygame.K_l]:
            print("hm")