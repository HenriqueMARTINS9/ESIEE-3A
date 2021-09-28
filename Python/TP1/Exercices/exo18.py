a = input('entrez un email : ')

if a.find('@') >0 and a.rfind(".") == len(a) - 4:
    print(a)