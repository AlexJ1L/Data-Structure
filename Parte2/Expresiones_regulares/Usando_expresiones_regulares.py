#EJERCICIO 1 --------------->
import re 
text= "The quick brown fox jumps over the lazy dog"

x = re.search("^The.*dog$",text)

if x:
    print("SI")
else:
    print("NO")



#EJERCICIO 2 --------------->
#la cadena en la que se buscarán los patrones
text1 = "La fecha es 23/06/2021 y el telefono es +1-555-555-5555"

#El patron a buscar 
pattern1= r"\d{2}/\d{2}/\d{4}"

#El texto con el que se reemplazará el patrón
replacement = "Fecha Oculta"

#Reemplazar todas las apariciones del patrón en la cadena de texto
new_text = re.sub(pattern1,replacement,text1)

#imprimir el resultado
print("Texto modificado:", new_text)



#EJERCICIO 3 --------------->
text2= "remplazando todas las vocales por el asterisco"

new_text2 = re.sub("[aeiou]","*",text2)
print(new_text2)



#EJERCICIO 4 --------------->
email= "example@example.com"

pattern4 = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.match(pattern4,email)

if result:
    print("Dirección de correo válida")
else:
    print("Dirección de correo inválida")




#EJERCICIO 5 --------------->
text5= "Este es un ejemplo de una página web: https://www.example.com y también podemos visitarla"
pattern5 = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result5 = re.findall(pattern5,text5) 

print(result5)




#EJERCICIO 6 ---------------->
#detectar un numero CABA y ocultandolo
texto = "Hola Pedro, mi numero es: +54 11 4321-4321 +54 11 4321-4321"
pattern = r"\+\d{2}\s\d{2}\s\d{4}-\d{4}" 

remplazo =re.sub(pattern,"(Número oculto)",texto)
print(remplazo)