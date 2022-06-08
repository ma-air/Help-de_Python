class Intro():
    ntrover=9
    def __init__(self,valor):
        self.valor=valor
    def segundo(self):
        print("segundo")
    def tercero(self):
        print(tercero)

dato = Intro("valor")
dir(dato)
print (dir(dato))

print(isinstance(dato, Intro))
print(hasattr(dato,"Introver")) #esta clase no puede acceder a este atributo