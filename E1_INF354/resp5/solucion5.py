import pandas as pd

df = pd.read_csv("SaYoPillow.csv", sep=",")
print(df.sample(14))# Conjunto de Datos

explicativas=df.drop(columns='clase')  # Datos
objetivo=df.clase # Objetivo

from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier(max_depth=4)
model.fit(X=explicativas, y=objetivo)


from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(16,8))
plot_tree(decision_tree=model,feature_names=explicativas.columns,filled=True,fontsize=10);

# Calculado Una predicion
# a=explicativas.sample()
# a