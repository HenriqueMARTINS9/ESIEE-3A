def compterMots(entry):
    dictionnaire = {}
    words = set(entry.split())
    for w in words:
       dictionnaire[w] = entry.count(w)
    return dictionnaire
            
paragraf = input('entrez un paragraphe')

print(compterMots(paragraf))