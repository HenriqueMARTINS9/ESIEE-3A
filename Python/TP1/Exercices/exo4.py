print('entrez un mot :')
w1= input()
print('entrez en un autre :')
w2= input()
words = (w1.lower(),w2.lower())

print('''le premier mot à apparaitre dans l'ordre alphabétique est "%s"''' %min(words))