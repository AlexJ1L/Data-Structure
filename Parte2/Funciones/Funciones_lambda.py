numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

#creando una funcion lambda para multiplicar por dos
Multiplicar_por_dos = lambda x : x*2
#print(Multiplicar_por_dos(5))


#creando funcion comun que diga si es par o no
#def es_par(num):
#   if (num %3==1):
#        return True

#creando filter con una funcion comun
#numeros_pares = filter(es_par,numeros)
#print(list(numeros_pares))



#Simplifico el codigo de arriba con la funcion lambda
numeros_pares = filter(lambda numero:numero%2==0,numeros)
print(list(numeros_pares))

