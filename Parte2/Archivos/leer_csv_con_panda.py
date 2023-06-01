import pandas as pd

#usamos la funcion read_csv para leer el archivo CSV
df = pd.read_csv("Parte2\\Archivos\\datos.csv")#,names= ["name","lastname","age"]
df2 = pd.read_csv("Parte2\\Archivos\\datos.csv")

#obteniendo los datos de la columna nombres
nombres = df["nombre"]


#ordenando el dataframe de forma ascendente por la edad
#df_ordenando = df.sort_values("edad")

#print(df_ordenando)


#ordenando el dataframe de forma descendente por la edad
#df_ordenando2 = df.sort_values("edad",ascending=False)

#print(df_ordenando2)


#Concatenando los dos dataframe
#df_concatenado = pd.concat([df,df2])
#print(df_concatenado)


#accediendo a la primer fila con head()
#primer_fila = df.head(3)
#print(primer_fila)


#accediendo a las ultimas fila con tail()
#ultimas_filas = df.tail(2)
#print(ultimas_filas)

#accediendo a la cantidad de filas y columnas con shape
#filas_y_columnas_totales,columnas_totales= df.shape
#print(filas_y_columnas_totales)
#print(columnas_totales)


#obteniendo data estadistica del datafram:
#df_info = df.describe()
#print(df_info)


#accediendo a un elemento especifico del df con loc en la fila 2
#elemento_especifico_loc = df.loc[2,"edad"]
#print(elemento_especifico_loc)


#accediendo a un elemento especifico del df con iloc en la fila 2
#elemento_especifico_loc = df.iloc[2,2]
#print(elemento_especifico_loc)


#accediendo a todas las filas de una columna
#apellidos = df.iloc[:,1]
#print(apellidos)


#accediendo a la filas 3 con loc
#fila_3 = df.loc[2,:]
#print(fila_3)

#accediendo a la filas 3 con iloc
#fila_3 = df.iloc[2,:]
#print(fila_3)

#accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"]>30,:]
print(mayor_que_30)


#cadena= "0123456789"
#Para revertir un string                    print(cadena[::-1])="9876543210"
#Para eliminar datos de un string R>L       print(cadena[:-4]) ="012345"
#Para poner un punto de partida y un final  print(cadena[2:4]) ="23"
#Para poner los datos de un string L>R      print(cadena[:4])  ="0123"
#print(cadena[2:4]) 
#print(df)