#si el modulo estuviera dentro de una carpeta en la misma ruta
#import Funciones_creadas.Saludo_con_Modulo as m_saludar

#saludo= m_saludar.saludar("ASFS")
#print(saludo)

import sys

#print(sys.builtin_module_names)
#Para acceder a un modulo de otra forma 
sys.path.append("C:\\Users\\Axel\\Desktop\\Python2\\Parte2\\Funciones_creadas")
print(sys.path)