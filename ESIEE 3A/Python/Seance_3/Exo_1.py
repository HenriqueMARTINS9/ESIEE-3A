class Domino():
    def __init__(self, A, B):
        self.A = A
        self.B = B
    
    def affiche_points(self):
        print("face A: " + str(self.A) + " , face B: " + str(self.B))
    
    def totale(self):
        return self.A + self.B

def main():
    d = Domino(4,6)
    d.affiche_points()
    x = d.totale()
    print(x)

if __name__ == '__main__' :
    main()