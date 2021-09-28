a = input("entrez une chaîne de charactères : ")
if a.find('@') >0 and a.endswith('.com') == True :
    print('%s est une chaîne valide' %a)
else :
    print('ERROR la chaîne est invalide')