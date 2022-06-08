class Persona():
    def __init__(self):
        pass
    def brincar(self):
        print("BRINCAR")
    @classmethod
    def correr(cls):
        print("Corro")
    @staticmethod
    def nadar():
        print("Nado")



jose = Persona()
jose.nadar()