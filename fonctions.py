#!/usr/bin/python3
# -*-coding:Utf-8 -*

import os
import pickle
from donnees import *
from labyrinthe import Labyrinthe

def creer_labyrinthe_depuis_chaine(chaine):
    """Cette fonction repere la position du robot et des obstacles et renvois :
       - une liste (robot) contenant les coordonées du robot
       - un dictionaire (obstacles) contenant des tuples représentant :
            - la nature de l'obstacle : "O" pour mur, "." pour porte, "U" pour sortie et " " pour espace libre
            - les coordonées des obstacles"""
    obstacles={}
    robot=[]
    abscisse=1
    ordonee=1
    for caractere in chaine:
       if caractere != ROBOT and caractere != "\n": #on note la nature de l'obstacle
           obstacles[(abscisse,ordonee)]=caractere  #et ses coordonées
           abscisse += 1
       elif caractere == ROBOT:
           robot=[abscisse,ordonee]                 #On note la position du robot
           obstacles[(abscisse,ordonee)]=" "        #On suppose qu'il y a un espace libre
           abscisse += 1                            #sous le robot au début du jeu
       elif caractere == "\n":                      #On change de ligne
           abscisse = 1
           ordonee += 1
    return Labyrinthe(robot,obstacles)

def recup_partie():
    """Cette fonction récupère la partie enregistrée si elle existe"""
    
    if os.path.exists(NOM_PARTIE_SAUVEGARDEE): # Le fichier existe
        # On le récupère
        fichier_partie = open(NOM_PARTIE_SAUVEGARDEE, "rb")
        mon_depickler = pickle.Unpickler(fichier_partie)
        partie = mon_depickler.load()
        fichier_partie.close()
    return partie

def enregistrer_partie(partie):
    """Cette fonction se charge d'enregistrer la partie en cours dans le fichier
    NOM_PARTIE_SAUVEGARDEE. Elle reçoit en paramètre le dictionnaire de la partie
    à enregistrer"""

    fichier_partie = open(NOM_PARTIE_SAUVEGARDEE, "wb") # On écrase les anciens scores
    mon_pickler = pickle.Pickler(fichier_partie)
    mon_pickler.dump(partie)
    fichier_partie.close()

def recup_mouvement():
    """ Cette fonction récupère la commande du joueur et renvoie un tuple contenant
    la direction et le nombre de pas """
 
    print("\n Mouvements possibles : s - n - e - o")
    print("Entrez q pour quitter la partie")
    reponse=input("Votre mouvement : ")
    if reponse == "":
        return recup_mouvement()
    reponse=reponse.lower()
    direction=reponse[0]
    if len(reponse)>1:
        pas=int(reponse[1:])
    else:
        pas=1
    return (direction,pas)
