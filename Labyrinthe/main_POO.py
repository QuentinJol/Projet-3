# -*- coding: utf8 -*-

import re
from random import randint
import os
import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((600, 480), RESIZABLE)
floor = pygame.image.load("ressources/floor.png").convert()
wall = pygame.image.load("ressources/wall.png").convert()
guard = pygame.image.load("ressources/guard.png").convert()
gamer = pygame.image.load("ressources/MacGyver20px.png").convert()
object1 = pygame.image.load("ressources/ether20.png").convert()
object2 = pygame.image.load("ressources/seringue20.png").convert()
object3 = pygame.image.load("ressources/aiguille20.png").convert()
# window.blit(floor, (0, 0))                

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
                self.course[y][x] = "p"

        def lab_display_graphic(self, window):
                y = 0
                i = 1
                while y < 17 :
                        x = 0
                        for value in self.course[y]:
                                if value == "a" :
                                        window.blit(object1, (x*20, y*20))
                                if value == "b" :
                                        window.blit(object2, (x*20, y*20))
                                if value == "c" :
                                        window.blit(object3, (x*20, y*20))
                                if value == "G" :
                                        window.blit(guard, (x*20, y*20))  
                                if value == "p":
                                        window.blit(gamer, (x*20, y*20))
                                if value == "#" :
                                        window.blit(wall, (x*20, y*20))
                                if value == " " :
                                        window.blit(floor, (x*20, y*20))           
                                x += 1 
                        y += 1


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
                        y = randint(1, 15)
                        x = randint(1, 15)
                        if self.course[y][x] == " " :
                                self.course[y][x]= objects[i]
                                i += 1


        def guardian_control(self, x, y, objects):
                if self.course[y][x+1] == "G" or self.course[y][x-1] == "G" :
                        if objects == 3:
                                print("Vous avez gagné !!!")
                                return True
                        else :
                                print("Vous avez perdu !")
                                return True


class Player:

        def __init__(self, x, y, lab, objects):

                self.x = x
                self.y = y
                self.objects = objects
                self.lab = lab
                

        def user_input(self):
                """
                User input function for direction
                """
                direction = input("Dans quelle direction souhaitez-vous aller ?(Z, Q, S ou D pour jouer)")
                direction = direction.lower()
                character_control = re.search("z|q|s|d", direction)
                if (character_control) :
                        return (direction)
                self.user_input()

        def player_movement(self):
                direction = self.user_input()
                if direction == "d" and self.lab.course[self.y][self.x + 1] in [" ", "o"]: 
                        self.lab.course[self.y][self.x] = " "
                        self.x += 1
                        self.lab.course[self.y][self.x] = "p" 
                elif direction == "z" and self.lab.course[self.y - 1][self.x] in [" ", "o"]:
                        self.lab.course[self.y][self.x] = " "
                        self.y -= 1
                        self.lab.course[self.y][self.x] = "p" 
                elif direction == "q" and self.lab.course[self.y][self.x - 1] in [" ", "o"]:
                        self.lab.course[self.y][self.x] = " "
                        self.x -= 1
                        self.lab.course[self.y][self.x] = "p" 
                elif direction == "s" and self.lab.course[self.y + 1][self.x] in [" ", "o"]:
                        self.lab.course[self.y][self.x] = " "
                        self.y += 1
                        self.lab.course[self.y][self.x] = "p" 
                return(self.x, self.y)

        def objects_capture(self):
                if self.lab.course[self.y][self.x] == "o":
                        self.objects += 1
                        print("Vous avez acquis un objet")
                        return self.objects
                return self.objects


                                

def main():
        labyrinthe = Map("parcours")
        guardian = False
        labyrinthe.read_file()
        player1 = Player(1, 1, labyrinthe, 0)
        labyrinthe.player_start_position(player1.x, player1.y)
        labyrinthe.objects_position()
        labyrinthe.lab_display()
        labyrinthe.lab_display_graphic(window)
        pygame.display.flip()
        while not guardian :
                print("\n")
                player1.player_movement()
                player1.objects_capture()
                os.system("clear")
                labyrinthe.lab_display()
                labyrinthe.lab_display_graphic(window)
                pygame.display.flip()
                guardian = labyrinthe.guardian_control(player1.x, player1.y, player1.objects)



main()

