chaine ='Ecrire l’inverse d’une chaine'
array = []
reversedChain = ''
print(chaine)
for i in chaine :
    array.append(i)
array.reverse()
for i in array :
    reversedChain = reversedChain + i
print(reversedChain)