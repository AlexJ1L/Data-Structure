diccionario = {
    "nombre": 'Axel',
    "Apellido": 'Lh',
    "Edad": '17'
    #"KEYS"; 'CLAVE',
}

print(diccionario.items()) #Muestra todas la Keys y las Claves
print(diccionario.keys()) #Muestra todas las Keys
print(diccionario.get("Edad")) #Muestra una Clave en especifico
#print(diccionario.get("hola")) #Si no encuentra nada lanza "None"

#diccionario.clear()
#print(diccionario)

diccionario.pop("nombre")
print(diccionario)
#Metodo Numerico >>>>>>>>>>>>>>>>>>
#Forma poco etica
Metodo2 = {
    0 : "Jose",
    1 : "Casa2",
    2 : "Calle sin salida" 
}
print(Metodo2[0])