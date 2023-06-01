import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Parte2\\Ejercicios2\\Archivos_problemas_graficos\\cofla_ingresos.csv")

#Creando el grafico
sns.barplot(x="Fuentes",y="Ingresos",data=df)

#obteniendo el total de ingresos
total_ingresos= df['Ingresos'].sum()

#mostrando el total de ingresos
print(f"El total de ingresos es de: ${total_ingresos} USD")
#mostrando la grafica
plt.show()