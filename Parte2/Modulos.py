#Importando un modulo y asignandole el nombre "m_saludar"

import Funciones_creadas.Saludo_con_Modulo as m_saludar #as Para cambiarle el nombre al modulo importado
saludo = m_saludar.saludar("Axel")
print(saludo) 

#Desde ese modulo, importamos dos funciones
#from Saludo_con_Modulo import saludar as N_saludo,saludar_raro as R_saludo #importamos dos funciones y les cambiamos el nombre

#Creamos las variables con los saludos
#saludo1 = N_saludo("Jose")
#saludo2 = R_saludo("Carmen")
#Mostramos los resultados
#print(saludo1)
#print(saludo2)

#Para ver las propiedades y metodos de el namespace
print(dir(m_saludar))

#
print(m_saludar,__name__)
print(__name__)