diccionario = dict (nombre = "axel", apellido = "Lh")
#Las listas no pueden ser claves


diccionario1 = {frozenset(["dalto","casa"]): "jajaja"}


#Creando un diccionario con fromkeys() cambiando el valor por defecto: None
diccionario2 = dict.fromkeys(["Nombre","Apellido","Edad"])
diccionario3 = dict.fromkeys("ABCDE","Valor1")

#Creando un diccionario con fromkeys() cambieando el valor por defecto: "No se"
diccionario4 = dict.fromkeys(["nombre","apellido"],"No se")


print(diccionario2)
print(diccionario3)
print(diccionario4)