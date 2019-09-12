# -*- coding: utf8 -*-

import re
from random import randint
import os
import pygame
from pygame.locals import *


class Map :

        def __init__(self, file):

                self.file = file


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
                        return temp_list2
                except IOError:
                        print("Erreur! Le fichier \"parcours\" n'a pas pu être ouvert.")
                        quit()
                
        def player_start_position(self, x, y, course):
                course[y][x] = "p"
                return(course)



        def lab_display(self, course : list):
                """
                Display labyrinthe function
                """
                for line in course:
                        print(''.join(line))


        def objects_position(self, course : list):
                """
                Objects positioning in labyrinthe
                """
                i = 0
                y = 1
                x = 1   
                while i < 3 :
                        y = randint(1, 15)
                        x = randint(1, 15)
                        if course[y][x] == " " :
                                course[y][x]= "o"
                                i += 1
                return course


        def guardian_control(self, x, y, course, objects, guardian):
                if course[y][x+1] == "G" or course[y][x-1] == "G" :
                                if objects == 3:
                                        guardian = 1
                                        print("Vous avez gagné !!!")
                                        return guardian
                                else :
                                        guardian = 1
                                        print("Vous avez perdu !")
                                        return guardian


class Player:

        def __init__(self, x, y, course, direction, objects):

                self.x = x
                self.y = y
                self.objects = objects

        def user_input(self):
                """
                User input function for direction
                """
                direction = input("Dans quelle direction souhaitez-vous aller ?(Z, Q, S ou D pour jouer)")
                direction = direction.lower()
                character_control = re.search("z|q|s|d", direction)
                if (character_control) :
                        return (direction)
                Player.user_input(self)

        def player_movement(self, course, direction):
                if direction == "d" and course[self.y][self.x + 1] in [" ", "o"]: 
                        self.x += 1    
                elif direction == "z" and course[self.y - 1][self.x] in [" ", "o"]:
                        self.y -= 1
                elif direction == "q" and course[self.y][self.x - 1] in [" ", "o"]:
                        self.x -= 1
                elif direction == "s" and course[self.y + 1][self.x] in [" ", "o"]:
                        self.y += 1
                return(self.x, self.y)

        def objects_capture(self, course):
                if course[self.y][self.x] == "o":
                        self.objects += 1
                        print("Vous avez acquis un objet")
                        return self.objects
                return self.objects


                                

def main():
        course = Map("parcours")
        direction ="a"
        guardian = 0
        objects = 0
        x = 1
        y = 1
        lab = course.read_file
        lab = course.player_start_position(x, y, course)
        lab = course.objects_position(course)
        print (lab)
        # while guardian != 1 :
        #         print("\n")
        #         direction = user_input()
        #         course[y][x] = " "
        #         x, y = (player_movement(x,y, course, direction))
        #         objects = objects_capture(x, y, course, objects)
        #         course[y][x] = "p"
        #         os.system("clear")
        #         lab_display(course)
        #         guardian = guardian_control(x, y, course, objects, guardian)



main()

