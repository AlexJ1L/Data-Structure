#Forma no optima de sumar valores

"""
def suma(lista):
    numeros_sumados = 0
    for numeros in lista:
        numeros_sumados = numeros_sumados + numeros
    return numeros_sumados

resultado = suma([5,4,4,321])
print(resultado)
"""


#Lo mismo que arriba pero utilizando el operarador * como parametro (*args)
def suma_total(numeros):
    #print(*numeros) #Quita la lista
    return sum([*numeros])


resultado2 = suma_total([3,23,45,63,27])
print(resultado2)


#Utilizando el operador * como argumento (*args) Tiene que ser el ultimo parametro para seguir agregando
def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma ("axel",3,23,45,63,27)
#print(resultado)