import tkinter as t

def calculer():
    resultat = int(value1.get() + int(value2.get()))
    t3.set(resultat)

fenetre = t.Tk()
value1 = t.StringVar()
value2 = t.StringVar()
entree1 = t.Entry(fenetre, textvariable=value1, width=3)
entree1.pack()
entree2 = t.Entry(fenetre, textvariable=value2, width=3)
entree2.pack()
t3 = t.StringVar()
label = t.Label(fenetre, text=t3)
label.pack()
button = t.Button(fenetre, text='Calculer', command=calculer())
button.pack()

fenetre.mainloop()