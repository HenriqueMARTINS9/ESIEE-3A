pSeuil = 2.3
vSeuil = 7.41


p = float(input('entrez la pression :'))
v = float(input('entrez le volume :'))
warnP = p>pSeuil
warnV = v>vSeuil

if warnP == True and warnV == True:
    print("Arret Immédiat")
if warnP == True and warnV == False:
    print("Augmentez le volume de l'enceinte svp")
if warnP == False and warnV == True:
    print("Diminuez le volume de l'enceinte svp")
if warnP == False and warnV == False:
    print('Tout va bien')