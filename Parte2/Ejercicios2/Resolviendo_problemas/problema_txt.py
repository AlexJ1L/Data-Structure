#crear 2 listas, una con nombres y otra con apellidos
nombres = ["Lucas","Matias","Camila","Pedro","Roberto"]
apellidos = ["Dalto","Zing","Lorenzana","Herrera","Gomez"]

#Registrar esta informacion en un TXT de forma óptima

with open("Parte2\\Ejercicios2\\Resolviendo_problemas\\nombres_y_apellidos.txt","w") as archivo:
    archivo.writelines("los datos son:\n\n")
    [archivo.writelines(f"nombres: {n}\nApellidos: {a}\n-----------------\n") for n,a in zip(nombres,apellidos)]
#Buscar una forma mas óptima