x = int(input('entrez un nombre "x" : '))
f = open('exo21.txt',"w")

for i in range(x) :
    f.write(input('entrez une chaine : ')+'\n')
f.close()