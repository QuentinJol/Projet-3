# -*- coding: utf8 -*-

import re
from random import randint
import os
import pygame
from pygame.locals import *

pygame.init()

BACKGROUND_COLOR = 0, 100, 255
policie_text = pygame.font.SysFont('freesans', 20)
score_text = "Player's objects :"
text = policie_text.render(score_text, True, BACKGROUND_COLOR)
textpos = text.get_rect()
textpos.centerx = 840
textpos.centery = 25

window = pygame.display.set_mode((950, 760), RESIZABLE)
window.blit(text, textpos)
floor = pygame.image.load("ressources/floor.png").convert()
floor = pygame.transform.scale(floor, (50, 50))
wall = pygame.image.load("ressources/wall.png").convert()
wall = pygame.transform.scale(wall, (50, 50))
guard = pygame.image.load("ressources/Guardian.png").convert()
guard = pygame.transform.scale(guard, (50, 50))
gamer = pygame.image.load("ressources/MacGyver.png").convert()
gamer = pygame.transform.scale(gamer, (50, 50))
object1 = pygame.image.load("ressources/ether50.png").convert()
object2 = pygame.image.load("ressources/seringue50.png").convert()
object3 = pygame.image.load("ressources/aiguille50.png").convert()



class Map :

        def __init__(self, file):

                self.file = file
                self.course = []

        def read_file(self):
                """
                Check and reading function for labyrinthe file
                """

                try :
                        with open(self.file, 'r') as fichier:
                                temp_list = []
                                temp_list2 = []
                                temp_list=(fichier.read().splitlines())
                                for line in temp_list:
                                        temp_list2.append(list(line.strip()))   
                        self.course = temp_list2
                except IOError:
                        print("Erreur! Le fichier \"parcours\" n'a pas pu être ouvert.")
                        quit()
                
        def player_start_position(self, x, y):
                """
                Player's start positionning function
                """
                self.course[y][x] = "p"


        def lab_display_graphic(self, window):
                """
                Display labytrinthe with PyGame function
                """
                mapping = {"a" : object1, "b" : object2, "c" : object3, "G" : guard, "p" : gamer, "#" : wall, " " : floor}
                for y, row in enumerate(self.course):
                        for x, case in enumerate(row):
                                if case in mapping:
                                        window.blit(mapping[case], (x*50, y*50))



        def lab_display(self):
                """
                Display labyrinthe function
                """
                for line in self.course:
                        print(''.join(line))



        def objects_position(self):
                """
                Objects positioning in labyrinthe
                """
                i = 0
                y = 1
                x = 1 
                objects = ["a", "b", "c"]  
                while i < 3 :
                        y = randint(2, 14)
                        x = randint(1, 14)
                        if self.course[y][x] == " " :
                                self.course[y][x]= objects[i]
                                i += 1


        def guardian_control(self, x, y, objects):
                """
                Guardian control function for the game finish
                """
                if self.course[y][x+1] == "G" or self.course[y][x-1] == "G" :
                        if "a" in objects and "b" in objects and "c" in objects:
                                print("Vous avez gagné !!!")
                                return True
                        else :
                                print("Vous avez perdu !")
                                return True


class Player:

        def __init__(self, x, y, lab, objects):

                self.x = x
                self.y = y
                self.objects = []
                self.lab = lab
                

        def user_input(self):
                """
                User input function for direction
                """
                for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP or pygame.K_DOWN or pygame.K_RIGHT or pygame.K_LEFT:
                                        return (event.key)


        def player_movement(self, player):
                for event in pygame.event.get():
                        if event.type == KEYDOWN:
                                if event.key == K_RIGHT and self.lab.course[self.y][self.x + 1] in [" ", "a", "b", "c"]: 
                                        self.lab.course[self.y][self.x] = " "
                                        self.x += 1
                                        player.objects_capture()
                                        self.lab.course[self.y][self.x] = "p" 
                                elif event.key == K_UP and self.lab.course[self.y - 1][self.x] in [" ", "a", "b", "c"]:
                                        self.lab.course[self.y][self.x] = " "
                                        self.y -= 1
                                        player.objects_capture()
                                        self.lab.course[self.y][self.x] = "p" 
                                elif event.key == K_LEFT and self.lab.course[self.y][self.x - 1] in [" ", "a", "b", "c"]:
                                        self.lab.course[self.y][self.x] = " "
                                        self.x -= 1
                                        player.objects_capture()
                                        self.lab.course[self.y][self.x] = "p" 
                                elif event.key == K_DOWN and self.lab.course[self.y + 1][self.x] in [" ", "a", "b", "c"]:
                                        self.lab.course[self.y][self.x] = " "
                                        self.y += 1
                                        player.objects_capture()
                                        self.lab.course[self.y][self.x] = "p" 
                                if event.type in [QUIT, K_ESCAPE]:
                                        return guardian == True
                                return(self.x, self.y)

        def objects_capture(self):
                if self.lab.course[self.y][self.x] == "a":
                        self.objects.append("a")
                        return self.objects
                if self.lab.course[self.y][self.x] == "b":
                        self.objects.append("b")
                        return self.objects
                if self.lab.course[self.y][self.x] == "c":
                        self.objects.append("c")
                        return self.objects
                return self.objects

        def objects_display(self, window):
                if "a" in self.objects :
                        textposa = text.get_rect()
                        textposa.centerx = 840
                        textposa.centery = 55
                        texta = policie_text.render("- Ether", True, BACKGROUND_COLOR)
                        window.blit(texta, textposa)
                if "b" in self.objects :
                        textposb = text.get_rect()
                        textposb.centerx = 840
                        textposb.centery = 75
                        textb = policie_text.render("- Seringue", True, BACKGROUND_COLOR)
                        window.blit(textb, textposb)
                if "c" in self.objects :
                        textposc = text.get_rect()
                        textposc.centerx = 840
                        textposc.centery = 95
                        textc = policie_text.render("- Aiguille", True, BACKGROUND_COLOR)
                        window.blit(textc, textposc)                                                
                return window



                                

def main():
        # run = True
        labyrinthe = Map("parcours")
        guardian = False
        labyrinthe.read_file()
        player1 = Player(1, 1, labyrinthe, "")
        labyrinthe.player_start_position(player1.x, player1.y)
        labyrinthe.objects_position()
        labyrinthe.lab_display_graphic(window)
        pygame.display.flip()

        # while run :
        #         for event in pygame.event.get():
        #                 if event.type == pygame.QUIT:
        #                         run = False
        while not guardian :
                player1.player_movement(player1)
                labyrinthe.lab_display_graphic(window)
                player1.objects_display(window)
                pygame.display.flip()
                guardian = labyrinthe.guardian_control(player1.x, player1.y, player1.objects)
                




main()

