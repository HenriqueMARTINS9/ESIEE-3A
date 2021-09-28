class CompteBancaire :
    def __init__(self,name,solde=0):
        self.name=name
        self.solde=solde
    
    def retrait(self,nb):
        self.solde -= nb

    def depot(self,nb):
        self.solde += nb

    def affiche(self):
        print(self.name, "possède", self.solde, "€")

compte1 = CompteBancaire('Jean',1000)
compte1.retrait(200)
compte1.affiche()
compte2 = CompteBancaire('Marc')
compte2.depot(500)
compte2.affiche()