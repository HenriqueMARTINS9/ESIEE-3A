def chiffrePorteBonnheur(nb):
    temporary =0
    nb = int(nb)
    while nb >10:
        temporary =0
        print(nb)
        liste = [int(a) for a in str(nb)]
        for i in liste :
            a = i**2
            temporary += a
        nb = temporary
    if(nb == 1):
        print(nb ," est un chiffre porte bonheur")
    else :
        print(nb, " n'est pas un chiffre porte bonheur")

entry = input("entrez un nombre")
chiffrePorteBonnheur(entry)