#Creando funcio que suma numeros
def sumar_dos():
    #iniciando un bucle
    while True:
    #Pidiendo numeros
        a = input("numero 1: ")
        b = input("numero 2: ")
        #Intentando convertirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
        #Si lanzo una excepción, pedirle que reingrese los datos
        except Exception as e:
            print("Te pedi un numero")
            print(f"ERROR: {type(e).__name__}")
        #Si todo salio bien terminamos el bucle
        else:
            break
        finally:
            print("Esto se ejecuta siempre pase lo que pase en el codigo") #Manejo de excepción finalizado
    #Mostramos el resultado
    return resultado


print(sumar_dos())