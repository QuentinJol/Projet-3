# -*- coding: utf8 -*-

"""
Classes for Labyrinthe game
"""

from random import randint
import sys
import pygame
from pygame.locals import K_DOWN, K_ESCAPE, KEYDOWN, K_UP, K_LEFT, K_RIGHT, RESIZABLE


pygame.init()

PLAYER_OBJECT_COLOR = 0, 100, 255
FINISH_TEXT_COLOR = 200, 0, 0
SCORE_TEXT = "Player's objects :"
PLAYER_OBJECT_POLICIE = pygame.font.SysFont("freesans", 20)
FINISH_TEXT_POLICIE = pygame.font.SysFont("freesans", 70)
TEXT = PLAYER_OBJECT_POLICIE.render(SCORE_TEXT, True, PLAYER_OBJECT_COLOR)
TEXTPOS = TEXT.get_rect()
TEXTPOS.centerx = 840
TEXTPOS.centery = 25
WINDOW = pygame.display.set_mode((950, 760), RESIZABLE)
WINDOW.blit(TEXT, TEXTPOS)


class Map:
    """
    Class for the labyrinthe's map management
    """

    def __init__(self, file):

        self.file = file
        self.course = []
        self.floor = pygame.image.load("ressources/floor.png").convert()
        self.floor = pygame.transform.scale(self.floor, (50, 50))
        self.wall = pygame.image.load("ressources/wall.png").convert()
        self.wall = pygame.transform.scale(self.wall, (50, 50))
        self.guard = pygame.image.load("ressources/Guardian.png").convert()
        self.guard = pygame.transform.scale(self.guard, (50, 50))
        self.gamer = pygame.image.load("ressources/MacGyver.png").convert()
        self.gamer = pygame.transform.scale(self.gamer, (50, 50))
        self.object1 = pygame.image.load("ressources/ether50.png").convert()
        self.object2 = pygame.image.load("ressources/seringue50.png").convert()
        self.object3 = pygame.image.load("ressources/aiguille50.png").convert()

    def read_file(self):
        """
            Check and reading function for labyrinthe file
        """

        try:
            with open(self.file, "r") as temp_file:
                temp_list = []
                temp_list = temp_file.read().splitlines()
                for line in temp_list:
                    self.course.append(list(line.strip()))
        except IOError:
            print('Erreur ! \nLe fichier "parcours" n\'a pas pu être ouvert.')
            sys.exit()

    def player_start_position(self, x, y):
        """
            Player's start positionning function
        """
        self.course[y][x] = "p"

    def lab_display_graphic(self):
        """
            Display labytrinthe with PyGame function
        """

        mapping = {
            "a": self.object1,
            "b": self.object2,
            "c": self.object3,
            "G": self.guard,
            "p": self.gamer,
            "#": self.wall,
            " ": self.floor,
        }
        for y, row in enumerate(self.course):
            for x, case in enumerate(row):
                if case in mapping:
                    WINDOW.blit(mapping[case], (x * 50, y * 50))

    def objects_position(self):
        """
        Objects positioning in labyrinthe
        """

        i = 0
        y = 1
        x = 1
        objects = ["a", "b", "c"]
        while i < 3:
            y = randint(2, 13)
            x = randint(1, 14)
            if self.course[y][x] == " ":
                self.course[y][x] = objects[i]
                i += 1

    def guardian_control(self, x, y, objects):
        """
        Guardian control function for the game finish
        """

        if self.course[y][x + 1] == "G" or self.course[y][x - 1] == "G":
            if len(objects) == 3:
                textfinish = FINISH_TEXT_POLICIE.render(
                    "Vous avez gagné !", True, FINISH_TEXT_COLOR
                )
            else:
                textfinish = FINISH_TEXT_POLICIE.render(
                    "Vous avez perdu !", True, FINISH_TEXT_COLOR
                )
            textposfinish = textfinish.get_rect()
            textposfinish.centerx = 480
            textposfinish.centery = 380
            WINDOW.blit(textfinish, textposfinish)
            pygame.display.flip()
            pygame.time.wait(2000)
            return True


class Player:
    """
    Class for the play management
    """

    def __init__(self, x, y, lab):

        self.x = x
        self.y = y
        self.objects = []
        self.lab = lab

    def player_movement(self, player):
        """
            User input and player movement function
        """
        caracters_list = [" ", "a", "b", "c"]

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if (
                    event.key == K_RIGHT
                    and self.lab.course[self.y][self.x + 1] in caracters_list
                ):
                    self.lab.course[self.y][self.x] = " "
                    self.x += 1
                    player.objects_capture()
                    self.lab.course[self.y][self.x] = "p"
                elif (
                    event.key == K_UP
                    and self.lab.course[self.y - 1][self.x] in caracters_list
                ):
                    self.lab.course[self.y][self.x] = " "
                    self.y -= 1
                    player.objects_capture()
                    self.lab.course[self.y][self.x] = "p"
                elif (
                    event.key == K_LEFT
                    and self.lab.course[self.y][self.x - 1] in caracters_list
                ):
                    self.lab.course[self.y][self.x] = " "
                    self.x -= 1
                    player.objects_capture()
                    self.lab.course[self.y][self.x] = "p"
                elif (
                    event.key == K_DOWN
                    and self.lab.course[self.y + 1][self.x] in caracters_list
                ):
                    self.lab.course[self.y][self.x] = " "
                    self.y += 1
                    player.objects_capture()
                    self.lab.course[self.y][self.x] = "p"
                elif event.key == K_ESCAPE:
                    sys.exit()
                return (self.x, self.y)

    def objects_capture(self):
        """
        Objet's capture function
        """

        if self.lab.course[self.y][self.x] == "a":
            self.objects.append("a")
        if self.lab.course[self.y][self.x] == "b":
            self.objects.append("b")
        if self.lab.course[self.y][self.x] == "c":
            self.objects.append("c")
        return self.objects

    def objects_display(self):
        """
            Object's player display function
        """

        if "a" in self.objects:
            texta = PLAYER_OBJECT_POLICIE.render("- Ether", True, PLAYER_OBJECT_COLOR)
            textposa = texta.get_rect()
            textposa.centerx = 840
            textposa.centery = 55
            WINDOW.blit(texta, textposa)
        if "b" in self.objects:
            textb = PLAYER_OBJECT_POLICIE.render("- Syringe", True, PLAYER_OBJECT_COLOR)
            textposb = textb.get_rect()
            textposb.centerx = 840
            textposb.centery = 75
            WINDOW.blit(textb, textposb)
        if "c" in self.objects:
            textc = PLAYER_OBJECT_POLICIE.render("- Needle", True, PLAYER_OBJECT_COLOR)
            textposc = textc.get_rect()
            textposc.centerx = 840
            textposc.centery = 95
            WINDOW.blit(textc, textposc)
