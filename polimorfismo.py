class Perro():
    def avanzar(self):
        print("4 patas")

class Perico():
    def avanzar(self): #mismmo metodo, diferente accion
        print("volar")


def mover(animal): #todos lo animales se van a mover
    animal.avanzar()

perro = Perro()
perico = Perico()
perro.avanzar()
perico.avanzar()
print("---------------------------------------------------------")
print("perico =")
mover(perico)
print("perro =")
mover(perro)