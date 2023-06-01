#Crear una funcion que verifique si un numero es primo
def numeros_primos(num):
    for i in range(2,num-1):
    #Si es divisible por alguno retornamos false y termina el bucle
        if num%i ==0: return False
    #si termina el bucle, significa que no fue divisible entonces es primo
    return True

#Creando funcion que retorne una lista con todos los primos
def primos_hasta(num):
    #creamos la lista
    primos= []
    for i in range(3,num+1):
        #verificamos si el valor es primo
        resultado = numeros_primos(i)
        #en caso de que sea lo agregamos a la lista
        if resultado==True: primos.append(i)
    
    #devolvemos la lista
    return primos

#creamos el resultado llamando a la funcion y lo mostramos
resultado= primos_hasta(2287)
print(resultado)