def askDate():
    print("entrez une date supérieur à l'an 1583 et inférieur à l'an 9999 au format DD/MM/YYYY")
    year=0
    while year<1583 or year>9999:  #la boucle se répète si les condition sur l'année ne sont pas respéctés.
        entry = input("date : ")
        year = int(entry[6:10]) #on récupère le substring contenant l'année
        if year<1583 or year>9999 :
            print("entrez une date supérieur à l'an 1583 et inférieur à l'an 9999 au format DD/MM/YYYY") #en cas de non respect des consignes on les re-affiche
    return int(entry[0:2]),int(entry[3:5]),int(entry[6:10]) #finalement en sortant de la boucle on retourne les données

def magicCalculation(day,month,year): #permet de calculer le jour
    c = (14-month)//12
    a = year-c
    m = month +12*c -2
    j = (day + a + a//4 -a//100 + a//400 +(31*m)//12)%7 #les formules sont donnés en consigne

    return(j)

def DayAssignement (nb) :
    jours = {0:"dimanche",1:"lundi",2:"mardi",3:"mercredi",4:"jeudi",5:"vendredi",6:"samedi"} #on crée un dictionaire qui retournera le bon str en fonction du jour
    return jours[nb]
    

j,m,y = askDate() #on assigne le jour à j, le mois à m et l'année à y

d = magicCalculation(j,m,y) #on calcule le jour de la semaine

print(DayAssignement(d)) #on affiche le str correspondant au jour