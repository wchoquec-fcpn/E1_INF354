import pandas as pd
import seaborn as sns

datos = pd.read_csv("SaYoPillow.csv", sep=",")  # Datos
sns.histplot(data=datos, x="sr1",  kde=True, hue="clase")

# en la grafica muestra una valor medio alto de estres 

# Niveles de estrés 
# (0 - bajo/normal, 
#  1: medio bajo, 
#  2: medio, 
#  3: medio alto,
#  4: alto) 

