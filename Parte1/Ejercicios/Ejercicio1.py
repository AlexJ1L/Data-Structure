#Ejercicio A
cursos_min = 2.5
cursos_max = 7
cursos_promedio = 4
dalto_curso = 1.5


#CRUDO
crudo_promedio = 5
crudo_dalto = 3.5

#Ejercicio B
Tiempo_vacio_promedio = 100 - cursos_promedio *1000 // crudo_promedio / 10
Tiempo_vacio_dalto = 100 - dalto_curso *1000 // crudo_dalto / 10

#Diferencias A
diferencia_de_min = 100 - dalto_curso / cursos_min * 100
diferencia_de_max = 100 - dalto_curso *1000 // cursos_max / 10
diferencia_de_promedio = 100 - dalto_curso / cursos_promedio * 100


#Resultado A
print("--------Curso de dalton dura--------")
print(f"------Un {diferencia_de_min}% menos que el mas rapido")
print(f"------Un {diferencia_de_max}% menos que el mas lento")
print(f"------Un {diferencia_de_promedio}% menos que el promedio")
print( )
#Ejercicio B
print("--------Tiempo Eliminado--------")
print(f"-----Un curso promedio elimina un {Tiempo_vacio_promedio}% de tiempo vacio")
print(f"-----El curso dalto elimino un {Tiempo_vacio_dalto}% de tiempo vacio")
print( )
print("--------Tiempo Ahorrado--------")
print(f"---Ver 10 horas de este curso equivale a ver {cursos_promedio *100// dalto_curso /10} horas de otros cursos")
print(f"---Ver 10 horas de otros cursos equivale a ver {dalto_curso *100// cursos_promedio /10} horas de este curso")
