# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 13:55:50 2021

@author: dcoqu
"""

def afficheMENU():
    print("taper 1: Extraire les Villes du fichier")
    print("taper 2: Extraire des statistiques Villes d’un département")
    print("taper 3: Visualiser l'histogramme des villes")
    print("taper 4: Distance entre 2 villes")
    print("taper 5: Plus court chemin")
    print("F: pour finir")
    
def afficheSOUS_MENU():
    print("taper 1: Lister les 5 Villes ayant le plus d'habitants")
    print("taper 2: Lister les 5 Villes ayant le moins d'habitants")
    print("taper 3: Afficher les 10 Villes sur une carte")
    print("taper 4: Lister les 10 Villes ayant le plus fort taux d'accroissement")
    print("taper 5: Lister les 10 Villes ayant le plus faible taux d'accroissement")
    print("Q: pour Quitter le sous-menu")


# Programme principal
# Appel de la procédure afficheMENU()
fini = False
while fini == False:
    afficheMENU()
    choix = input("votre choix: ")
    if choix == '1':
        print("appel de fonction1\n")
    elif choix == '2':
        finiBis = False
        while finiBis == False:
            afficheSOUS_MENU()
            choixBis = input("votre choix: ")
            if choixBis == '1':
                print("appel de la stat1\n")
            elif choixBis == '2':
                 print("appel de la stat2\n")
            elif choixBis == '3':
                print("appel de la stat3\n")
            elif choixBis == '4':
                print("appel de la stat4\n")
            else:
                finiBis = True
    elif choix == '3':
        print("Appel de la fonction3\n")
    elif choix == '4':
        print("Appel de la fonction4\n")
    elif choix == '5':
        print("Appel de la fonction5\n")
    elif choix == 'F':
        fini = True

print("Fin du programme")