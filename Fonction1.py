"""
On crée une fonction nommée :
        extraction_ville_csv(fichier)
Travail à faire
Classement national de la ville en fonction du nombre d’habitants :
        def classement_national_ville_habitants(fich):

Classement national de la ville en fonction de la superficie de la ville :
        def classement_national_ville_superficie(fich):

Classement national de la ville en fonction de la densité de population :
        def classement_national_ville_densite(fich):

Classement département de la ville en fonction du nombre d’habitants :
        def classement_departemental_ville_habitant(fich):

Classement département de la ville en fonction de la superficie de la ville :
        def classement_departemental_ville_superficie(fich):

Classement département de la ville en fonction de la densité de population
        def classement_departemental_ville_densité(fich)
"""
#######################################################################
#######################################################################
# https://iut-info.univ-reims.fr/users/nocent/python/?section=6
# tracé sur une carte avec folium  https://iut-info.univ-reims.fr/users/nocent/python/?section=9
# doc folium https://python-visualization.github.io/folium/
#######################################################################
#######################################################################


import math
import ressources
from pathlib import *
import os
from math import cos, sin, asin, acos, pi, atan2, sqrt
from distance1 import *
import copy






def recup_ville_de_france(fichier):
    """
    Cette fonction permet d'extraire les données du fichier villes_france.csv
    le fait d'utiliser readlines permet de récupérer une liste dont chaque élément coorespond à une ville ainsi que toutes les données associées
    :param fichier: fichier "villes_france.csv"
    :return: une liste "recup" dont chaque élément est une str qui comporte toutes les données d'une ville (27 données par ville au total)
    """
    # on se place dans le bon répertoire
    p = Path('E:/SAE15/SAE15_2021-2022')
    os.chdir(p)
    with open(fichier,'r') as fich:
        recup = fich.readlines()
    return recup


def conversionDMS_DEGRE(deg, min, sec):
    """
    Converti un angle donné en degés, minutes, seconde en un flottant en degreé
    Par exemple d = 36 degrés, 12 minutes et 56 seconde donnée en paramètre de la fonction
    La fonction renvera : 36.21555555555556 degrés
    :param deg:
    :param min:
    :param sec:
    :return: un flottant en degrès
    """
    angle_degre = 0
    angle_degre = deg + min /60 + sec/60/60
    return angle_degre


def haversine(VilleA, villeB):
    """
    Cette fonction permet de claculer la distance méridienne en tre deux coordonnées GPS
    Exemple :  si on a MArseille villeA = (43.2967 ,5.37639 )
                et Paris  villeB = (48.86 ,2.34445 )
    La distance méridienne entre ces deux ville devra être égale à 462.06693278381385 km
    On prendra comme formule, la formule de Haversine
    d = 2*r*Arcsin(sqrt(sin))

    :param VilleA: tuple (latA, longA)
    :param villeB: tuple (latB, longB)
    :return: distance en km
    """
    # conversion en radin
    # rayon moyen de la terre r (donné en km)
    r = 6371
    lambdaA = villeA[1]*pi/180
    lambdaB = villeB[1]*pi/180
    phiA = villeA[0]*pi/180
    phiB = villeB[0]*pi/180
    print(lambdaA, phiA , lambdaB, phiB)
    # https://www.youtube.com/watch?v=L3M74lFJ5Ec
    # site explicatif sur la formule ci-dessous
    distance = 2*r*asin(sqrt(((sin((phiB - phiA)/2))**2) + cos(phiA)*cos(phiB)*(sin((lambdaB - lambdaA)/2))**2))
    return distance


"""
    Cette fonction va renvoyer une liste de liste avec les données du fichier initial au bon format.
    par exemple, avant traitement avec cette fonction, toutes les données sont du type str.
"""
def extraction_ville_gps(villes_liste):
    """
    Cette fonction va renvoyer une liste de liste avec les données du fichier initial au bon format.
    par exemple, avant traitement avec cette fonction, toutes les données sont du type str.

    int(eval(i[1])),            departement
    eval(i[3]),                 ville
    i[14],                      pop en 2010
    i[15],                      pop en 1999
    i[16],                      pop en 2012
    i[17],                      surface
    float(eval(i[19])),         latitude
    float(eval(i[20])),         longitude
    i[25],                      alt min
    i[26]])                     alt max

    :param villes_liste:
    :return:
    """
    L= []
    temp = []
    for i in villes_liste:
        temp.append(i.split(','))
    for i in temp:
        if ((eval(i[1]) != '2A') and (eval(i[1]) != '2B'))  and i[25] != 'NULL':
            L.append([int(eval(i[1])),
                      eval(i[3]),
                      int(eval(i[14])),
                      int(eval(i[15])),
                      int(eval(i[16])),
                      float(eval(i[18])),
                      float(eval(i[19])),
                      float(eval(i[20])),
                      eval(eval(i[25])),
                      eval(eval(i[26]))])
        else:
            L.append([eval(i[1]),
                      eval(i[3]),
                      int(eval(i[14])),
                      int(eval(i[15])),
                      int(eval(i[16])),
                      float(eval(i[18])),
                      float(eval(i[19])),
                      float(eval(i[20])),
                      i[25],
                      i[26]])

    return L

def creation_dico_ville_parametres(fichier_ville_csv):
    """
    cette fonction va nous renvoyer un dictionnaire où la clé est le nom de la ville en majuscule et
    la valeur est un tuple avec dans l'ordre :
    int(eval(i[1])),            departement
    i[14],                      pop en 2010
    i[15],                      pop en 1999
    i[16],                      pop en 2012
    i[17],                      surface
    float(eval(i[19])),         latitude
    float(eval(i[20])),         longitude
    i[25],                      alt min
    i[26]])                     alt max
    :param fichier_ville_csv: fichier donné dans la SAé
    :return: dictionnaire des noms de villes avec un tuple comme clé
    exemple :
     {'LE THUEL': (2, 170, 149, 200, 7.06, 4.07695, 49.6495, 112, 172),
 'SEPTVAUX': (2, 191, 202, 200, 8.56, 3.38333, 49.5667, 93, 212),
 'NEUFCHATEL-SUR-AISNE': (2, 416, 492, 400, 2.86, 4.03333, 49.4333, 56, 119),}
 ordre des paramètres du tuple :
     departement
     pop en 2010
     pop en 1999
     pop en 2012
     surface
     latitude
     longitude
     alt min
     alt max
    """
    #
    villes_liste = recup_ville_de_france(fichier_ville_csv)  # on extrait les données brutes du fichier
    aa = extraction_ville_gps(villes_liste)  # on crée la liste "aa" qui comprend les données de chaque ville dans un format normal
    # reste à créer le dictionnaire
    dico_final = dict()
    for i in aa:
        dico_final[i[1]] = (i[0], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])
    return dico_final

# renvoie un dictionnaire avec comme clé le département et comme valeurs le nombre de villes par département
def compte_villes_par_dep(fich):
    """
    renvoie un dictionnaire avec comme clé le département et comme valeurs le nombre de villes par département
    :param fich: est  une liste
            [[1, 'CORMORANCHE-SUR-SAONE', 4.83333, 46.2333],
            [1, 'PLAGNE', 5.73333, 46.1833],
            [1, 'TOSSIAT', 5.31667, 46.1333]]
    cette liste a été obtenue par la fonction "extraction villes GPS
    :return:
    """
    d={}
    cpt = 0
    for i in range(95):
        cpt = 0
        for j in fich:
            if j[0] == i:
                cpt += 1
                d[i] = cpt
    return d

def Nb_habitants_villes_par_dep2012(fich, departement):
    """
    renvoie un dictionnaire contenant comme clé : le nom de ville
    comme valeur : le nombre d'habitant en 2012 [
    :param fich:
    :param departement:
    :return: un dictionnaire (pour le departement 74
{'ANDILLY': 800,
 'MINZIER': 800,
 'SAINT-PAUL-EN-CHABLAIS': 2100, ...}
    """
    d = {}
    for i in fich:
        if i[0] == departement:
            d[i[1]]=i[4]
    return d

def Nb_habitants_villes_par_dep1999(fich, departement):
    """
    renvoie un dictionnaire contenant comme clé : le nom de ville
    comme valeur : le nombre d'habitant en 1999 [
    :param fich:
    :param departement:
    :return: un dictionnaire (pour le departement 74
{'ANDILLY': 800,
 'MINZIER': 800,
 'SAINT-PAUL-EN-CHABLAIS': 2100, ...}
    """
    d = {}
    for i in fich:
        if i[0] == departement:
            d[i[1]]=i[2]
    return d

def Nb_habitants_villes_par_dep2010(fich, departement):
    """
    renvoie un dictionnaire contenant comme clé : le nom de ville
    comme valeur : le nombre d'habitant en 2010 [
    :param fich:
    :param departement:
    :return: un dictionnaire (pour le departement 74
{'ANDILLY': 800,
 'MINZIER': 800,
 'SAINT-PAUL-EN-CHABLAIS': 2100, ...}
    """
    d = {}
    for i in fich:
        if i[0] == departement:
            d[i[1]]=i[3]
    return d

"""
renvoie un dictionnaire pour l'ensemble du fichier contenant comme clé : le nom de ville
comme valeur : le nombre d'habitant en 1999
"""
def Nb_habitants_villes_global(fich):
    """
    renvoie un dictionnaire pour l'ensemble du fichier contenant comme clé : le nom de ville
    comme valeur : le nombre d'habitant en 1999 [
    :param fich:
    :return: un dictionnaire (pour le departement 74
{'ANDILLY': 800,
 'MINZIER': 800,
 'SAINT-PAUL-EN-CHABLAIS': 2100, ...}
    """
    d = {}
    for i in fich:
        d[i[1]]=i[4]
    return d

def plus_grande_ville_N(N):
    """
    fonction qui va classer les N plus grande et N plus petites villes en fonction de leur nombre d'habitants

    :param N: int -> nombre de ville
    :return: tuple (liste_N_Petites, liste_N_Grandes)
    """
    dico_ville = Nb_habitants_villes_global(extraction_ville_gps(villes_liste))

    # Inversion du dictionnaire
    dico_ville_inverse = {}
    for k,v in dico_ville.items():
        dico_ville_inverse[v]=k
    liste_tri = sorted(dico_ville_inverse)
    # on recupere le N valeurs les plus petites
    petitesN = liste_tri[:N]
    grandesN = liste_tri[len(liste_tri) - N :]
    liste_petiteN = []
    for i in petitesN:
        liste_petiteN.append((dico_ville_inverse[i], i))
    liste_grandeN = []
    for i in grandesN:
        liste_grandeN.append((dico_ville_inverse[i], i))
    return liste_petiteN, liste_grandeN

def dico_ville_par_noms():
    """
    cette fonction va nous renvoyer un dictionnaire avec comme clé le nom de la vile en majuscule
    et comme clé les paramètres qui nous semble utils rangés dans une liste
    :param liste_ville: recup_ville_france
    :return:  renvoie le dictionnaire souhaité
    """
    villes_france = recup_ville_de_france('villes_france.csv')
    liste_villes = extraction_ville_gps(villes_france)
    d = {}
    for i in liste_villes:
        d[i[1]] = [i[2], i[3], i[4], i[5], i[6], i[7]]
    return d

def creation_villes_grandes(N):
    """
    On veut créer une liste des N plus grande ville de france
    :return:
    """
     # nb de villes dans notre liste
    petit, grand = plus_grande_ville_N(N)
    dico_villes = dico_ville_par_noms()
    fich = recup_ville_de_france('villes_france.csv')
    extract = extraction_ville_gps(fich)
    Liste_finale = [] # liste finale à retourner
    dico_final = {}
    for i in grand :
        dico_final[i[0]]=dico_villes[i[0]]
    # on crée une liste avec le nom et un tuple représenat les coordonnée gps de la ville
    #['PARIS', (lat_paris, long_paris)]
    d_final = {}
    for i in dico_final:
        d_final[i] = (dico_final[i][4], dico_villes[i][5])
    return d_final

def crea_table_distance(N):
    """

    :param N:
    :return:
    """
    # creat table remplie de "1" de dimension  N*N
    table = [[1]*N for i in range(N)]
    table_temp = copy.deepcopy(table)
    for i in range(N):
        for j in range(N):
            if i == j:
                table_temp[i][j] = 0
    table = copy.deepcopy(table_temp)
    print(table)
    a = creation_villes_grandes(N)
    table2 = copy.deepcopy(table)
    Liste_villes = []
    for i in a:
        Liste_villes.append(i)
    Liste_villes.sort() # liste des villes ordonnée
    d={}
    for i,v in enumerate(Liste_villes):
        d[i]=v
    # calcul des distance et rempissage de la table lorsque i,j = 1

    for i in range(N):
        for j in range(N):
            if table[i][j] == 1:
                lat1 = a[d[i]][0]
                lon1 = a[d[i]][1]
                lat2 = a[d[j]][0]
                lon2 = a[d[j]][1]
                dist_1_2 = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
                print(dist_1_2)
                table2[i][j] = dist_1_2


                #print(table)

    return Liste_villes, table,d,a, table2


def haversine_net(lat1, lon1, lat2, lon2):
    R = 6372.8  # Rayon moyen de la terre en km

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return R * c


if __name__ == "__main__":
    villes_liste = recup_ville_de_france('villes_france.csv') # on extrait les données brutes du fichier
    aa = extraction_ville_gps(villes_liste) # on crée la liste "aa" qui comprend les données de chaque ville dans un format normal
    dep2012 = Nb_habitants_villes_par_dep2012(aa, 73)
    dep1999 = Nb_habitants_villes_par_dep1999(aa, 73)
    dep2010 = Nb_habitants_villes_par_dep2010(aa, 73)

    L = []
    for i in range(65,76):
        L.append(Nb_habitants_villes_par_dep2012(aa,i))
    # test ville classées et retour de liste
    a = creation_villes_grandes(10)
    # calcul distance entre Lille et maeseille
    latMarseille = a['MARSEILLE'][1]
    lonMarseille = a['MARSEILLE'][0]

    latParis = a['PARIS'][1]
    lonParis = a['PARIS'][0]
    dist_Paris_Marseille = mpu.haversine_distance((latMarseille, lonMarseille), (latParis, lonParis))





