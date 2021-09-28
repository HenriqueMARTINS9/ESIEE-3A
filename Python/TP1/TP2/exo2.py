import string 

def generator ():
    array=[]
    for i in string.ascii_lowercase :
        array.append(i)
    return array

def generator2 () :
    array=[]
    for i in string.ascii_lowercase :
        for a in range(2) :
            array.append(i)
    return array

def generatorN () :
    array=[]
    n = int(input("entrez un nombre"))
    for i in string.ascii_lowercase :
        for a in range(n) :
            array.append(i)
    return array

print(generatorN())