#!/usr/bin/python3
# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""
from donnees import *

class Labyrinthe:

    """Classe représentant un labyrinthe."""

    def __init__(self, robot, obstacles):
        self.robot = robot
        self.grille = obstacles

    def __repr__(self):
        abscisse=1
        ordonee=1
        chaine=""
        while (abscisse,ordonee) in self.grille:
            while (abscisse,ordonee) in self.grille:
                if [abscisse,ordonee]==self.robot:
                    chaine+=ROBOT
                else:
                   chaine+=self.grille[(abscisse,ordonee)]
                abscisse += 1
            abscisse = 1
            ordonee += 1
            chaine+="\n"
        return chaine
                
    def __str(self):
        return repr(self)
