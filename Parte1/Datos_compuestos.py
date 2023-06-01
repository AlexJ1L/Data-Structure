#INDICE 1 ,ELEMENTO 0
lista = ["Axel", "LH", True, 1.72]
print(lista[0])    
#SIEMPRE VAN CON CORCHETE PARA MOSTRARLO

#LA LISTA VA CON NUMEROS DE INDICE
print(lista[1])



#LAS TUPLAS NO SE PUEDEN MODIFICAR >>>>>>>>>>>
#NO SE PUEDE MODIFICAR DE NINGUNA FORMA SON INMUTABLES
#print(dir(tulpa)) #Solo se puede remover y eliminar elementos
tupla = ("Axel", "LH", True, 1.78)
print(tupla[0])


#ESTO NO SE PUEDE >>>>>>>>>>>>>>
#ESTE CODIGO HACE QUE "Axel" LO QUITEMOS Y POGAMOS A "hola" >>>>>>>>>>>>>>>>>>

#Tupla[0] = "hola"
#print(Tupla[0])


#CREANDO UN CONJUNTO >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#NO SE PUEDEN REPETIR LOS DATOS
#LOS CONJUNTOS NO SE PUEDEN MODIFICAR 
#NO SE PUEDE ACCEDER POR EL INDICE 
#SON DATOS DESORDENADOS 
conjunto = {"Axel", "LH", True, 1.40}
print(conjunto)

#NO SE PUEDE ACCEDER AL DATO POR EL INDICE >>>>>>>>>>
#print(conjunto[0])



#CREANDO UN DICCIONARIO >>>>>>>>>>>>>>>>>>
diccionario = {
    "nombre": "Axel",
    "edad": 17,
    "altura": 179,
    "esta_emocionado": True,
    "dato_duplicado":"Axel"
    #"CLAVE": "VALOR",
}
#print(diccionario)

#LOS CONJUNTOS VAN CON LETRAS POR CLAVE Y VALOR
print(diccionario['altura'] +10)

