from Fonction1 import *
import matplotlib.pyplot as plt
import numpy as np
import statistics



##############################################################
##############################################################
#     Classement villes par département
##############################################################
##############################################################

def classement_villes_departement(fichier_csv):
    """

    :param fichier_csv:
    :return: dictionnaire avec clé : num_departement
    valeur : nb_habitant
    """
    # recupère le dictionnaire des département et du nombre d'habitants'
    dico = creation_dico_ville_parametres(fichier_csv)
    dico_final = {}
    for k,v in dico.items():
        dico_final[v[0]] = dico_final.get(v[0], 0) + 1
    return dico_final

def affichage_ville_departement(dico_ville_departement):
    """

    :param dico_ville_departement:
    :return:
    """
    L = []
    X = []
    Y = []
    d = classement_villes_departement('villes_france.csv')
    for k,v in d.items():
        L.append((k, v))
    for i in L :
        X.append(i[0])
        Y.append(i[1])
    # data = [1, 2, 2, 3, 3, 3, 4, 4, 5]

    #plt.style.use('_mpl-gallery')

    # make data:

    x = np.array(X)
    y = np.array(Y)

    # plot
    plt.plot(x,y)

    plt.show()
    return L

def statistiques_par_departement_habitant(fichier_csv, N):
    """
    stat = (moyenne, ecart-type, mediane, 10%plusFaible, 10%plusGrand)
    :param fichier_csv:
    :param N: N est un entier qui caractéridse le numéro du département
    :return: une liste avec des tuples (ville, données)
    exemple pour la haute savoie

    [('MEGEVE', (74, 3705, 4518, 3900, 44.11, 6.61667, 45.8667, 1027, 2485)),
    ('MEGEVETTE', (74, 527, 366, 500, 21.66, 6.5, 46.2, 856, 1760)),
    ('MEILLERIE', (74, 314, 279, 300, 3.91, 6.71667, 46.4, 372, 1000)), ...]

    """
    dico_dep = dict()
    L = []
    dico = creation_dico_ville_parametres(fichier_csv)
    for cle, valeur in dico.items():
        if valeur[0] == N:
            L.append((cle, valeur))
    habitant2010 = []
    habitant1999 = []
    habitant2012 = []
    surface = []
    densite = []
    altitude_basse = []
    altitude_haute = []

    for i in L:
        habitant2010.append(i[1][1])
        habitant1999.append(i[1][2])
        habitant2012.append(i[1][3])
        surface.append(i[1][4])
        altitude_basse.append(i[1][7])
        altitude_haute.append(i[1][8])

    stat_hab2010 = (statistics.mean(habitant2010), statistics.stdev(habitant2010), statistics.median(habitant2010))
    stat_hab1999 = (statistics.mean(habitant1999), statistics.stdev(habitant1999), statistics.median(habitant1999))
    stat_hab2012 = (statistics.mean(habitant2012), statistics.stdev(habitant2012), statistics.median(habitant2012))
    stat_surface = (statistics.mean(surface), statistics.stdev(surface), statistics.median(surface))
    stat_alt_basse = (statistics.mean(altitude_basse), statistics.stdev(altitude_basse), statistics.median(altitude_basse))
    stat_alt_haute = (statistics.mean(altitude_haute), statistics.stdev(altitude_haute), statistics.median(altitude_haute))

    # présentation sous forme de tablea
    print(f"STATISTIQUES DU DEPARTEMNT {N}:  \n")

    print(f" Statistiques du nb habitant en 2010")
    print(f"Nb habitant       moyenne    Ecart_Type    Médiane ")
    print(f"                  {stat_hab2010[0]:.2f}    {stat_hab2010[1]:.2f}     {stat_hab2010[2]:.2f}")

    print("\n")
    print(f" Statistiques du nb habitant en 1999")
    print(f"Nb habitant       moyenne    Ecart_Type    Médiane ")
    print(f"                  {stat_hab1999[0]:.2f}    {stat_hab1999[1]:.2f}     {stat_hab1999[2]:.2f}")

    print("\n")
    print(f" Statistiques du nb habitant en 2012")
    print(f"Nb habitant       moyenne    Ecart_Type    Médiane ")
    print(f"                  {stat_hab2012[0]:.2f}    {stat_hab2012[1]:.2f}     {stat_hab2012[2]:.2f}")

    print("\n")
    print(f" Statistiques surface")
    print(f"Surface               moyenne    Ecart_Type    Médiane ")
    print(f"                      {stat_surface[0]:.2f}    {stat_surface[1]:.2f}     {stat_surface[2]:.2f}")

    print("\n")
    print(f" Statistiques ALTITUDE BASSE")
    print(f"Alt_Basse             moyenne    Ecart_Type    Médiane ")
    print(f"                      {stat_alt_basse[0]:.2f}    {stat_alt_basse[1]:.2f}     {stat_alt_basse[2]:.2f}")

    print("\n")
    print(f" Statistiques ALTITUDE HAUTE")
    print(f"Alt_Haute             moyenne    Ecart_Type    Médiane ")
    print(f"                      {stat_alt_haute[0]:.2f}    {stat_alt_haute[1]:.2f}     {stat_alt_haute[2]:.2f}")

    return stat_hab2010, stat_hab1999, stat_hab2012, stat_surface, stat_alt_basse, stat_alt_haute




