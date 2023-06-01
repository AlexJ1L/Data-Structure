#encoding="UTF-8" Para que detecte los caracteres 
Archivo = open("Parte2\\Archivos\\Texto.txt",encoding="UTF-8")

#Una vez que se lee no se puede leer
#print(archivo)#Codigo extraño por tener el programa abierto

#Leer archivos completos
#print(Archivo.read()) #Leer el documento de txt

#leer linea individual
#linea_12 = Archivo.readlines()
#print(linea_12)

#linea_13 = Archivo.readline()
#print(linea_13)

linea_14 = Archivo.readline(10)
print(linea_14)


#cerarr el archivo
Archivo.close()
