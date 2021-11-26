from Fonction1 import *
import matplotlib.pyplot as plt
import numpy as np

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
    bar(x, y, width=1, edgecolor="white", linewidth=0.7)

    plt.show()
    return L
