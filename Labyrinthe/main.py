# -*- coding: utf8 -*-

import re


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
        character_control = re.findall("(?i)z|q|s|d", direction)
        if (character_control) :
                print(direction)
                return (direction)
        else:
                user_input()

def player_movement(x, y, direction):
        if direction == "d":
                x += 1
                print(x)
                return(x, y)
        elif direction == "z":
                y -= 1
                return (x, y)
        elif direction == "q":
                x -= 1
                return(x, y)
        elif direction == "s":
                y += 1
                return(x, y)
        else:
                pass


def main():
        course = []
        course_file = "parcours"
        direction ="a"
        x = 1
        y = 1
        course = read_file(course_file)
        course[y][x] = "p"
        lab_display(course)
        direction = user_input()
        course[y][x] = " "
        x, y = (player_movement(x,y, direction))
        print(x, y)
        course[y][x] = "x"
        print(direction)
        lab_display(course)


main()

#while course[15][10] != "p" :
 #       direction = input("Dans quelle direction souhaitez-vous aller ?")
  #      if direction = "z":
   #             if 


