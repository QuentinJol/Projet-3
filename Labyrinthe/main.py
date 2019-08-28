# -*- coding: utf8 -*-

import re
from random import randint


def read_file(file):
        """
        Reading function for Labyrinthe file
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
        Objects position in labyrinthe
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
                else :
                        pass

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
        else:
                user_input()

def player_movement(x, y, direction, course):
        if direction == "d" and course[y][x + 1] == " ": 
                x += 1    
        elif direction == "z" and course[y - 1][x] == " ":
                y -= 1
        elif direction == "q" and course[y][x - 1] == " ":
                x -= 1
        elif direction == "s" and course[y + 1][x] == " ":
                y += 1
        return(x, y)

def objects_capture(objects, course, x, y):
        if course[y+1][x] == "o" or course[y-1][x] == "o" or course[y][x+1] == "o" or course[y][x-1] == "o" :
                objects += 1
                print("Vous avez acquis un objet")
                return objects
        else :
                pass

def main():
        course = []
        course_file = "parcours"
        direction ="a"
        gardien = 0
        objects = 0
        x = 1
        y = 1
        course = read_file(course_file)
        course[y][x] = "p"
        objects_position(course)
        lab_display(course)
        while gardien != 1 :
                direction = user_input()
                course[y][x] = " "
                x, y = (player_movement(x,y, direction, course))
                course[y][x] = "p"
                objects_capture(objects, course, x, y)
                if course[y+1][x] == "G" or course[y-1][x] == "G" or course[y][x+1] == "G" or course[y][x-1] == "G" :
                        if objects == 3:
                                gardien += 1
                                print("Vous avez gagné !!!")
                                break
                        else :
                                print("Vous avez perdu !")
                                break
                lab_display(course)


main()

