# -*- coding: utf8 -*-

import re


# Fonction pour le lecture du fichier labyrinthe
def read_file(file):
    with open(file, 'r') as fichier:
        liste_temporaire = []
        temp_list2 = []
        liste_temporaire=(fichier.read().splitlines())
        for line in liste_temporaire:
                temp_list2.append(list(line.strip()))   
        return temp_list2


# Fonction d'affichage du labyrinthe
def affichage_parcours(mon_parcours):
        for line in mon_parcours:
                print(''.join(line))

# Fonction de récupération de l'entrée utilisateur pour la direction du joueur avec vérification du caractere saisi
def entree_utilisateur():
        direction = input("Dans quelle direction souhaitez-vous aller ?(Z, Q, S ou D pour jouer)")
        character_control = re.findall("(?i)z|q|s|d", direction)
        if (character_control) :
                return (direction)
        else:
                entree_utilisateur()

# def deplacement_personnage():
#         if direction == "d":
#                return (x =+ 1)
#         else:
#                 pass



def main():
        mon_parcours = []
        fichier_parcours = "parcours"
        direction ="a"
        x = 1
        y = 1
        mon_parcours = read_file(fichier_parcours)
        mon_parcours[y][x] = "p"
        affichage_parcours(mon_parcours)
        direction = entree_utilisateur()
        print(direction)


main()

#while mon_parcours[15][10] != "p" :
 #       direction = input("Dans quelle direction souhaitez-vous aller ?")
  #      if direction = "z":
   #             if 


