# -*- coding: utf-8 -*-
"""Copie de Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cW5iLwaysVoH_p2JStpVYWHKE1snpVSN
"""

# Evolution du nombre de criminels dans une population

from tkinter import *
from random import randrange

haut = 40 # hauteur du tableau
larg = 40 # largeur du tableau
cote = 15  # création d'une cellule
rouge = 0
blanc = 1
nb_rouge = haut*larg
nb_blanc = 0

# Créer les matrices
cell = [[0 for row in range(haut)] for col in range(larg)]
parti = [[rouge for row in range(haut)] for col in range(larg)]

# Dessiner toutes les cellules
def dessiner():
    for y in range(haut):
        for x in range(larg):
            if parti[x][y]==rouge:
                coul = "red"
            else:
                coul = "white"
            canvas.itemconfig(cell[x][y], fill=coul)

# Données initiales
def init():
    global nb_rouge, nb_noir
    nb_bleu, nb_noir = 0, 0
    nb_echanges = 0
    for y in range(haut):
        for x in range(larg):
            if nb_bleu < haut*larg/2:
                parti[x][y] = rouge
                nb_bleu += 1
            else:
                parti[x][y] = blanc
                nb_noir += 1
            cell[x][y] = canvas.create_rectangle((x*cote, y*cote, (x+1)*cote, (y+1)*cote), outline="gray", fill="red")
    # placer au hasard 50% de criminels de couleur rouge
    while nb_echanges < (haut*larg//4):
        x1 = randrange(larg)
        y1 = randrange(haut)
        x2 = randrange(larg)
        y2 = randrange(haut)
        parti[x1][y1], parti[x2][y2] = parti[x2][y2], parti[x1][y1]
        nb_echanges += 1
    dessiner()

# Choisir l'opinion d'un des 8 voisins de la cellule (a,b) - tableau torique
def etat_voisin(a,b):
    voisin = randrange(8)
    if voisin==1:
        etat = parti[(a-1)%larg][(b+1)%haut]
    elif voisin==2:
        etat = parti[a][(b+1)%haut]
    elif voisin==3:
        etat = parti[(a+1)%larg][(b+1)%haut]
    elif voisin==4:
        etat = parti[(a-1)%larg][b]
    elif voisin==5:
        etat = parti[(a+1)%larg][b]
    elif voisin==6:
        etat = parti[(a-1)%larg][(b-1)%haut]
    elif voisin==7:
        etat = parti[a][(b-1)%haut]
    else:
        etat = parti[(a+1)%larg][(b-1)%haut]
    return etat

# Appliquer la règle
def calculer():
    global nb_rouge, nb_blanc
    x = randrange(larg)
    y = randrange(haut)
    nouveau_criminel = etat_voisin(x,y)
    if parti[x][y] != nouveau_criminel:
        if nouveau_criminel == rouge:
            nb_rouge += 1
            nb_blanc -= 1
        else :
            nb_rouge -= 1
            nb_blanc += 1
        parti[x][y] = nouveau_criminel
        if parti[x][y] == rouge:
            coul = "red"
        else:
            coul = "white"

        canvas.itemconfig(cell[x][y], fill=coul)

# Calculer et dessiner le prochain tableau
def tableau():
    calculer()
    fenetre.after(1, tableau)

# Lancement du programme
fenetre = Tk()
fenetre.title("Criminel🔴 Non Criminel⚪️")
canvas = Canvas(fenetre, width=cote*larg, height=cote*haut, highlightthickness=0)
canvas.pack()
init()
tableau()
fenetre.mainloop()

