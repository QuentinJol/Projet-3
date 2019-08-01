# -*- coding: utf8 -*-



mon_parcours = []
liste_temporaire = []
liste_temporaire2 = []
fichier_parcours = "parcours.csv"
direction = ""

def read_file(file):
    with open(file, 'r') as fichier:
        return(fichier.read().splitlines())

liste_temporaire = (read_file(fichier_parcours))

for line in liste_temporaire:
        liste_temporaire2.append("".join(line))

for line in liste_temporaire2:
        mon_parcours.append(list(line.strip()))   


mon_parcours[1][1] = "x"

for line in mon_parcours:
        print(''.join(map(str, line)))


if mon_parcours[1][1] != "x":
        print(type(mon_parcours[1][1]))

while mon_parcours[15][10] != "x0" :
        direction = input("Dans quelle direction souhaitez-vous aller ?")
        if direction = "z":



print(direction)