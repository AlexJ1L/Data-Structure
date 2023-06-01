Lista = list(["Hola","Axel","178"])
#las listas son mas flexibles si queremos mover o modificar los datos

cadena = ([4736,62])

print(len(Lista)) #Nos devuelve la cantidad de elementos de la lista

#AGREGAR UN ELEMENTETO A LA LISTA
Lista.append("Jose")
print(Lista)

#PARA COLOCAR UN ELEMENTO CON EL INDICE
Lista.insert(2,"Ojo")
print(Lista)

#PARA AGREGAR VARIOS ELEMENTOS A LA LISTA 
Lista.extend([True,False,"Rapido","Carro",347847])
print(Lista)

#Remueve elementos por su Dato
Lista.remove("Carro")
print(Lista)

#ACOMODA LA LISTA DE FORMA ASCENDENTE
#Solo acepta numeros y True y False
cadena.sort()
print(cadena)

#LOS CAMBIA DE POSICION CONTRARIA A DONDE ESTABAN
cadena.sort(reverse= True)
print(cadena)

#LOS CAMBIA DE POSICION CONTRARIA A DONDE ESTABAN
Lista.reverse()
print(Lista)

#Index BUSCA DATOS COMPLETOS No separados
#EXAMPLE
Api = ([293,3487,73])

print(Api.index(73))
print(Api)

#
#print(dir(set(["jajaj","dawdasd"]))) 
#  #Solo se puede remover y eliminar elementos

tulpa= (383,89347,"jgudj")

print(dir(tulpa))