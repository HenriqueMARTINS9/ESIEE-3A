liste = ["a","b","c"]

result = set()
for i in range(2**len(liste)) :
    for k in liste :
        result.add(k)

print(result)