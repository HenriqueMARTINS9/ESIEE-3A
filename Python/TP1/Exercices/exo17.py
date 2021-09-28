chaine = input('entrez une chaine : ')
array = []
reversedChain = ''
print(chaine)
for i in chaine :
    array.append(i)
array.reverse()
for i in array :
    reversedChain = reversedChain + i
print(reversedChain)

if chaine == reversedChain :
    print(chaine +' est un palyndrome')
else : print(chaine +" n'est pas un playndrome")