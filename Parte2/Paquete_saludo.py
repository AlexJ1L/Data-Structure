#python Parte2\Paquete_saludo.py
import Paquete.Saludo_normal
import Paquete.Saludo_raro


#print(type(Paquete.__path__)) #Para ver que tipo de dato es
#print(Paquete.__path__) #Para ver la locacion del documento

print(Paquete.Saludo_normal.saludar("axel"))
print(Paquete.Saludo_raro.saludar_raro("axel"))