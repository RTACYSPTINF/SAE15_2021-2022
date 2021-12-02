"""
Département : numéro du département RT
Slug : identifiant unique en minuscule, sans accent et sans espace. Peut servir pour faire les URLs d’un site web.
Nom : nom en majuscule et sans accent.
Nom simple : nom en minuscule, sans accent et avec les tirets remplacés par des espaces. Peut être utilisé pour faire une recherche lorsqu’on ne sait pas si le nom de ville possède un tiret ou des espaces (ex : “Saint-Étienne” possède un tiret comme séparateur, tandis que “Le Havre” possède un espace comme séparateur)
Nom reel : nom correct avec les accents
Nom soundex : soundex du nom de la ville (permet de trouver des villes qui se prononcent presque pareil) [ajouté le 31/10/2013]
Nom metaphone : metaphone du nom de la ville (même utilité que le soundex) [ajouté le 31/10/2013]
Code postal : code postal de la ville. Si la ville possède plusieurs code postaux, ils sont tous listés et séparés par un tiret [ajouté le 31/10/2013]
Numéro de commune : numéro de la commune dans le département. Combiné avec le numéro de département, il permet de créer le code INSEE sous 5 caractères.
Code commune (ou code INSEE) : identifiant unique sous 5 caractères
Arrondissement : arrondissement de la ville
Canton : canton de la ville
Population en 2010 : nombre d’habitants lors du recensement de 2010
Population en 1999 : nombre d’habitants lors du recensement de 1999
Population en 2012 (approximatif) : valeur exprimée en centaine
Densité en 2010 : nombre d’habitants au kilomètre carré arrondie à l’entier. Calculé à partir du nombre d’habitant et de la surface de la ville [corrigé le 02/07/2014]
Surface / superficie : surface de la ville en kilomètre carrée [corrigé le 02/07/2014]
Longitude/latitude en degré : géolocalisation du centre de la ville. Permet de localiser la ville sur une carte (exemple : carte Google Maps) [ajouté le 31/10/2013, corrigé le 07/11/2013]
Longitude/latitude en GRD : géolocalisation exprimée en GRD
Longitude/latitude en DMS (Degré Minute Seconde) : géolocalisation exprimée en Degré Minute Seconde
Altitude minimale/maximale : hauteur minimum et maximum de la ville par rapport au niveau de l’eau
"""

import csv

INDEX_VILLES = ['Departement',              # int
                'Slug',                     # str
                'Nom',                      # str
                'Nom simple',               # str
                'Nom reel',                 # str
                'Nom soundex',              # str
                'Nom metophone',            # str
                'Code postal',              # int
                'Numero de commune',        # int
                'Code commune',             # int
                'Arrondissement',           # int
                'inconnu1',
                'Canton',                   # int
                'Population 2010',          # int
                'Population 1999',          # int
                'Population 2012',          # int
                'Densite 2010',             # int
                'Surface',                  # float
                'superficie',               # float
                'Longitude degre',          # float
                'Latitude degre',           # float
                'Longitude GRD',
                'Latitude GRD',
                'Longitude DMS',
                'Latitude DMS',
                'Altitude min',
                'Altitude max']

"""
Le dictionnaire qui suit permet de connaitre le lien entre l'indice et le nom de ma colonne associée
Par exemple, si on veut connaître l'indice du "numero de commune" on aura l'indice 8
dico_INDEX_VILLES['numero de commune'] renverra l'indice 8
"""
dico_INDEX_VILLES={'Departement': 0,
                     'Slug': 1,
                     'Nom': 2,
                     'Nom simple': 3,
                     'Nom reel': 4,
                     'Nom soundex': 5,
                     'Nom metophone': 6,
                     'Code postal': 7,
                     'Numero de commune': 8,
                     'Code commune': 9,
                     'Arrondissement': 10,
                     'inconnu1': 11,
                     'Canton': 12,
                     'Population 2010': 13,
                     'Population 1999': 14,
                     'Population 2012': 15,
                     'Densite 2010': 16,
                     'Surface': 17,
                     'superficie': 18,
                     'Longitude degre': 19,
                     'Latitude degre': 20,
                     'Longitude GRD': 21,
                     'Latitude GRD': 22,
                     'Longitude DMS': 23,
                     'Latitude DMS': 24,
                     'Altitude min': 25,
                     'Altitude max': 26}



def extract_ind_tel(fichcsv):
    with open(fichcsv) as f:
        recup = csv.reader(f, delimiter=';')
        L = []
        for row in recup:
            L.append(row)
    IND01 = []
    IND02 = []
    IND03 = []
    IND04 = []
    IND05 = []
    for i in L:
        if i[2] == '1':
            IND01.append(i[0])
        elif i[2] == '2':
            IND02.append(i[0])
        elif i[2] == '3':
            IND03.append(i[0])
        elif i[2] == '4':
            IND04.append(i[0])
        else :
            IND05.append(i[0])
    return IND01, IND02, IND03, IND04, IND05

aa = extract_ind_tel('indicatifs_france.csv')

INDICATIF_01 = aa[0]
INDICATIF_02 = aa[1]
INDICATIF_03 = aa[2]
INDICATIF_04 = aa[3]
INDICATIF_05 = aa[4]

DEPARTEMENT = INDICATIF_01 + INDICATIF_02 + INDICATIF_03 + INDICATIF_04 + INDICATIF_05

if __name__ == "__main":
    pass