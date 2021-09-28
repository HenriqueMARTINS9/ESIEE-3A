f = open("exo22.txt",'r')
File = f.readlines() #crée une liste composé des lignes du fichier


for l in File :
    clean = l.rstrip() #enlève le retour à la ligne
    print(clean)
    if clean.find('@') >0 and len(clean)-clean.rindex(".") > 2: #it can be .com or .fr,.it ...
        print('is an Email')