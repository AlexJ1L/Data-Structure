animales = {"perro","gato","loro","cocodrilo","pez"}
Carros   = {"Urus","Versa","Gladiador","Can am"}
precios  = {"640","552","325","125"}

#for animal in animales:
    #print(f"El {animal} a muerto.")

#Funcion "zip" es para recorrer mas de una conjunto al mismo tiempo
for carros,precio,rango in zip(Carros,precios,range(1,5)):
    print(f"{rango}--El {carros} cuesta {precio}.")





#Forma optima de recorrer un conjunto con su indice
for num1 in enumerate(precios):
    indice = num1[0]
    valor  = num1[1]
    print(f"El indice es: {indice} y el valor es: {valor}.")

#Usando el for/else
for numeros in precios:
    print(f"Ejecutando el ultimo bucle, valor actual: {numeros}")
else:
    print("El bucle termino")


#Tambien funciona para las tuplas y listas y conjuntos