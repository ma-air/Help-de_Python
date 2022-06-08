def primerD(funcion):
    def funcionDecorada(*args,**kkwars):
        print("Primer decorador")
    return funcionDecorada


@primerD #siempre va a imprimir Primer decorador
def funcion():
    print("Mi primer decorador")


funcion()