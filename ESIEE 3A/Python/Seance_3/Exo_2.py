class CompteBancaire():
    def __init__(self, nom, solde = 0):
        self.nom = nom
        self.solde = solde
    
    def depot(self,somme):
        self.solde += somme

    def retrait(self,somme):
        self.solde -= somme

    def affiche(self):
        print("Le solde du compte de " + self.nom + " est " + str(self.solde) + " euros.")

def main():
    compte1 = CompteBancaire('Jean', 1000)
    compte1.retrait(200)
    compte1.affiche()
    compte2 = CompteBancaire('Marc')
    compte2.depot(500)
    compte2.affiche()

if __name__ == '__main__' :
    main()