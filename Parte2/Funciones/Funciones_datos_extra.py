#def frase(nombre,apellido,adjetivo):
#    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

#utilizando keyword argumets
#frase_resultado= frase(adjetivo="alegre",nombre="axel",apellido="Lh")
#print(frase_resultado)


#Creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo="tonto"): #valor por defecto
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"

#utilizando keyword argumets
frase_resultado= frase("axel","Lh","alegre") #Valor opcional
print(frase_resultado)