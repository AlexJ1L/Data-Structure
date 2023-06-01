#Creando mi propia excepción personalizada
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Impresionante, cometiste el el siguente error: {err}")
        
    #raise ZeroDivisionError("No se puede dividir entre 0")
#Lanzando mi propia excepción
try:
    raise MiExcepcion("JAJAJAJAJAJAJA")

#Manejandola
except:
    print("Como vas a cometer ese error")