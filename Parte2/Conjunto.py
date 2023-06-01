Conjunto = set(["dato1","dato2",("dato en lista1","dato en lista2")])

print(Conjunto)

#
conjunto1 = frozenset (["dato1","dato2"])
conjunto2 = {conjunto1, "dato 3" }
print(conjunto2)


#conjunto b = 2,4,6,8,10 #Conjunto o SuperConjunto
#Conjunto a = 2,4,6 #SubConjunto de B

#Teoria de conjuntos
Conjunto1 = {1,3,5,7}
Conjunto2 = {1,5,7}
#PARA CONFIRMAR SI ES UN SUBCONJUNTO
#Forma 1
true  = Conjunto2.issubset(Conjunto1) #"issuset" sirver para saber si "Conjunto2" es un SubConjunto de "Conjunto1"
true2 = Conjunto2 <= Conjunto1
print(true)
print(true2)
print(  )
print(  )


#Para ver si es un SuperConjunto
#Forma 2
true2  = Conjunto2.issuperset(Conjunto1)
false2 = Conjunto2 > Conjunto1
print(false2)
print(true2)
print(  )
print(  )

#Para verificar si hay algun nuero en comun
comun = Conjunto2.isdisjoint(Conjunto1)

print(comun)