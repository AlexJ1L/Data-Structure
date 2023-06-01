#abriendo el archivo con with open
with open("Parte2\\Archivos\\Texto.txt",encoding="UTF-8") as archivo:
#leemos el archivo
    Contenido = archivo.read()
#Mostramos el contenido
#no es necesario cerrar el texto con close
print(Contenido)