with open("Parte2\\Archivos\\Texto.txt",'w',encoding="UTF-8") as archivo:
    #Sobre escribiendo el archivo
    #archivo.write("dawodaowdakwdksdddddddsaaaasdshola como estan todos los que son personas")
    
    #Agregando 2 lineas con writelines
    archivo.writelines(["-Hola como estan todos?\n","-dawodaowdakwdks\n"])
    #Agregando 2 lineas mas
    archivo.writelines(["-Hola s2ds2sdsa\n","-dawwad11111wdks"])