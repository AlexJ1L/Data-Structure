import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Parte2\\Ejercicios2\\Archivos_problemas_graficos\\dispersion.csv")

#Creando el grafico
sns.scatterplot(x="Tiempo",y="Dinero",data=df)


#mostrando la grafica
plt.show()