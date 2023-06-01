numeros = {2,23,46,32,12}

#Encontrando el numero mayor de una lista
numero_mas_alto = max(numeros) #Funcion "max"
print(numero_mas_alto)

#Encontrando el numero menor de una lista
numero_mas_alto = min(numeros) #Funcion "min"
print(numero_mas_alto)

#Redondeando a decimales
numero = round(122.22332,2)
print(numero)

#Retorna False --> 0, Funciones vacias, False, None
#Retorna True --> Un numero distinto a 0, True, Cadena de texto o numeros
resultado_bool = bool(0)
print(resultado_bool)

#Retorna True, si todos los valores son verdaderos 
resultado_all = all([2,"Hola",[232,52]])
print(resultado_all)

#Suma todos los valores de un iterable
sum_total = sum(numeros)
print(sum_total)