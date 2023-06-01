with open("Parte2\\Archivos\\Texto.txt",'a',encoding="UTF-8") as archivo:
#Append es para agregar y no sobre escribe como write

    #Agregando 2 lineas con writelines
    #archivo.writelines(["-muchas casas\n","-estan destruidas\n"])
    #Agregando lineas en blanco
    archivo.write("\n")
    for i in range(5):
     archivo.write(f"Linea {i+i} agregada\n")