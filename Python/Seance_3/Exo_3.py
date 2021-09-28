class TableMultiplication():
    def __init__(self, nombre, i = 0):
        self.nombre = nombre
        self.i = i
    
    def prochain(self):
        print( self.i * self.nombre)
        self.i += 1

def main():
    tab = TableMultiplication(3)
    tab.prochain()
    tab.prochain()
    tab.prochain()
    tab.prochain()

if __name__ == '__main__' :
    main()