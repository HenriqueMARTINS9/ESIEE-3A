def compterMots(entry):
    i= 0
    array =[]
    dictionnaire = {}
    for x in entry : array.append(x)

    while i < len(array):
        temporaryStr = ''
        for l in array:
            if l != ' ' :
                i = i+1
                temporaryStr = temporaryStr +l
            else :
                if dictionnaire.__contains__(temporaryStr) == False:
                    dictionnaire[temporaryStr] =1
                    temporaryStr = ''
                    i =i+1
                if dictionnaire.__contains__(temporaryStr) :
                    dictionnaire[temporaryStr] = dictionnaire[temporaryStr]+1
                    temporaryStr = ''
                    i =i+1
    return dictionnaire  

paragraf = input('entrez un paragraphe')

print(compterMots(paragraf))