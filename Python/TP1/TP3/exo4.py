import math

class Fraction :
    def __init__(self,num,denum):
        self.num=num
        self.denum=denum
    
    def affiche(self):
        print(str(self.num)+"\n"+"-"+"\n"+str(self.denum))
    
    def __add__(self,other):
        a1=self.denum
        a2=self.num
        b1=other.denum
        b2=other.num
        if a1 == b1:
            return(Fraction(a2+b2,a1))
        else :
            gcd = math.gcd(a1,b1)
            if gcd ==1 :
                gcd= a1*b1
            if gcd<a1:
                A=a1/gcd
                a2=a2/A
            elif gcd>a1:
                A=gcd/a1
                a2=a2*A
            if gcd<b1:
                A=b1/gcd
                b2=b2/A
            elif gcd>b1:
                A=gcd/b1
                b2=b2*A
            a1=gcd
            b1=gcda1=self.denum
        a2=self.num
        b1=other.denum
        b2=other.num
        return(Fraction(a1*b1,a2*b2))
        b1=other.denum
        b2=other.num
        if a1 == b1:
            return(Fraction(a2+b2,a1))
        else :
            gcd = math.gcd(a1,b1)
            if gcd ==1 :
                gcd= a1*b1
            if gcd<a1:
                A=a1/gcd
                a2=a2/A
            elif gcd>a1:
                A=gcd/a1
                a2=a2*A
            if gcd<b1:
                A=b1/gcd
                b2=b2/A
            elif gcd>b1:
                A=gcd/b1
                b2=b2*A
            a1=gcd
            b1=gcd
        return(Fraction(a2-b2,a1))

    def __mul__(self,other):
        a1=self.denum
        a2=self.num
        b1=other.denum
        b2=other.num
        return(Fraction(a1*b1,a2*b2))
    
    def __truediv__(self,other):
        a1=self.denum
        a2=self.num
        b1=other.denum
        b2=other.num
        return(Fraction(a1*b2,a2*b1))

        
            

F1 = Fraction(1,3)
F2 = Fraction(1,2)

F3 = F1+F2
F4 = F2-F1
F5 = F1*F2
F6 = F1/F2
F3.affiche()
F4.affiche()
F5.affiche()
F6.affiche()