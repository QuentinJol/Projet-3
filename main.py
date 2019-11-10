# -*- coding: utf8 -*-

"""
Main file for Labyrinthe game
"""


import pygame
import player_map_classes

pygame.init()


def main():
    """
    Labyrinthe game main function
    """

    labyrinthe = player_map_classes.Map("parcours")
    guardian = False
    labyrinthe.read_file()
    player1 = player_map_classes.Player(1, 1, labyrinthe)
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
