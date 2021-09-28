from itertools import zip_longest

class Poly:

    def __init__(self,*arg):
        self.coeffList=[]
        for i in arg :
            self.coeffList.append(i)
    
    def coeff(self):
        print(self.coeffList)

    def evalue(self,x):
        result=0
        for count, value in enumerate(self.coeffList):
            result += value*x**(count+1)
        return result

    def __add__(self,other):
        a = list(zip_longest(self.coeffList,other.coeffList, fillvalue=0))
        result =[]
        for i in a :
            result.append(sum(i))
        print('result ', result)
        return(Poly(*result))


P1= Poly(5,2)
P2= Poly(2,3,8)
P1.coeff()
print(P1.evalue(2))
P3 = P1+P2
P3.coeff()