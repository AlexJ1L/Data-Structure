diccionario = {
    "nombre": "axel",
    "apellido": "LH",
    "edad": "17"
}
for Dic in diccionario:
    print(f"la calve es: {Dic}")

print( )

#Recorriendo diccionarios con items() para obtener la clave y el valor
for dic in diccionario.items(): #.items() Para mostrar todo
    DIC  = dic[0]
    value = dic[1]
    print(f"la clave es : {DIC} y el valor es: {value}")


#PARA ELIMINAR UNA COSA DE EL DICCIONARIO Y QUE CONTINUE
Frutas = ["Banana","Apple","Pear","Papaya","Orange","Durazno"]

for Fruta in Frutas:
    if Fruta == 'Orange':
        continue
    print(f"I will eat a: {Fruta}")

print(" ")
#Para terminar y quitar y el dato
#Evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in Frutas:
    if fruta == 'Orange':
        break
    print(f"I will eat a: {fruta}")
else:
    print("EL BUCLE TERMINO")


#Para recorrer una cadena de texto
cadena = "hola soy"
for letra in cadena:
    print(letra)



#METODO 1 >>>>>>>>>>>>
#for de forma larga
numeros = [20,29,2]

#Lista para que meta el resultado de "numero"
numero_duplicados = list()

for numero in numeros:
    numero_duplicados.append(numero*2)

print(numero_duplicados)


#METODO 2 >>>>>>>>>>>>>>>>>>>
#for en una sola linea de codigo
Forma2 = [x * 3 for x in numeros]

print(Forma2)