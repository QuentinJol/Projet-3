# -*- coding: utf8 -*-

import re
from random import randint
import os
import pygame
from pygame.locals import *


def file_control(file):
        try:
                with open(file):
                        pass
        except IOError:
                print("Erreur! Le fichier n' pas pu être ouvert")

def read_file(file):
        """
        Reading function for labyrinthe file
        """
        with open(file, 'r') as fichier:
                temp_list = []
                temp_list2 = []
                temp_list=(fichier.read().splitlines())
                for line in temp_list:
                        temp_list2.append(list(line.strip()))   
        return temp_list2



def objects_position(course):
        """
        Objects positioning in labyrinthe
        """
        i = 0
        y = 0
        x = 0    
        while i < 3 :
                y = randint(1, 15)
                x = randint(1, 15)
                if course[y][x] == " " :
                        course[y][x]= "o"
                        i += 1


def lab_display(course):
        """
        Display labyrinthe function
        """
        for line in course:
                print(''.join(line))

def user_input():
        """
        User input function for direction
        """
        direction = input("Dans quelle direction souhaitez-vous aller ?(Z, Q, S ou D pour jouer)")
        direction = direction.lower()
        character_control = re.search("z|q|s|d", direction)
        if (character_control) :
                return (direction)
        user_input()

def player_movement(x, y, direction, course):
        if direction == "d" and course[y][x + 1] in [" ", "o"]: 
                x += 1    
        elif direction == "z" and course[y - 1][x] in [" ", "o"]:
                y -= 1
        elif direction == "q" and course[y][x - 1] in [" ", "o"]:
                x -= 1
        elif direction == "s" and course[y + 1][x] in [" ", "o"]:
                y += 1
        return(x, y)

def objects_capture(x, y, course, objects):
        if course[y][x] == "o":
                objects += 1
                print("Vous avez acquis un objet")
                return objects
        return objects

def guardian_control(x, y, course, objects, guardian):
         if course[y][x+1] == "G" or course[y][x-1] == "G" :
                        if objects == 3:
                                guardian = 1
                                print("Vous avez gagné !!!")
                                return guardian
                        else :
                                print("Vous avez perdu !")
                                quit()
                                

def main():
        course = []
        course_file = "parcours"
        direction ="a"
        guardian = 0
        objects = 0
        x = 1
        y = 1
        file_control(course_file)
        course = read_file(course_file)
        course[y][x] = "p"
        objects_position(course)
        lab_display(course)
        while guardian != 1 :
                print("\n")
                direction = user_input()
                course[y][x] = " "
                x, y = (player_movement(x,y, direction, course))
                objects = objects_capture(x, y, course, objects)
                course[y][x] = "p"
                os.system("clear")
                lab_display(course)
                guardian = guardian_control(x, y, course, objects, guardian)



main()

