

def fusion_liste(L1, L2):
    L_finale = list()
    inter = True
    cpt = 0
    while (inter==True) and len(L1)>0 and len(L2)>0:
        if (L1[0]<=L2[0]):
            L_finale.append(L1[0])
            L1.pop(0)
        else :
            L_finale.append(L2[0])
            L2.pop(0)
    if len(L1) == 0:
        L_finale = L_finale + L2
    if len(L2) == 0:
        L_finale =  L_finale + L1
    return L_finale

print(fusion_liste([7,8,12,36], [1,2,17]))


def triAvantFusion(Liste):
    if len(Liste) <= 1:
        return Liste
    else:
        milieu = len(Liste)//2
        left_list = Liste[:milieu]
        right_list = Liste[milieu:]
        left_list = triAvantFusion(left_list)
        right_list = triAvantFusion(right_list)
    return fusion_liste(left_list, right_list)


#print(triAvantFusion([(5, 170), (8, 340), (14, 288), (15, 259),  (6, 310), (10, 269), (1, 195), (4, 277), (9, 165), (12, 309),  (7, 178), (11, 295), (13, 270), (2, 281), (3, 249)]))

print(triAvantFusion([1,5,3,41,5,3,3,56,4,8,78,56]))

def fact(N):
    a = 1
    if N==0:
        print("return 1")
        return 1
    else:
        a = N*fact(N-1)
        print(N,a)
    return a

print(fact(5))

def tri_fusion(L):
    """

    :param L:
    :return:
    """
    milieu = len(L)//2
    L_temp = []
    L1 = L[:milieu]
    L2 = L[milieu:]
    L_temp = L1 + L2
    while len(L1)>1 and len(L2)>1:
        pass


def is_palindrome(chaine_car):
    """

    :param chaine_car:
    :return:
    """
    for i in range(len(chaine_car)):
        if chaine_car[i] != chaine_car[-i-1]:
            return False
    return True


def is_palindrome_bis(chaine_car):
    """

    :param chaine_car:
    :return:
    """
    resultat = True
    cpt = 0
    while cpt < len(chaine_car)//2+1:
        if chaine_car[cpt] != chaine_car[-cpt-1]: # ou chaine_car[len(chaine_car) - 1 -cpt]
            return False
        cpt += 1
    return True

print(is_palindrome_bis('aanaaaaarraaaaaaa'))

def occurence_char(chaine):
    s = set(chaine)
    d = {}
    for i in chaine:
        d[i] = d.get(i,0) +1
    return d