class Clase():
    def __new__(cls): #metodo estatico que devuelve el dato
        print("new")
        return super().__new__(cls)
    def __init(self):
        print("init")

c = Clase()
    

