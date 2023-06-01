#Creando una funcion simple 
def saludar():
    print("Hola,Buenas tardes axel ¿Como estas?")

#Ejecutando funcion
saludar()

def saludar (nombre):
    print(f"Hola,buenas tardes {nombre} ¿Como estas?")
saludar("jose")

#Crear una funcion que tenga parametros
def saludar (nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "unknow"


    print(f"Hola,buenas tardes {adjetivo} ¿Como estas?")
    
saludar("camila","mujER")
saludar("jose","hombre")
saludar("jose","nobuienas")


#Crear una funcion que nos retorne multiples valores
def calculo (num):
    caracteres = "abcdefghi"
    num_entero = str(num) #Obtiene el primer numero que le pases
    num = int(num_entero[0])
    
    c1  = num -2
    c2  = num 
    c3  = num -5
    contraseña = f"{caracteres[c1]}{caracteres[c2]}{caracteres[c3]}{num * 2}" #2, 4, -1, 8 cei8 (8 es el numero ingresado * 2)
    return contraseña,num

#Desempaquetando la funcion
password, primer_numero = calculo(583) 

#Mastrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña es: {password}")
print(f"El número utilizado para crearlo fue: {primer_numero}")
