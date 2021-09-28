import math

class Fraction():
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def affiche(self):
        print(str(self.num) + "/" + str(self.denom))    

    def addition(self,autre_fraction):
        num1 = self.num
        denom1 = self.denom
        num2 = autre_fraction.num
        denom2 = autre_fraction.denom
        pgcd = math.gcd(denom1, denom2)
 
        if denom1 == denom2 :
            num = num1 + num2
            denom = denom1

        if pgcd == 1 :
            num = denom1 * num2 + denom2 * num1
            denom = denom1 * denom2 

        if pgcd < denom1 :
            num = num1 / (denom1 / pgcd) + num2
            denom = denom2

        elif pgcd > denom1:
            num = num2 / (denom2 / pgcd) + num1
            denom = denom1

        if pgcd < denom2 :
            num = num2 / (denom2 / pgcd) + num1
            denom = denom1

        elif pgcd > denom2:
            num = num1 / (denom1 / pgcd) + num2
            denom = denom2

        return Fraction(num, denom)
        
    def multiplication(self, autre_fonction):
        num1 = self.num
        denom1 = self.denom
        num2 = autre_fraction.num
        denom2 = autre_fraction.denom


def main():
    f = Fraction(3,4)
    f.affiche()
    g = Fraction(1,6)
    g.affiche()
    r1 = f.addition(g) 
    r1.affiche()
    r2 = f / g
    r2.affiche()

if __name__ == '__main__' :
    main()