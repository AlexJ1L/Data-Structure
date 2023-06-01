#cambia el tipo de data de una columna
import pandas as pd
df = pd.read_csv("Parte2\Ejercicios2\Resolviendo_problemas\datos.csv")

#convertir a sring los datos de una columna
df ['edad'] = df['edad'].astype(str)

#mostar el tipo de dato del primer elmento de la columna edad
#print(df['edad'][0])

#tipo de dato
#print(type(df['edad'][0]))

#remplazando los datos "dalto" por "maestro"
#df['apellido'].replace("dalto","maestro",inplace=True)
#print(df['apellido'])

#eliminando las filas con datos vacios
#print(df)
#df =df.dropna()
#print(df)

#eliminando las filas repetidas
#df = df.drop_duplicates()
#print(df)

#creando un csv con el datafram resultante (limpio)
df.to_csv("Parte2\Ejercicios2\Resolviendo_problemas\datos_limpios.csv")
