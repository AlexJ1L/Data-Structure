"""Hacer una para cada OPM (Suma, Resta, Multi, Div)"""
def Suma(*n):
    suma = sum([*n])
    print(suma)

def Resta(nr1,nr2):
    print(nr1 - nr2)

def Multiplicar(nm1,nm2):
    print(nm1 * nm2)

def Dividir(nd1,nd2):
    D = int(float(nd1 / nd2))
    print(D)


Sum = Suma(20,392,293)
Resta = Resta(60,20)
Mult = Multiplicar(20, 10)
Dividir(13, 12)