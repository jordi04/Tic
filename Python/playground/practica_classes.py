class Llibre:
    def __init__(self, propietari, read):
        self.propietari = propietari
        self.read = read

    def change(par):
        par.read=not(par.read)

    def check(par):
        if par.read == False:
            print("Todavía no has leído este libro")
        else:
            print("Ya has leído este libro")

llibre = Llibre("Jordi Roca Bonnín", True)
llibre.check()
llibre.change()
llibre.check()
    