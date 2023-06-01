#DATO.METODO ()
Str = "Hello world!"


print(Str.upper())
print(Str.lower())
print(Str.capitalize())


#PARA BUSCAR EL INDICE DE EL DATO 
print(Str.find("Hello"))
print(Str.find("e"))
print(Str.find("h")) #Si no existe el dato da como resultado el indice -1

#
Numeric = "29472649" #ES UN TEXTO (POR QUE TIENE COMILLAS) PARA QUE DEJE DE SER UN TEXTO SE LE QUITAN LAS COMILLAS
Letras = ""

print(Numeric.isnumeric()) #SI EL TEXTO SON SOLO NUMEROS DA TRUE Y SI CONTIENE SIGNOS DA FALSE
print(Numeric.isalpha())   #EL ESPACIO Y LOS NUMEROSO NO SON "Alpha Numerico" 


print(Str.count("j")) #CUENTA LA CANTIDAD DE VECES QUE ESTA FUNCIONA CON LETRA "a" O CON PALABRAS "hola"

print(len(Str)) #SIRVER PARA CONTAR LOS CARACTERES DE UN DATO (ES UNA FUNCION)
print(Str.replace("ello", "ola")) #REEMPLAZA LOS DATOS POR OTRO
print(Str.split()) #SEPARA EL DATO FORMANDO UNA LISTA