#Falto el maestro y los alumnos van a armar la clase.
#Perdi el nombre y la edad de los compañeros

#Funcion para obtener al asistente y al profesor segun la edad: 
def obtener_compañeros(cantidad_de_compañeros):
    #creando la lista con los compañeros
    Compañeros = []
    
    #Ejecutando un for para pedir información de cada compañero
    for i in range (cantidad_de_compañeros):
        nombre= input("Ingrese el nombre del compañero: ")
        edad= int(input("Ingrese la edad del compañero: "))
        Compañero = (nombre,edad)
        
        #Agregando la información a la lista
        Compañeros.append(Compañero)
    
    #Ordenando de menor a mayor según su edad
    Compañeros.sort(key=lambda x: x[1])
    
    #Compañeros [x] devuelve una tupla con (nombe,edad) y despues accedemos al nombre
    #Para definir al asistente y al prfesor
    asistentes= Compañeros[0][0] #[(1,2),(1,2),(1,2)]
    profesor = Compañeros [-1][0]
    
    #Retornamos una tupla
    return asistentes,profesor

#Desempaquetamos lo que nos rotorna la funcion
asistente,profesor = obtener_compañeros(5)

#Mostrando el resultado
print(f"El asistente es: {asistente} y el profesor es: {profesor}")


