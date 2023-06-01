import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Parte2\\Ejercicios2\\Archivos_problemas_graficos\\Pedos.csv")

#Creando el grafico
sns.lineplot(x="Fecha",y="Pedos",data=df)

#creando un punto en el momento de mas pedos
plt.plot("01-09",17,"o")

#mostrando la grafica
plt.show()