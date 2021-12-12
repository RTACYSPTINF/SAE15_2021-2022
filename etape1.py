from ressources import *

def extraction_villes_csv(fichier):
    """

    :param fichier: fichier csv "villes_france.csv"
    :return: liste dont chaque éléments est une ligne du fichier csv non traitée
    5 premieres lignes de la liste récupérée :
    ['"1","01","ozan","OZAN","ozan","Ozan","O250","OSN","01190","284","01284","2","26","6","618","469","500","93","6.6","4.91667","46.3833","2866","51546","+45456","462330","170","205"\n',
 '"2","01","cormoranche-sur-saone","CORMORANCHE-SUR-SAONE","cormoranche sur saone","Cormoranche-sur-SaÃ´ne","C65652625","KRMRNXSRSN","01290","123","01123","2","27","6","1058","903","1000","107","9.85","4.83333","46.2333","2772","51379","+44953","461427","168","211"\n',
 '"3","01","plagne-01","PLAGNE","plagne","Plagne","P425","PLKN","01130","298","01298","4","03","6","129","83","100","20","6.2","5.73333","46.1833","3769","51324","+54342","461131","560","922"\n',
 '"4","01","tossiat","TOSSIAT","tossiat","Tossiat","T230","TST","01250","422","01422","2","25","6","1406","1111","1400","138","10.17","5.31667","46.1333","3309","51268","+51854","460828","244","501"\n',
 '"5","01","pouillat","POUILLAT","pouillat","Pouillat","P430","PLT","01250","309","01309","2","33","6","88","58","100","14","6.23","5.43333","46.3333","3435","51475","+52542","461938","333","770"\n']
    """
    f = open(fichier)  # ouverture du fichier
    recup = f.readlines()  # on récupère une liste avec les lignes du fichier à traiter
    f.close() # fermeture obligatoire du fichier
    return recup




def extract_infos_villes(UneListe):
    """
    Cette fonction va permettre de donner une liste de listes.

    :param UneListe: c'est la liste créée avec la fonction extraction_villes_csv(fichier)
    :return: une liste au format demandé, c'est à dire :
    ['01','CORMORANCHE-SUR-SAONE','01290',1058,903,1000,107,9.85,4.83333,46.2333,168,211]
    les trois premiers éléments de cette liste sont de type str et les autres de types entiers ou float selon ce qui est donné dans le fichier csv.
    """
    L = [] # liste finale qui est à retourner
    for j in UneListe:
        i = j.split(",") # on éclate chaque élément de la liste qui est une str avec les éléments séparés par des virgules ","
        if i[25]!= 'NULL':  # certainne altitude sont des chaines de caractères (str) de type 'NULL'
            L.append([eval(i[1]),
                      eval(i[3]),
                      eval(i[8]),
                      int(eval(i[14])),
                      int(eval(i[15])),
                      int(eval(i[16])),
                      int(eval(i[17])),
                      float(eval(i[18])),
                      float(eval(i[19])),
                      float(eval(i[20])),
                      eval(eval(i[25])),
                      eval(eval(i[26]))])
    return L


def extract_villes_depart_indicatif():
    """
    Cette fonction va créer 5 fichiers texte comportant les noms des villes par indicatifs téléphonique
    :param listeInfo: Liste obtenu avec la fonction extract_infos_villes(UneListe)
    :return: cind fichiers textes
    IF01.txt (Iles de France 01)
    NO02.txt (Nord Ouest 02)
    NE03.txt (Nord Est 03)
    SE04.txt (Sud Est 04)
    SO04.txt (Sud Ouest 05)
    """
    Liste1 = extraction_villes_csv('villes_france.csv')
    liste_ville = extract_infos_villes(Liste1)
    # creation fichier IF01.txt
    f = open('IF01.txt', 'w')
    for i in liste_ville:
        if i[0] in INDICATIF_01:
            f.write(i[0] + "   " + i[1] + "\n")
    f.close()

    f = open('NO02.txt', 'w')
    for i in liste_ville:
        if i[0] in INDICATIF_02:
            f.write(i[0] + "   " + i[1] + "\n")
    f.close()

    f = open('NE03.txt', 'w')
    for i in liste_ville:
        if i[0] in INDICATIF_03:
            f.write(i[0] + "   " + i[1] + "\n")
    f.close()

    f = open('SE04.txt', 'w')
    for i in liste_ville:
        if i[0] in INDICATIF_04:
            f.write(i[0] + "   " + i[1] + "\n")
    f.close()

    f = open('SO05.txt', 'w')
    for i in liste_ville:
        if i[0] in INDICATIF_05:
            f.write(i[0] + "   " + i[1] + "\n")
    f.close()



