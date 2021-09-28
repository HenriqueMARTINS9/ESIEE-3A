class Domino:
    def __init__(self,A,B):
        self.A = A
        self.B = B

    def affiche_points(self):
        print("face A :" ,self.A ,"\nface B :",self.B)
    
    def total(self):
        return self.A+self.B

a = Domino(4,6)
a.affiche_points()
x = a.total()
print(x)