# -*- coding: utf8 -*-

from random import randint

import pygame
from pygame.locals import K_DOWN, K_ESCAPE, KEYDOWN, K_UP, K_LEFT, K_RIGHT, RESIZABLE

pygame.init()

PLAYER_OBJECT_COLOR = 0, 100, 255
FINISH_TEXT_COLOR = 200, 0, 0
PLAYER_OBJECT_POLICIE = pygame.font.SysFont("freesans", 20)
FINISH_TEXT_POLICIE = pygame.font.SysFont("freesans", 70)
SCORE_TEXT = "Player's objects :"
TEXT = PLAYER_OBJECT_POLICIE.render(SCORE_TEXT, True, PLAYER_OBJECT_COLOR)
TEXTPOS = TEXT.get_rect()
TEXTPOS.centerx = 840
TEXTPOS.centery = 25

WINDOW = pygame.display.set_mode((950, 760), RESIZABLE)
WINDOW.blit(TEXT, TEXTPOS)



class Map:
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
                temp_list2 = []
                temp_list = temp_file.read().splitlines()
                for line in temp_list:
                    temp_list2.append(list(line.strip()))
            self.course = temp_list2
        except IOError:
            print('Erreur! Le fichier "parcours" n\'a pas pu être ouvert.')
            quit()

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
            if "a" in objects and "b" in objects and "c" in objects:
                textfinish = FINISH_TEXT_POLICIE.render("Vous avez gagné !", True, FINISH_TEXT_COLOR)
                textposfinish = textfinish.get_rect()
                textposfinish.centerx = 480
                textposfinish.centery = 380
                WINDOW.blit(textfinish, textposfinish)
                pygame.display.flip()
                pygame.time.wait(2000)
                return True
            else:
                textfinish = FINISH_TEXT_POLICIE.render("Vous avez perdu !", True, FINISH_TEXT_COLOR)
                textposfinish = textfinish.get_rect()
                textposfinish.centerx = 480
                textposfinish.centery = 380
                WINDOW.blit(textfinish, textposfinish)
                pygame.display.flip()
                pygame.time.wait(2000)
                return True
        return False


class Player:
    def __init__(self, x, y, lab):

        self.x = x
        self.y = y
        self.objects = []
        self.lab = lab

    def player_movement(self, player):
        """
            User input and player movement function
        """

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RIGHT and self.lab.course[self.y][self.x + 1] in [
                    " ",
                    "a",
                    "b",
                    "c",
                ]:
                    self.lab.course[self.y][self.x] = " "
                    self.x += 1
                    player.objects_capture()
                    self.lab.course[self.y][self.x] = "p"
                elif event.key == K_UP and self.lab.course[self.y - 1][self.x] in [
                    " ",
                    "a",
                    "b",
                    "c",
                ]:
                    self.lab.course[self.y][self.x] = " "
                    self.y -= 1
                    player.objects_capture()
                    self.lab.course[self.y][self.x] = "p"
                elif event.key == K_LEFT and self.lab.course[self.y][self.x - 1] in [
                    " ",
                    "a",
                    "b",
                    "c",
                ]:
                    self.lab.course[self.y][self.x] = " "
                    self.x -= 1
                    player.objects_capture()
                    self.lab.course[self.y][self.x] = "p"
                elif event.key == K_DOWN and self.lab.course[self.y + 1][self.x] in [
                    " ",
                    "a",
                    "b",
                    "c",
                ]:
                    self.lab.course[self.y][self.x] = " "
                    self.y += 1
                    player.objects_capture()
                    self.lab.course[self.y][self.x] = "p"
                elif event.key == K_ESCAPE:
                    quit()
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


def main():
    labyrinthe = Map("parcours")
    guardian = False
    labyrinthe.read_file()
    player1 = Player(1, 1, labyrinthe)
    labyrinthe.player_start_position(player1.x, player1.y)
    labyrinthe.objects_position()
    labyrinthe.lab_display_graphic()
    pygame.display.flip()
    while not guardian:
        player1.player_movement(player1)
        labyrinthe.lab_display_graphic()
        player1.objects_display()
        pygame.display.flip()
        guardian = labyrinthe.guardian_control(player1.x, player1.y, player1.objects)


if __name__ == "__main__":
    main()

