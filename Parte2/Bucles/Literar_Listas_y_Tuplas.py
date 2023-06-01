animales = ["perro","gato","loro","cocodrilo","pez"]
Carros   = ["Urus","Versa","Gladiador","Can am"]
precios  = [640,552,325,125]

#for animal in animales:
#    print(f"El {animal} a muerto.")

#for dig in precios:
#    resultado = dig * 10
#    print(resultado)

""" Funcion "zip" es para recorrer mas de una lista al mismo tiempo """
#For anidados
for carros,precio,rango in zip(Carros,precios,range(1,5)):
    print(f"{rango}--El {carros} cuesta {precio}.")




#Forma no optima de recorrer una lista por su indice
for num in range(len(precios)):
    print(precios[num])

#Forma optima de recorrer una lista con su indice
for num1 in enumerate(precios):
    indice = num1[0]
    valor  = num1[1]
    print(f"El indice es: {indice} y el valor es: {valor}.")

#Usando el for/else
for numeros in precios:
    print(f"Ejecutando el ultimo bucle, valor actual: {numeros}")
else:
    print("El bucle termino")


#Tambien funciona para las tuplas