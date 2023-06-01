# Pedirle un dato al usuario 

""" Input SIEMPRE DEVUELVE UN TEXTO """
Nombre = input ("Inserte su Nombre: ")
#print(f"Tu nombre es: {Nombre}")


""" Como los inputs siempre develve un texto y como los textos solo se juntan da como resultado 66 ("6"*2=66) """
Numero = input("Inseta tu Altura: ")
Resultado = int(float(Numero))#*2
#print(f"El numero es: {Resultado}") #EL RESULTADO ES 66


""" Forma Numerica """
numero = input ("Inserta tu Edad: ")
resultado2 = int(numero) #*2
#print(f"El Numero es: {resultado2}")


Año = input ("Año de nacimiento: ")
Año = int(Año)

print(f"Tu nombre es: {Nombre}")
print(f"Tu altura es: {Resultado}")
print(f"Tu edad es: {resultado2}")
print(f"El año de nacimiento es: {Año}")



""" Convertir numero float a inter """
Dato = input ("Inserte un numero: ")
salida = int(Dato) #*2
print(f"El Numero es: {salida}")


""" Int Y float JUNTOS SON PARA OBTERNER COMO RESULTADO NUMEROS ENTEROS (4.6 *2 = 9)
int SE PUEDE RESIVIR NUMEROS ENTEROS SI SE PONE UN PUNTO (4.6 *2 = ERROR)
float PARA RESIVIR NUMEROS DECIMALES (4.6 *2 = 9.2) """