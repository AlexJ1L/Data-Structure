import re 

texto = """Hola maestro, como abesta es la cadena 1. como esta mi capitan
Esta es la 221 linea de textoab
y esta es la 3 linea de codigo__"""

#Buscar si la palabra es existente
#resultado =re.search("es la",texto)
#print(resultado)

#Haciendo una busqueda simple ,flags=re.IGNORECASE es para ignorar las min y may
#resultado =re.findall("esta",texto,flags=re.IGNORECASE)
#print(resultado)

#\d   Busca digitos numericos del 0 al 9
#resultado =re.findall(r"\d", texto)
#print(resultado)

#\D   busca TODO MENOS digitos numericos del 0 al 9
#resultado =re.findall(r"\D", texto)
#print(resultado)

#\w   busca caracteres alfanmericos [a-z,A-Z,0-9,_]
#resultado =re.findall(r"\w", texto)
#print(resultado)

#\W   Busca TODO MENOS caracteres alfanmericos [a-z,A-Z,0-9,_]
#resultado =re.findall(r"\W", texto)
#print(resultado)

#\s   Busca espacios en blanco, espacios,tab,salto de linea
#resultado =re.findall(r"\s", texto)
#print(resultado)

#\S   Busca TODO MENOS espacios en blanco, espacios,tab,salto de linea
#resultado =re.findall(r"\S", texto)
#print(resultado)

#. Busca TODO MENOS saltos en linea
#resultado =re.findall(r".", texto)
#print(resultado)

#\n Busca TODO MENOS saltos en linea
#resultado =re.findall(r"\n", texto)
#print(resultado)

#\ Cancelar caracteres especiales
#resultado =re.findall(r"\.", texto)
#print(resultado)

#armando una cadena que busque un numerom seguido de un punto y un espacio
#resultado =re.findall(r"\d\.\s",texto)
#print(resultado)

#buscando el principio de una linea
#^ Busca el comienzo de una linea
#resultado =re.findall(r"^Hola", texto)
#print(resultado) 

#^ Busca el comienzo de una linea con ,flags=re.M activa la multilinea
#resultado =re.findall(r"^Esta", texto,flags=re.M)
#print(resultado) 

#$ Busca el final de una linea con ,flags=re. activa la multilinea
#resultado =re.findall(r"capitan$", texto,flags=re.M)
#print(resultado) 

#{n} Busca n cantidad de veces el valor de la izquierda
#resultado =re.findall(r"\d{3}\s", texto)
#print(resultado)

#{n,m} al menos n, como maximo m
#resultado =re.findall(r"\d{1,4}", texto)
#print(resultado)

#{n,m} al menos n, como maximo m
#resultado =re.findall(r"ab{1,4}", texto)
#print(resultado)

#{n,m} al menos n, como maximo m Sola palabras juntas abab = ab
#resultado =re.findall(r"(ab){2}", texto)
#print(resultado)

#{n,m} al menos n, como maximo m Nos devuelve cualquiera de los valores "aa","ab","ba","bb"
#resultado =re.findall(r"[ab]{2}", texto)
#print(resultado)

# | Busca una cosa o la otra
resultado =re.findall(r"\d{1,4}|Hola", texto)
print(resultado)