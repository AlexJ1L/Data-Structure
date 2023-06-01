frase = input ("Dime una frase: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)

print(f"Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo.")

print(f"Axel lo diria en {cantidad_de_palabras*100 // 2 *1.3 / 100} segundo.")

if cantidad_de_palabras >= 120:
    print("Esto es demasiado para mi")