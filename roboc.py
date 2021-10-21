#!/usr/bin/python3
# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import pickle
from donnees import *
from fonctions import *
from carte import Carte

# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-4].lower()
        with open(chemin, "r") as fichier:
            contenu = fichier.read()
            # Création d'une carte, à compléter
        cartes.append(Carte(nom_carte, contenu))

# Si il y a une partie sauvegardée
# on propose de la poursuivre
path = os.getcwd()  # path=l'endroit ou l'on se trouve
partie_sauvegardee = False
# partie=Carte()
for nom_fichier in os.listdir(path):  # On cherche un fichier de partie sauvegardée
    if nom_fichier == NOM_PARTIE_SAUVEGARDEE:
        partie = recup_partie()
        print("\nIl existe une partie sauvegardée.")
        reponse = input("Voulez-vous la poursuivre ? (O/N) ")
        reponse = reponse.lower()
        if reponse == "o":
            partie_sauvegardee = True

# Pas de partie sauvegardéé ou refus de la poursuivre.pi
# On affiche les cartes
if partie_sauvegardee != True:
    print("\nLabyrinthes existants :")
    for i, carte in enumerate(cartes):
        print("  {} - {}".format(i + 1, carte.nom))
    numero = input("Entrez le numéro de carte choisi : ")
    if numero == "":
        print("Vous n'avez pas choisi de carte. On démarre sur la carte Numéro 1")
        numero = 1
    numero = int(numero)
    partie = cartes[numero - 1]
print("\nVous avez choisi la carte : {}\n".format(partie.nom))
print(partie.labyrinthe)

# Cours de la partie
continuer_partie = "o"
while continuer_partie != "n":
    deplacement = recup_mouvement()
    print("direction : {} - pas : {}".format(deplacement[0], deplacement[1]))
    if deplacement[0] == "s":
        i = 1
        while i <= deplacement[1]:
            if partie.labyrinthe.grille[partie.labyrinthe.robot[0], partie.labyrinthe.robot[1] + 1] == MUR:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Il y a un mur !!! Mouvement impossible")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                break
            elif partie.labyrinthe.grille[partie.labyrinthe.robot[0], partie.labyrinthe.robot[1] + 1] == SORTIE:
                partie.labyrinthe.robot[1] += 1
                continuer_partie = "n"
                print("Vous avez trouvé la sortie !!!!!!!")
            elif partie.labyrinthe.grille[partie.labyrinthe.robot[0], partie.labyrinthe.robot[1] + 1] == ESPACE or \
                    partie.labyrinthe.grille[partie.labyrinthe.robot[0], partie.labyrinthe.robot[1] + 1] == PORTE:
                partie.labyrinthe.robot[1] += 1
            i += 1
    elif deplacement[0] == "n":
        i = 1
        while i <= deplacement[1]:
            if partie.labyrinthe.grille[partie.labyrinthe.robot[0], partie.labyrinthe.robot[1] - 1] == MUR:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Il y a un mur !!! Mouvement impossible")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                break
            elif partie.labyrinthe.grille[partie.labyrinthe.robot[0], partie.labyrinthe.robot[1] - 1] == SORTIE:
                partie.labyrinthe.robot[1] -= 1
                continuer_partie = "n"
                print("Vous avez trouvé la sortie !!!!!!!")
            elif partie.labyrinthe.grille[partie.labyrinthe.robot[0], partie.labyrinthe.robot[1] - 1] == ESPACE or \
                    partie.labyrinthe.grille[partie.labyrinthe.robot[0], partie.labyrinthe.robot[1] - 1] == PORTE:
                partie.labyrinthe.robot[1] -= 1
            i += 1

    elif deplacement[0] == "e":
        i = 1
        while i <= deplacement[1]:
            if partie.labyrinthe.grille[partie.labyrinthe.robot[0] + 1, partie.labyrinthe.robot[1]] == MUR:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Il y a un mur !!! Mouvement impossible")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                break
            elif partie.labyrinthe.grille[partie.labyrinthe.robot[0] + 1, partie.labyrinthe.robot[1]] == SORTIE:
                partie.labyrinthe.robot[0] += 1
                continuer_partie = "n"
                print("Vous avez trouvé la sortie !!!!!!!")
            elif partie.labyrinthe.grille[partie.labyrinthe.robot[0] + 1, partie.labyrinthe.robot[1]] == ESPACE or \
                    partie.labyrinthe.grille[partie.labyrinthe.robot[0] + 1, partie.labyrinthe.robot[1]] == PORTE:
                partie.labyrinthe.robot[0] += 1
            i += 1

    elif deplacement[0] == "o":
        i = 1
        while i <= deplacement[1]:
            if partie.labyrinthe.grille[partie.labyrinthe.robot[0] - 1, partie.labyrinthe.robot[1]] == MUR:
                print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Il y a un mur !!! Mouvement impossible")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
                break
            elif partie.labyrinthe.grille[partie.labyrinthe.robot[0] - 1, partie.labyrinthe.robot[1]] == SORTIE:
                partie.labyrinthe.robot[0] -= 1
                continuer_partie = "n"
                print("Vous avez trouvé la sortie !!!!!!!")
            elif partie.labyrinthe.grille[partie.labyrinthe.robot[0] - 1, partie.labyrinthe.robot[1]] == ESPACE or \
                    partie.labyrinthe.grille[partie.labyrinthe.robot[0] - 1, partie.labyrinthe.robot[1]] == PORTE:
                partie.labyrinthe.robot[0] -= 1
            i += 1


    elif deplacement[0] == "q":
        print("\nPartie sauvegardée. A bientot.\n")
        enregistrer_partie(partie)
        continuer_partie = "n"
    else:
        print("\nDéplacement invalide.\n")
    print(partie.labyrinthe)
