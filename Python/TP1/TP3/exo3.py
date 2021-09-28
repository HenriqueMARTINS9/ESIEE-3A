class TableMultiplication:
    def __init__(self,n):
        self.n=n
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        self.i += 1

    def prochain(self):
        print(self.n, "x" ,self.i, "=", self.n*self.i)
        next(self)

tab = TableMultiplication(5)

tab.prochain()
tab.prochain()
tab.prochain()
tab.prochain()
