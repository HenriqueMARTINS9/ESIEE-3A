from selectmenu import SelectMenu

class Film :
    def __init__(self,title,year,number,cost,gain):
        self.title = title
        self.year = year
        self.number = number
        self.cost = cost
        self.gain = gain
        self.acteurs = []

    def __str__(self):
        return ("Film : \nTitre = %s\nAnnée de sortie = %s\nNuméro d'épisode = %s\nCout = %s Million€\nRecette = %s Million€\n %s"%(self.title,self.year,self.number,self.cost,self.gain,self.acteurs))

class Acteur :
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.film = None
        self.personnages = []
    
    def __str__(self):
        return("Acteur :\nNom = %s\nPrénom = %s"%(self.name,self.surname))

class Personnage :
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.acteur = None
    
    def __str__(self):
        return("Personnage :\nNom = %s\nPrénom = %s"%(self.name,self.surname))

class Gentil(Personnage):
    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.force=True

    def __str__(self):
        return(super().__str__+"est du bon coté de la force")

class Méchant(Personnage):
    """return l'attribut booléen "obscure" d'un personnage """
    def __init__(self,name,surname):
        self.obscur = True
        super().__init__(name,surname)

    def __str__(self):
        return(super().__str__+"est du mauvais coté de la force")

E1 = Film("La menace Fantome","1999",'1','4','15')
a1 = Acteur("Neesson","Liam")
a1.personnages = [Gentil("Qui-Gon","jinn")]
a2 = Acteur("McGregor","Ewan")
a2.personnages = [Gentil("Obi-wan","kenobi")]
a3 = Acteur("Portman", "Nathalie")
a3.personnages = [Gentil("Padmé","")]
a4 = Acteur("McDiarmid","Ian")
a4.personnages = [Méchant("Dark","Sidious")]

def askComplete(film) :
    film = Film(input("Entrez un titre : "),input("année de sortie : "),input("numéro d'épisode : "),input("cout : "),input("recette : "))
    result1 = "oui"
    result2 = "oui"
    i = 0
    while(result1 == "oui") :
        menu1 = SelectMenu()
        menu1.add_choices(['oui','non'])
        result1 = menu1.select("voulez vous ajouter un acteur au film ? %d ont déja été ajoutés"%len(film.acteurs))
        result2 = result1
        if(result1 == "oui") :
            film.acteurs.append(Acteur(input("entrez le nom : "),input("entrez le prénom : ")))
            while(result2 == "oui") :
                menu2 = SelectMenu()
                menu2.add_choices(['oui','non'])
                result2 = menu2.select("voulez vous ajouter un personnage à cet acteur ? %d ont déja été ajoutés"%len(film.acteurs[i].personnages))
                if(result2 == "oui") :
                    menu3 = SelectMenu()
                    menu3.add_choices(['gentil','Méchant'])
                    result3 = menu3.select("Le personnage est il gentil ou méchant ?")
                    if(result3 == "gentil") :
                        film.acteurs[i].personnages.append(Gentil(input("entrez le nom : "),input("entrez le prénom : ")))
                    elif(result3== "Méchant") :
                        film.acteurs[i].personnages.append(Méchant(input("entrez le nom : "),input("entrez le prénom : ")))
        i=i+1

def main():
    select1 = ""
    index = 0
    currentFilm = "film"
    while(select1 != "quitter"):
        menu1 = SelectMenu()
        menu1.add_choices(['ajouter un film','quitter'])
        select1 = menu1.select("Menu Principal")
        if select1 == 'ajouter un film' :
            askComplete(currentFilm + str(index))
            index = index+1

main()

        